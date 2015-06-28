#!/bin/python
import sys
import musixmatch
import random
import nltk
sys.path.append('/usr/local/lib/python.2.7/site-packages')

from musixmatch.lyrics import Lyrics

musixmatch_wslocation = 'http://api.musixmatch.com/ws/1.1'
musixmatch_apikey = '77a751b9e63dedb74abbce23aa667c34'

#track.search
# https://github.com/monkeython/musixmatch/tree/master/musixmatch
# https://developer.musixmatch.com/documentation/input-parameters
#track.lyrics.get?track_id=15953433

#rand_id = random.randrange(99999999)
songid = 17459676

try:
	slyrics = musixmatch.ws.track.lyrics.get(track_id=songid, country='us', apikey=musixmatch_apikey)
except musixmatch.api.Error, e:
	pass

text = slyrics['body']['lyrics']['lyrics_body']

print "LYRICS"
print "======"
print text
print ""

text = nltk.word_tokenize(text)
print nltk.pos_tag(text)

