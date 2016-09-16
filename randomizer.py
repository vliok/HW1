import random

def randomizer():
    file = open("occupations.csv","r")
    next(file)
    d = {}
    for line in file:
        if "\"" in line:
            line = line[1:]
            list = line.split("\",")
        else:
            list = line.split(",")
        d[ list[0] ] = float( list[1] )
    d.pop("Total")
    bound = 0.0
    randNum = random.random() * 99.8
    for job in d:
        bound += d[job]
        if randNum < bound:
            return job

print randomizer()
