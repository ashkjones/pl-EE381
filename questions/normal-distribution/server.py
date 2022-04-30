import random
import math
import numpy as np
import scipy.stats as stats

def generate(data):
    choices = []
    average = 9
    x = 11

    #selections available with correct answer
    choices.append({"text": 100, "answer": False, "feedback": "Incorrect"})
    choices.append({"text": 200, "answer": False, "feedback": "Incorrect"})
    choices.append({"text": 300, "answer": True, "feedback": "Correct! The number of students weighing between 120 and 155 lb is 500(0.6000) = 300"})
    choices.append({"text": 400, "answer": False, "feedback": "Incorrect"})

    data["params"]["average"] = average
    data["params"]["x"] = x
    data["params"]["choices"] = choices
