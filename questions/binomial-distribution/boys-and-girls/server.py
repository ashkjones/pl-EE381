def generate(data):

    q1choices = []
    q2choices = []
    q3choices = []

#question 1 choices
    q1choices.append({"text": 200, "answer": False, "feedback": "This is the probability there is less than 11."})
    q1choices.append({"text": 250, "answer": True, "feedback": "Correct!"})
    
    q1choices.append({"text": 300, "answer": False, "feedback": "Less than 11 inclusive."})
    q1choices.append({"text": 225, "answer": False, "feedback": "Less than 11 inclusive."})

# #question 2 choices
    q2choices.append({"text": 25, "answer": True, "feedback": "This is the probability there is less than 11."})
    q2choices.append({"text": 20, "answer": False, "feedback": "Correct!"})
    
    q2choices.append({"text": 30, "answer": False, "feedback": "Less than 11 inclusive."})
    q2choices.append({"text": 22, "answer": False, "feedback": "Less than 11 inclusive."})

# #question 3 choices
    q3choices.append({"text": 400, "answer": False, "feedback": "This is the probability there is less than 11."})
    q3choices.append({"text": 250, "answer": False, "feedback": "Correct!"})
    
    q3choices.append({"text": 300, "answer": False, "feedback": "Less than 11 inclusive."})
    q3choices.append({"text": 500, "answer": True, "feedback": "Less than 11 inclusive."})

    data["params"]["q1choices"] = q1choices
    data["params"]["q2choices"] = q2choices
    data["params"]["q3choices"] = q3choices

