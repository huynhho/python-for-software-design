class Time:
    pass

time = Time()
time.hours = 11
time.minutes = 59
time.seconds =30
def addTime(t1, t2):
    sum = Time()
    sum.hours = t1.hours + t2.hours
    sum.minutes =t1.minutes + t2.minutes
    sum.seconds = t1.seconds + t2.seconds
    return sum
