import random
import math
import numpy as np
import scipy.stats as stats

def generate(data):
    choices = []
    average = 9
    x = 11

    #selections available with correct answer
    choices.append({"text": 0.7543, "answer": False, "feedback": "Incorrect"})
    choices.append({"text": 0.7034, "answer": False, "feedback": "Incorrect"})
    choices.append({"text": 0.7734, "answer": True, "feedback": "Correct! Let X be the random variable giving the number of heads that will turn up in 10 tosses. As such, the required probability P(3 <= X <= 6) = 0.7734"})
    choices.append({"text": 0.8654, "answer": False, "feedback": "Incorrect"})

    data["params"]["average"] = average
    data["params"]["x"] = x
    data["params"]["choices"] = choices
