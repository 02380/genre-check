#!venv/bin/python

import argparse
import os
import time
import math
from pprint import pprint
import eyed3

eyed3.log.setLevel("ERROR")
parser = argparse.ArgumentParser()
parser.add_argument("cwd")
args = parser.parse_args()
print("genre-checker: scanning {0}".format(args.cwd))

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

for song in songs:
	audiofile = eyed3.load(song)
	if hasattr(audiofile, 'tag'):
		if hasattr(audiofile.tag, 'genre'):
			songs_ok.append(song)
	time.sleep(0.01)

print("{0} songs found - {1} are tagged, {2} are not [{3}%]".format(len(songs),len(songs_ok),len(songs)-len(songs_ok),round((len(songs_ok)/len(songs))*100,2)))