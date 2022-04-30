import random
import math
import numpy as np
import scipy.stats as stats

def generate(data):
    choices = []
    average = 9
    x = 11

    choices.append({"text": 7, "answer": False, "feedback": "Incorrect"})
    choices.append({"text": 10, "answer": False, "feedback": "Incorrect"})
    choices.append({"text": 5, "answer": True, "feedback": "Correct!"})
    choices.append({"text": 3, "answer": False, "feedback": "Incorrect"})

    data["params"]["average"] = average
    data["params"]["x"] = x
    data["params"]["choices"] = choices
