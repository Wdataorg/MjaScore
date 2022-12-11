class ErrorOfInformation(Exception):
    def __init__(self, message):
        super().__init__(message)

ERRORSTR = 'Input message is error'

def _percentscore(score, fullscore):
    result = score / fullscore * 100
    return result

def _valuelistone(value):
    if value == 'Easy':
        return 1
    
    elif value == 'Normal':
        return 2
    
    elif value == 'Hard':
        return 3
    
    else:
        raise ErrorOfInformation(ERRORSTR)

def _valuelisttwo(value):
    if value == 'Have reviewed':
        return 1
    
    elif value == "Haven't reviewed":
        return 2

    else:
        raise ErrorOfInformation(ERRORSTR)

def _valuelistthree(value):
    if value == 'Mid/Final Exam':
        return 1
    
    elif value == 'Test':
        return 2
    
    elif value == 'Large scale examination':
        return 3
    
    else:
        raise ErrorOfInformation(ERRORSTR)

def _valuelistfour(value):
    if value == 'Very good':
        return 1
    
    elif value == 'Good':
        return 2
    
    elif value == 'Normal':
        return 3
    
    elif value == 'Bad':
        return 4
    
    elif value == 'Very bad':
        return 5
    
    else:
        raise ErrorOfInformation(ERRORSTR)

def _valuelistfive(value):
    if value == 'Yes':
        return 1
    
    elif value == 'No':
        return 2
    
    else:
        raise ErrorOfInformation(ERRORSTR)

def geninformation(valuelist):
    result = []
    if len(valuelist) == 7:
        result.append(_valuelistone(valuelist[0]))
        result.append(_valuelisttwo(valuelist[1]))
        result.append(_valuelistthree(valuelist[2]))
        result.append(_valuelistfour(valuelist[3]))
        result.append(_valuelistfive(valuelist[4]))
        result.append(_percentscore(valuelist[-2], valuelist[-1]))
        return result