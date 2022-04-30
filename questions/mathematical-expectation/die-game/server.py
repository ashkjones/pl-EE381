import random
import math
import numpy as np
import scipy.stats as stats

def generate(data):
    choices = []
    average = 9
    x = 11

    #selections available with correct answer
    choices.append({"text": "\$7", "answer": False, "feedback": "Incorrect"})
    choices.append({"text": "\$10", "answer": False, "feedback": "Incorrect"})
    choices.append({"text": "\$5", "answer": True, "feedback": "Correct! It follows that the player can expect to win \$5. In a fair game, therefore, the player should be expected to pay \$5 in order to play the game."})
    choices.append({"text": "\$3", "answer": False, "feedback": "Incorrect"})

    data["params"]["average"] = average
    data["params"]["x"] = x
    data["params"]["choices"] = choices
