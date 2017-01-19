def gaussian_sum(n):
	if n == 1:
		return 1
	else:
		return n + gaussian_sum(n-1)

print(gaussian_sum(100))