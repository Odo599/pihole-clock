import datetime as dt

def add_time(t,d):
    return (dt.datetime.combine(dt.date(1, 1, 1), t) + d).time()