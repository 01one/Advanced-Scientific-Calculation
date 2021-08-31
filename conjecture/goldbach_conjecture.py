#  Copyright 2021 Mahid e-mahid@outlook.com
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY


"""Goldbach’s conjecture
Any even number can be written as a sum of two primes."""

x=eval(input("Enter an even number: "))
prime=[]

for i in range(2,x+1):
	for j in range(2,i):
		if i%j==0:
			break
	else:
		prime.append(i)
		
y=len(prime)

l=[]

for i in range(y):
	for j in range(i+1):
		a=prime[i]
		b=prime[j]
		k=a+b
		if k==x:
			l.append([a,b])
print(l)
