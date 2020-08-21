import sys
l=[]#List for storing songs
for line in sys.stdin:#Read input from mapper
	(name, points)=line.strip().split(",")
	l.append((name,points))

for song in l:#Print all songs, and their start and end points for the preview
	print (song)