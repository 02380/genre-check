from tinytag import TinyTag
import argparse
import os
import time
import math
from pprint import pprint
import progressbar


no_info_doc = "LOG\n\n"

def log_bad_song(s):
	return str('NO INFO: {0}\n'.format(s))

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

with progressbar.ProgressBar(max_value=len(songs)) as bar:
	for i, song in enumerate(songs):
		audiofile = TinyTag.get(song)
		# audiofile = eyed3.load(song)
		# if hasattr(audiofile, 'tag'):
		# 	if hasattr(audiofile.tag, 'genre'):
		# 		songs_ok.append(song)
		# 	else:
		# 		log_bad_song(song)
		# else:
		# 	log_bad_song(song)
		log_bad_song(audiofile.genre)
		if hasattr(audiofile, 'genre'):
			if audiofile.genre == 'None' or audiofile.genre == None or audiofile.genre == '':
				no_info_doc += log_bad_song(song)
			else:	
				songs_ok.append(song)
		else:
			log_bad_song(song)
		time.sleep(0.01)
		bar.update(i)


with open('log.txt', 'w', encoding='utf-8') as the_file:
    the_file.write(no_info_doc)
print("{0} songs found - {1} are tagged, {2} are not [{3}%]".format(len(songs),len(songs_ok),len(songs)-len(songs_ok),round((len(songs_ok)/len(songs))*100,2)))