def fac(n):
	if n <= 0:
		return 1
	else:
		return n * fac(n - 1)

def main():
	n = int(input("Enter a number to find a factorial: "))
	print(fac(n))


main()
