try:
	m = 1/0
except ZeroDivisionError as e:
	print("Catch NameError in the sub-function")

print(type(e))
print(dir(e))
print(e.message)