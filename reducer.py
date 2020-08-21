import sys
artists={}#dictionary for storing the songs of each artist
for line in sys.stdin:#Read input from mapper
	name, points=line.strip().split(",")
	if name in artists:
		artists[name].append(points)
	else
		artists[name]=[points]

for artist in artists:#Print all songs, and their start and end points for the preview
	print (artist, artists[artist])
