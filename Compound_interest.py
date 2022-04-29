x,y,z=map(int,input().split())
k=x*pow(1+y/100,z)
print("{:.2f}".format(k))