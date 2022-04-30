def generate(data):

    q1choices = []

#question 1 choices
    q1choices.append({"text": 0.4593, "answer": False, "feedback": "This is wrong"})
    q1choices.append({"text": 0.277, "answer": False, "feedback": "This is wrong"})
    
    q1choices.append({"text": 0.377, "answer": True, "feedback": "Correct!"})
    q1choices.append({"text": 0.225, "answer": False, "feedback": "This is wrong"})

    data["params"]["q1choices"] = q1choices

