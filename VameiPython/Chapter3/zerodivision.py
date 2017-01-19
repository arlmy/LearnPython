while True:
	inputStr = input("Please input a number:") #等待输入
	try:
		num = float(inputStr)
		print("Input number:", num)
		print("result:", 10/num)
	except ValueError:
		print("Illegal input. Try Again.")
	except ZeroDivisionError:
		print("Illegal devision by zero. Try Again.")
	finally:
	    exit()