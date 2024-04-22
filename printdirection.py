def drawUp(len):
	drawLayer(1, len + 1, 1, len)

def drawDown(len):
	drawLayer(len, 0, -1, len)

def drawRight(len):
	drawLine(0, len, 1)
	drawLine(len - 2, -1, -1)

def drawLeft(len):
	drawLine(len - 1, 0, -1)
	drawLine(0, len, 1)
	
def drawLayer(start, end, step, len):
	for i in range(start, end, step):
		spacing = len - i
		word = (spacing * " ") + ("* ") * i + (spacing * " ")
		print(word[:-1])
		
def drawLine(start, end, step):
	for i in range(start, end, step):
		print(i * " " + "*")

def printArrow(dir, len):
	
	if not isinstance(len, int) or len < 1:
		print("Must enter a positive integer length")
		return
	
	if dir == "up":
		drawUp(len)
	elif dir == "down":
		drawDown(len)
	elif dir == "right":
		drawRight(len)
	elif dir == "left":
		drawLeft(len)

if __name__ == '__main__':
	printArrow("up", 4)
	print()
	print("--------------")
	print()
	printArrow("up", 4.0)
	print()
	print("--------------")
	print()
	printArrow("down", 5)
	print()
	print("--------------")
	print()
	printArrow("right", 3)
	print()
	print("--------------")
	print()
	printArrow("left", 6)