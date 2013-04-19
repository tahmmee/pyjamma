from lib.pyjama import Note, Measure, Song
from lib.notes import *

m1 = Measure([
               Note(G3, 2.3, 4.4, 28),
               Note(G5, 3.1, 3.4, 32),
               Note(C4, 1.1, 1.3, 43), Note(C4, 3.1, 3.4, 34), Note(C4, 4.3, 6.3, 40),
               Note(G4, 1.1, 3, 48),  Note(G4, 2.3, 3.1, 42), Note(G4, 3.3, 4.2, 30), Note(G4, 4.3, 6.2, 41),
               Note(D5_,1.1, 3, 58),
               Note(D5, 3.1, 3.4, 62),  Note(D5, 4.1, 6.2, 30),
            ])

m2 = Measure([
               Note(F5, 1.1, 1.4, 78), Note(F5, 2.1, 2.3, 63), Note(F5, 2.4, 3.1, 26),
               Note(G4, 1.3, 2.1, 39), Note(G4, 2.3, 3.1, 40), Note(G4, 3.3, 4.2, 30), Note(G4, 4.3, 6.0, 35),
               Note(D5_,3.1, 3.3, 39), Note(D5_, 4.1, 4.3, 48),
               Note(C4, 2.3, 4.2, 35), Note(C4, 4.3, 4.4, 35)
            ])

song = Song([m1,m2], 80, "emopiano")
song.play()
