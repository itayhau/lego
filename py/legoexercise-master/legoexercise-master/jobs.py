import random
from models import RecordModel, CalculationMethods
from api import db


def process_mean():
    numbers = generate_random_list(20)
    mean = get_mean(numbers)
    record_model = RecordModel(result=mean, model=CalculationMethods.MEAN)
    db.session.add(record_model)
    db.session.commit()


def process_median():
    numbers = generate_random_list(10)
    median = get_median(numbers)
    record_model = RecordModel(result=median, model=CalculationMethods.MEDIAN)
    db.session.add(record_model)
    db.session.commit()


def get_mean(numbers):
    return sum(numbers) / len(numbers)


def get_median(numbers):
    #  maybe add validation of the amount of numbers
    #  maybe save the required len in configuration file
    middle = len(numbers) // 2
    numbers.sort()

    return (numbers[middle] + numbers[~middle]) / 2


def generate_random_list(length):
    return random.sample(range(100), length)
