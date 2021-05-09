import { Button } from 'react-bootstrap'

const Job = ({ job, onDelete }) => {
  return (
    <div
      className={`job`}
    >
      <h3>
        Running Job: {job.name}
        <Button
          variant="danger"
          onClick={() => onDelete(job.id)}
        >Stop</Button>
      </h3>
      <p>Started at: {new Date(job.start_date).toLocaleString()}</p>
      <p>Interval: {job.interval} seconds</p>
    </div>
  )
}

export default Job