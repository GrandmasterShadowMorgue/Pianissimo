from music21 import *

MozRon = converter.parse('Music/Rondo Alla Turca.mxl')

melody = MozRon.parts[0].measures(0,4)

def getPitches(piece):
	#Returns a list of all the pitches in a piece in sequence.
	return [str(pitch) for p in piece.pitches]


sp = midi.realtime.StreamPlayer(MozRon)
sp.play()
	