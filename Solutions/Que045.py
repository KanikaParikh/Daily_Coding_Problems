from random import randint


def rand5():
    return randint(1, 5)


def rand7():
    i = 5 * rand5() + rand5() - 5
    if i < 22:
        return i % 7 + 1
    return rand7()
num_exp = 100000
resultdict = dict()
for _ in range(num_exp):
    n = rand7()
    if n not in resultdict:
        resultdict[n] = 0
    resultdict[n] += 1

desired_prob = 1 / 7
for n in resultdict:
    resultdict[n] = resultdict[n] / num_exp
    print(round(desired_prob, 2))
