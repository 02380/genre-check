#!venv/bin/python

import argparse
import os
from pprint import pprint
import eyed3

parser = argparse.ArgumentParser()
parser.add_argument("cwd")
args = parser.parse_args()
print(args.cwd)

mp3s = []
songs = []
songs_ok = []
m4as = []

for root, dirs, files in os.walk(args.cwd):
    for filename in files:
        if os.path.splitext(filename)[1] == ".mp3":
        	songs.append(os.path.join(root, filename))
        elif os.path.splitext(filename)[1] == ".m4a":
        	songs.append(os.path.join(root, filename))

# print(songs[110])
# audiofile = eyed3.load(songs[110])
# print(audiofile.tag.genre)

for song in songs:
	audiofile = eyed3.load(song)
	if hasattr(audiofile, 'tag'):
		if hasattr(audiofile.tag, 'genre'):
			print("song good!")
			songs_ok.append(song)

print("{0} songs found - {1} are tagged, {2} are not [{3}%]".format(len(songs),len(songs_ok),len(songs)-len(songs_ok),len(songs_ok)/len(songs)))