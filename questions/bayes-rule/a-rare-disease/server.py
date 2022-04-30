import random, math

def generate(data):

    accurate = random.randint(90,98)
    false = random.randint(4,6)
    pos_d = accurate/100.0
    pos_nd = false/100.0
    p_d = 0.001
    p_nd = 0.999

    p_pos = p_d * pos_d + p_nd * pos_nd
    p_d_and_pos = p_d * pos_d
    p_d_g_pos = round(p_d_and_pos / p_pos, 4)

    data["params"]["accurate"] = accurate
    data["params"]["false"] = false
    data["correct_answers"]["answer"] = p_d_g_pos
    

