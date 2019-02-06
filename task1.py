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
def histogram(file):
	d = dict()
	file.readline()
	for line in file:
		line=line.split(",")
		if line[12]  not in d:
			d[line[12]] = 1
		else:
			d[line[12]] += 1
	return d
print(histogram(file))

file=open("Street_Centrelines.csv")
def own(file):
	s=set()
	file.readline()
	for line in file:
		line=line.split(",")
		s.add(line[11])
	return s
print(own(file))

