from math import sqrt

def distance(vector1: tuple, vector2: tuple) -> float:
    result = 0
    for i in range(len(vector1)):
        result += (vector1[i] - vector2[i]) ** 2
    result = sqrt(result)
    return result

def cosine(vector1: tuple, vector2: tuple) -> float:
    result = 0
    numerator = 0
    denominator = 0
    for i in range(len(vector1)): 
        numerator += vector1[i] * vector2[i]
    for j in range(len(vector1)): 
        denominator += (vector1[j] * vector1[j])
        
    denominator = sqrt(denominator)
    temp = 0
    for x in range(len(vector2)):
        temp += vector2[x] * vector2[x]
    denominator *= sqrt(temp)
    result = numerator / denominator
    return result


