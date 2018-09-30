train = open('airsim_rec.txt','r')
for line in train:
	fields = line.split("; ")
	x = float(fields[1])
	y = float(fields[2])
	z = float(fields[3])
	print (x,y,z)