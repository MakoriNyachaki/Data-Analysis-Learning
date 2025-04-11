def move(f, t):
	print("Move object from {} to {}!".format(f, t))


def moveVia(f, v, t):
	move(f, v)
	move(v, t)


def main():
	moveVia("A", "C", "D")

main()
