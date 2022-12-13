from math import sqrt

def _sorted(scoredict):
    scoredictfunc = list(scoredict)
    for i in range(len(scoredictfunc)-1):
        for j in range(len(scoredictfunc)-i-1):
            if scoredictfunc[j][1] > scoredictfunc[j+1][1]:
                scoredictfunc[j], scoredictfunc[j+1] = scoredictfunc[j+1], scoredictfunc[j]
    return scoredictfunc

def _returnscorelist(scoredict):
    resort = _sorted(scoredict)
    canbeaverage = int(sqrt(len(resort)))
    result = []
    for i in range(canbeaverage):
        result.append(resort[i][0][-1])
    return result

def predict(scoredict, fullscore):
    listscore = _returnscorelist(scoredict)
    # print(listscore)
    average = sum(listscore) / len(listscore)
    # print(average)
    return fullscore / 100 * average