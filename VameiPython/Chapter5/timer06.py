import datetime

t = datetime.datetime(2017,1,20,13,23)
t_next = datetime.datetime(2010,1,24,21,20)

delta1 = datetime.timedelta(seconds = 800)
delta2 = datetime.timedelta(weeks = 3)

print(t + delta1)
print(t + delta2)
print(t_next - t)