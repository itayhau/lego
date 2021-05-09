from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, jsonify
from flask_restplus import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, NotFound
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/lego_exc'

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

db = SQLAlchemy(app)
scheduler = BackgroundScheduler()
scheduler.start()

activate_parser = reqparse.RequestParser()
activate_parser.add_argument('seconds', type=int, required=True)
activate_parser.add_argument('method', type=int, required=True)


@api.route('/activate')
class Activate(Resource):
    @api.expect(activate_parser)
    def put(self):
        from jobs import CalculationMethods, process_mean, process_median

        args = activate_parser.parse_args()

        model = CalculationMethods(args.method)

        if model == CalculationMethods.MEAN:
            job = scheduler.add_job(process_mean, 'interval', seconds=args.seconds)
        elif model == CalculationMethods.MEDIAN:
            job = scheduler.add_job(process_median, 'interval', seconds=args.seconds)
        else:
            raise BadRequest('Model must be MEAN or MEDIAN')

        return jsonify(map_job(job))


@api.route('/deactivate/<string:job_id>')
class Deactivate(Resource):
    def put(self, job_id):
        job = scheduler.get_job(job_id)
        if job:
            scheduler.remove_job(job_id)
        else:
            raise NotFound(f'There is no existing job with id: {job_id}')


@api.route('/jobs')
class Jobs(Resource):
    def get(self):
        if len(scheduler.get_jobs()) == 0:
            return '', 204
        jobs = list(map(map_job, scheduler.get_jobs()))
        return jsonify(jobs)


@api.route('/results')
class Results(Resource):
    def get(self):
        from models import RecordModel

        since = datetime.now() - timedelta(minutes=10)
        res = db.session.query(RecordModel).filter(RecordModel.date > since).all()
        records = list(map(map_record, res))
        return jsonify(records)


def map_job(job):
    return {"id": job.id,
            "name": job.name.split("_")[1],
            "start_date": job.trigger.start_date,
            "interval": job.trigger.interval.seconds}


def map_record(record):
    return {"id": record.id,
            "method": record.model.name,
            "date": record.date,
            "result": record.result}


if __name__ == '__main__':
    app.run(debug=True)
