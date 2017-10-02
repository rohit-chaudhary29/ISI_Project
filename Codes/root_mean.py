import math
files=open('Root_mean',"rb")

count=0
val = [0.091423940590147218,
0.071034658943409537,
0.068074454160558198,
0.075314424104563599,
0.081185494600876304]

print val
sum=0.0
for i in range(0,5):
	sum+=((1-val[i])*(1-val[i]))
sum=sum/5.0
#print sum
print math.sqrt(sum)
