def getSubjectStats(subject, weights):
    return [[elt[0], elt[1], avg(elt[1], weights)]
            for elt in subject]

def dotProduct(a, b):
    result = 0.0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

def avg(grades, weights):
    try:
        return dotProduct(grades, weights) / len(grades)
    except ZeroDivisionError:
        print 'no grades data'
        return 0.0
    except TypeError:
        newgr = [convertLetterGrade(elt) for elt in grades]
        return dotProduct(newgr, weights) / len(newgr)

def convertLetterGrade(grade):
    if type(grade) == int:
        return grade
    elif grade == 'A':
        return 90.0
    elif grade == 'B':
        return 80.0
    elif grade == 'C':
        return 70.0
    elif grade == 'D':
        return 60.0
    else:
        return 50.0

test = [[['fred', 'flinstones'], [10.0, 5.0, 85.0]],
        [['barney', 'rubble'], [10.0, 8.0, 74.0]],
        [['wilma', 'flintstone'], [8.0, 10.0, 96.0]],
        [['dino'], []]]

weights = [0.3, 0.2, 0.5]

weights1 = [0.15, 0.1, 0.25, 0.25]

test1 = [[['fred', 'flintstone'], [10.0, 5.0, 85.0, 'D']],
         [['barney', 'rubble'], [10.0, 8.0, 74.0, 'B']],
         [['wilma', 'flintstone'], [8.0, 10.0, 96.0, 'A']],
         [['dino'], []]]

test2 = [[['fred', 'flintstone'], [10.0, 5.0, 8500, 'D']],
         [['barney', 'rubble'], [10.0, 8.0, 74.0, 'B']],
         [['wilma', 'flintstone'], [8.0, 10.0, 96.0, 'A']]]
