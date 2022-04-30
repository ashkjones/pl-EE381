import random, math


def generate(data):

    N = random.randint(9,13)
    total_F = random.randint(4,6)
    total_B = N - total_F
    n = random.randint(4,5)

    total_combo = nCr(N,n)

    # question 1
    first_combo = nCr(total_F,3)
    second_combo = nCr(total_B, n-3)
    answer_q1 = round(first_combo*second_combo/total_combo, 4)
    

    # question 2
    first_combo = nCr(total_F, n-2)
    second_combo = nCr(total_B, 2)
    answer_q2 = round(first_combo*second_combo/total_combo, 4)

    data["params"]["N"] = N
    data["params"]["total_F"] = total_F
    data["params"]["total_B"] = total_B
    data["params"]["n"] = n
    data["correct_answers"]["answer_q1"] = answer_q1
    data["correct_answers"]["answer_q2"] = answer_q2


def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)