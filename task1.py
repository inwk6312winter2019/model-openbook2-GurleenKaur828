file=open("Street_Centrelines.csv")
l=[]
def easy(file):
	file.readline()
	for line in file:
		line=line.split(",")
		l.append((line[2],line[4],line[6],line[7]))
easy(file)
print(l)

file=open("Street_Centrelines.csv")
def histogram(s):
	d = dict()
	s.readline()
	for line in s:
		line=line.split(",")
		if line[12]  not in d:
			d[line[12]] = 1
		else:
			d[line[12]] += 1
	return d
print(histogram(file))
