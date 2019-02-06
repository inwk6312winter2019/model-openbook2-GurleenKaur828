file=open("Street_Centrelines.csv")
l=[]
def easy(file):
	file.readline()
	for line in file:
		line=line.split(",")
		l.append((line[2],line[4],line[6],line[7]))
easy(file)
print(l)

