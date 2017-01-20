from datetime import datetime 

str = "output-1997-1-23-030000.txt"

format = "output-%Y-%m-%d-%H%M%S.txt"

t = datetime.strptime(str, format)

print(t)