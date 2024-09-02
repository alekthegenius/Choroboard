import mido
import sys
from pychord import find_chords_from_notes
import keyboard

print(mido.get_input_names())

note_dict = {
    0: "C",
    1: "C#",
    2: "D",
    3: "D#",
    4: "E",
    5: "F",
    6: "F#",
    7: "G",
    8: "G#",
    9: "A",
    10: "A#",
    11: "B"}


current_notes = []
session_notes = []
session_note_values = []



try:
    while True:
        with mido.open_input("KL Essential 61 mk3 MIDI") as inport:

            for msg in inport:
                note = {note_dict[(msg.note)%12]: (msg.note-24)//12}
                note_value = msg.note

                if msg.type == "note_on":
                    current_notes.append(note)
                    if note not in session_notes:
                        session_notes.append(note)
                        session_note_values.append(note_value)

                if msg.type == "note_off":

                    current_notes.remove(note)


                if current_notes == []:
                    session_notes.sort(key=lambda x: list(x.values())[0])
                    session_notes.sort(key=lambda x: list(x.keys())[0])

                    if len(session_notes) == 2:
                        if session_notes[0] != session_notes[1]:
                                number = session_note_values[0] - session_note_values[1]
                                print("Number: ", number)
                                
                    elif len(session_notes) == 3:

                        print("Current notes: ", session_notes)

                        note_list = []
                        for note in session_notes:
                            note_list.append(list(note.keys())[0])
                        
                        print("Chords: ", find_chords_from_notes(note_list))

                    elif len(session_notes) == 4:
                        print("Current notes: ", session_notes)

                        note_list = []
                        for note in session_notes[:1]:
                            note_list.append(list(note.keys())[0])

                        over_note = list(session_notes[0].keys())[0]

                        print("Chords: ", find_chords_from_notes(note_list), "/", over_note)

                        
                    
                    session_notes = []

                
                

except KeyboardInterrupt:
    sys.exit(0)


