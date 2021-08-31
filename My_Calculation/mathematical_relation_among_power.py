#  Copyright 2021 Mahid   e-mahid@outlook.com
#  I found a replationship among power when I was a college student.
#  I do not know the importance of this. But theres an interesting pattern. Factorial

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY


def relation(p=2):
	x=[i**p for i in range(1,p+2)]
	print(x)
	n=[]
	for i in range(p):
		for j in range(len(x)-1):
			a=abs(x[j]-x[j+1])
			n.append(a)
		x=n
		print(x)
		n=[]
relation(2)
relation(3)
relation(4)
relation(5)
relation(6)
relation(7)
