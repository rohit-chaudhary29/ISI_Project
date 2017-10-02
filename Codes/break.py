files=open('E.txt',"rb")
file2=open('E_5.txt',"w")
count=0
for line in files:
	if count >=1600 and count <=2000:
		file2.write(line)
	count+=1
