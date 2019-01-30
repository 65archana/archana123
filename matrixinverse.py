a=[[1,1],[1,1]]
b=[[1,1],[1,1]]
m=len(a)
for i in range(m):
	for j in range(len(a[0])):
		a[i][j]=input("enter elements in your matrix")
print "MATRIX:",a

s=((a[0][0]*a[1][1])-(a[0][1]*a[1][0]))
t=float(1)/float(s)
m=len(b)
for i in range(m):
	for j in range(len(b[0])):
		b[0][0]=a[1][1]*t
		b[0][1]=-a[0][1]*t
		b[1][0]=-a[1][0]*t
		b[1][1]=a[0][0]*t
print "inverse of the MATRIX:",b


