from math import sqrt
n=int(input())
cox={}
coy={}
coz={}
count=0
for i in range(0,n):
    z1=input()
    z=list(map(int,z1.split()))
    cox[z[0]]=cox.get(z[0],0)+1
    coy[z[1]]=coy.get(z[1],0)+1
    coz[z1]=coz.get(z1,0)+1
x=cox.values()
y=coy.values()
z=coz.values()
for a in x:
    count+=(a*(a-1))/2
for b in y:
    count+=(b*(b-1))/2
for c in z:
    count-=(c*(c-1))/2
print(int(count))

