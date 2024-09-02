import mido
import sys
from pychord import find_chords_from_notes
import keyboard

print(mido.get_input_names())




def main():
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


    char_dict = {
        'A': 'A',
        'B': 'B',
        'C': 'C',
        'D': 'D',
        'E': 'E',
        'F': 'F',
        'G': 'G',
        'Am': 'H',
        'Bm': 'I',
        'Cm': 'J',
        'Dm': 'K',
        'Em': 'L',
        'Fm': 'M',
        'Gm': 'N',
        'A7': 'O',
        'B7': 'P',
        'C7': 'Q',
        'D7': 'R',
        'E7': 'S',
        'F7': 'T',
        'G7': 'U',
        'Asus2': 'V',
        'Bsus2': 'W',
        'Csus2': 'X',
        'Dsus2': 'Y',
        'Esus2': 'Z'
    }

    current_notes = []
    session_notes = []
    session_note_values = []


    with mido.open_input("KL Essential 61 mk3 MIDI") as inport:
            while True:

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
                        session_note_values.sort()

                        if len(session_notes) == 2:
                            if session_notes[0] != session_notes[1]:
                                    number = session_note_values[1] - session_note_values[0]
                                    print("Number: ", number)
 

                                    keyboard.write(f"{number}")
                                    
                        elif len(session_notes) == 3:

                            print("Current notes: ", session_notes)

                            note_list = []
                            for note in session_notes:
                                note_list.append(list(note.keys())[0])
                            
                            chord = str(find_chords_from_notes(note_list)[0])

                            chord.replace("[<Chord: ", "").replace(" >]", "")

                            print("Chord: ", chord) 

                            if chord in list(char_dict.keys()):
                                char = char_dict[chord]

                                keyboard.write(char)
                        else:
                            pass

                            
                        
                        session_notes = []
                        session_note_values = []

if __name__ == "__main__":
     try:
         main()
     except KeyboardInterrupt:
         sys.exit(0)


