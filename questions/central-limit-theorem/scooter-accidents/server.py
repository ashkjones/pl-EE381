import random
import math
import numpy as np
import scipy.stats as stats

def generate(data):
    choices = []
    average = 9
    x = 11
    root = math.sqrt(average)

    # adding inclusive answers
    # correct_z = np.array([(x - 0.5) / root])
    # table_value = stats.zscore(correct_z)
    choices.append({"text": 0.6915, "answer": False, "feedback": "This is the probability there is less than 11."})
    choices.append({"text": 0.3085, "answer": True})
    
    # adding exclusive answers
    # wrong_z = np.array([x / root])
    # table_value = stats.zscore(wrong_z)
    choices.append({"text": 0.7486, "answer": False, "feedback": "Less than 11 inclusive"})
    choices.append({"text": 0.2514, "answer": False, "feedback": "Less than 11 inclusive"})

    data["params"]["average"] = average
    data["params"]["x"] = x
    data["params"]["choices"] = choices
