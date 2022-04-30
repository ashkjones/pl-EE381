import random
import math
import numpy as np
import scipy.stats as stats

def generate(data):
    choices = []
    average = 9
    x = 11

    #selections available with correct answer
    choices.append({"text": "42%", "answer": False, "feedback": "Incorrect"})
    choices.append({"text": "36%", "answer": False, "feedback": "Incorrect"})
    choices.append({"text": "23%", "answer": True, "feedback": "Correct! The proportion of nondefective washers after calculations is 77%. Thus, the percentage of defective washers is 100% - 77% = 23%"})
    choices.append({"text": "57%", "answer": False, "feedback": "Incorrect"})

    data["params"]["average"] = average
    data["params"]["x"] = x
    data["params"]["choices"] = choices
