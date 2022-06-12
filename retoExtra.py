from math import factorial,log2,floor
def bell(n):
	if n==0:
		return 1
	elif n>0:
		arreglo=[1]*(n+1)
		for y in range(1,n+1):
			for k in range(1,y):
				arreglo[y]+=(factorial(y-1)/(factorial(k)*factorial(y-1-k)))*arreglo[k]
		return arreglo[len(arreglo)-1]
def fibonacci(n):
	a,b=0,1
	if n==0:
	    b=0
	else:
		for k in range(n-1):
			b=b+a
			a=b-a
	return b
def evil(n):
	print(fibonacci(floor(log2(bell(n+1)))+1))
evil(int(input("N: ")))
