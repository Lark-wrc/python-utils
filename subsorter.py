import os, sys

#make this a variable at... somepoint.
os.chdir("/home/bill/Downloads")

folders = []
files = []

for x in os.listdir('.'):
	if os.path.isdir(x):
		folders.append(x)
	else:
		files.append(x)


for f in files:
	matches = []

	s = f[0:-4].split()
	for x in folders:
		matchtick = 0
		z = x.lower().split()
		if z[0][0] == '@':
			z[0] = z[0][1:]
		for i in s:
			if i.lower() in z:
				matchtick+=1
		matches.append(matchtick)

	mostmatched = max(matches)
	if mostmatched > 1:
		index = matches.index(mostmatched)
		print f, ' to ', folders[index]
		os.rename(f, folders[index]+"/"+f)

print 'Mission Complete~'
print 'Sayonara~'