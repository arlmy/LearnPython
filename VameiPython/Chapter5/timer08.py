from datetime import datetime

format = "%Y-%m-%d %H:%M %A %a %I %p %f"
t = datetime(2017,1,24,12,50)



print(t.strftime(format))