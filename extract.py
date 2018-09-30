import sys

f = open("coordinates.txt",'w')
images = sys.argv[1]
gps = sys.argv[2]

images_path = []
with open(images) as file:
	for line in file:
		line = line.strip()
		line = line[2:]
		images_path.append(line)

# print(len(images_path))
x = []
y = []
z = []
image_add = []
with open (gps) as file:
	for line in file:
		line = line.strip()
		arr = line.split()
		x.append(arr[1])
		y.append(arr[2])
		z.append(arr[3])
		image_add.append(arr[8])
for i in images_path[1:]:
	if i in image_add:
		idx = images_path.index(i)
		f.write("%s %s %s\n" % (x[idx],y[idx],z[idx]))
f.close()