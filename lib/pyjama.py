import rtmidi
import time
import threading

midiout = rtmidi.MidiOut(0)

class Note(threading.Thread):

    CHANNEL = 0x9a # grandpiano

    def __init__(self, note, start = 1, end = None, velocity = 112, channel = CHANNEL):
        threading.Thread.__init__(self)
        self.note = note
        self.start_b = start 
        self.end_b = end or start + 0.2
        self.velocity = velocity 
        self.channel = channel
        self.bps = None

    def run(self):

        # play
        msg = [self.channel, self.note, self.velocity]
        midiout.send_message(msg)


        # sustain
        sustain = (self.end_b - self.start_b) * self.bps
        if sustain > 0:
            time.sleep(sustain)

        # off
        midiout.send_message([self.channel, self.note, 0])


class Measure(object):
    def __init__(self, notes):
        self.ticks = [1, 1.1, 1.2, 1.3,
                      2, 2.1, 2.2, 2.3,
                      3, 3.1, 3.2, 3.3,
                      4, 4.1, 4.2, 4.3]

        self.notes = notes

    def play(self, bps):

        for tick in self.ticks:
            # play notes at this tick
            notes = self.get_notes(tick)
            self.play_notes(notes, bps)

            # sleep till next tick
            time.sleep(bps/4.0)

    def get_notes(self, tick):
        return [note for note in self.notes if note.start_b == tick]

    def play_notes(self, notes, bps):
        for note in notes:
            note.bps = bps
            note.start()



class Song(object):

    def __init__(self, measures, tempo = 120, name = "mysong"):
        self.measures = measures
        self.tempo = tempo
        self.name = name
        self.bps = 60/float(self.tempo)

        # create virtual midi out
        midiout.open_virtual_port(self.name)

    def play(self):
        for measure in self.measures:
            measure.play(self.bps)
