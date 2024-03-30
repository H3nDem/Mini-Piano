from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from PIL import Image, ImageTk
from pygame import mixer

WIN_HEIGHT = 684
WIN_WIDTH = 912

class Piano(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        mixer.init()
        mixer.set_num_channels(34) # Number of audio files that can read at the same time, to allow playing several notes together without/with less chance of being interrupted by not producing sound anymore
        self.init_notes('notes')
        self.init_features()
        self.bind_keys()
        self.init_piano_GUI()



        
        
    # Initialize the 88-key piano in the same order as a real piano
    def init_notes(self, path):
        self.piano= {
            'A0': mixer.Sound(path + '/A0.wav'), 'A0#': mixer.Sound(path + '/A0#.wav'),
            'B0': mixer.Sound(path + '/B0.wav'), 'C1': mixer.Sound(path + '/C1.wav'),
            'C1#': mixer.Sound(path + '/C1#.wav'), 'D1': mixer.Sound(path + '/D1.wav'),
            'D1#': mixer.Sound(path + '/D1#.wav'), 'E1': mixer.Sound(path + '/E1.wav'),
            'F1': mixer.Sound(path + '/F1.wav'), 'F1#': mixer.Sound(path + '/F1#.wav'),
            'G1': mixer.Sound(path + '/G1.wav'), 'G1#': mixer.Sound(path + '/G1#.wav'),
            'A1': mixer.Sound(path + '/A1.wav'), 'A1#': mixer.Sound(path + '/A1#.wav'),
            'B1': mixer.Sound(path + '/B1.wav'), 'C2': mixer.Sound(path + '/C2.wav'),
            'C2#': mixer.Sound(path + '/C2#.wav'), 'D2': mixer.Sound(path + '/D2.wav'),
            'D2#': mixer.Sound(path + '/D2#.wav'), 'E2': mixer.Sound(path + '/E2.wav'),
            'F2': mixer.Sound(path + '/F2.wav'), 'F2#': mixer.Sound(path + '/F2#.wav'),
            'G2': mixer.Sound(path + '/G2.wav'), 'G2#': mixer.Sound(path + '/G2#.wav'),
            'A2': mixer.Sound(path + '/A2.wav'), 'A2#': mixer.Sound(path + '/A2#.wav'),
            'B2': mixer.Sound(path + '/B2.wav'), 'C3': mixer.Sound(path + '/C3.wav'),
            'C3#': mixer.Sound(path + '/C3#.wav'), 'D3': mixer.Sound(path + '/D3.wav'),
            'D3#': mixer.Sound(path + '/D3#.wav'), 'E3': mixer.Sound(path + '/E3.wav'),
            'F3': mixer.Sound(path + '/F3.wav'), 'F3#': mixer.Sound(path + '/F3#.wav'),
            'G3': mixer.Sound(path + '/G3.wav'), 'G3#': mixer.Sound(path + '/G3#.wav'),
            'A3': mixer.Sound(path + '/A3.wav'), 'A3#': mixer.Sound(path + '/A3#.wav'),
            'B3': mixer.Sound(path + '/B3.wav'), 'C4': mixer.Sound(path + '/C4.wav'),
            'C4#': mixer.Sound(path + '/C4#.wav'), 'D4': mixer.Sound(path + '/D4.wav'),
            'D4#': mixer.Sound(path + '/D4#.wav'), 'E4': mixer.Sound(path + '/E4.wav'),
            'F4': mixer.Sound(path + '/F4.wav'), 'F4#': mixer.Sound(path + '/F4#.wav'),
            'G4': mixer.Sound(path + '/G4.wav'), 'G4#': mixer.Sound(path + '/G4#.wav'),
            'A4': mixer.Sound(path + '/A4.wav'), 'A4#': mixer.Sound(path + '/A4#.wav'),
            'B4': mixer.Sound(path + '/B4.wav'), 'C5': mixer.Sound(path + '/C5.wav'),
            'C5#': mixer.Sound(path + '/C5#.wav'), 'D5': mixer.Sound(path + '/D5.wav'),
            'D5#': mixer.Sound(path + '/D5#.wav'), 'E5': mixer.Sound(path + '/E5.wav'),
            'F5': mixer.Sound(path + '/F5.wav'), 'F5#': mixer.Sound(path + '/F5#.wav'),
            'G5': mixer.Sound(path + '/G5.wav'), 'G5#': mixer.Sound(path + '/G5#.wav'),
            'A5': mixer.Sound(path + '/A5.wav'), 'A5#': mixer.Sound(path + '/A5#.wav'),
            'B5': mixer.Sound(path + '/B5.wav'), 'C6': mixer.Sound(path + '/C6.wav'),
            'C6#': mixer.Sound(path + '/C6#.wav'), 'D6': mixer.Sound(path + '/D6.wav'),
            'D6#': mixer.Sound(path + '/D6#.wav'), 'E6': mixer.Sound(path + '/E6.wav'),
            'F6': mixer.Sound(path + '/F6.wav'), 'F6#': mixer.Sound(path + '/F6#.wav'),
            'G6': mixer.Sound(path + '/G6.wav'), 'G6#': mixer.Sound(path + '/G6#.wav'),
            'A6': mixer.Sound(path + '/A6.wav'), 'A6#': mixer.Sound(path + '/A6#.wav'),
            'B6': mixer.Sound(path + '/B6.wav'), 'C7': mixer.Sound(path + '/C7.wav'),
            'C7#': mixer.Sound(path + '/C7#.wav'), 'D7': mixer.Sound(path + '/D7.wav'),
            'D7#': mixer.Sound(path + '/D7#.wav'), 'E7': mixer.Sound(path + '/E7.wav'),
            'F7': mixer.Sound(path + '/F7.wav'), 'F7#': mixer.Sound(path + '/F7#.wav'),
            'G7': mixer.Sound(path + '/G7.wav'), 'G7#': mixer.Sound(path + '/G7#.wav'),
            'A7': mixer.Sound(path + '/A7.wav'), 'A7#': mixer.Sound(path + '/A7#.wav'),
            'B7': mixer.Sound(path + '/B7.wav'), 'C8': mixer.Sound(path + '/C8.wav')
        }

        self.notes = [
            'A0', 'A0#', 'B0', 'C1', 'C1#', 'D1', 'D1#', 'E1', 'F1', 'F1#', 'G1',
            'G1#', 'A1', 'A1#', 'B1', 'C2', 'C2#', 'D2', 'D2#', 'E2','F2', 'F2#',
            'G2', 'G2#', 'A2', 'A2#', 'B2', 'C3', 'C3#', 'D3', 'D3#', 'E3', 'F3',
            'F3#', 'G3', 'G3#', 'A3', 'A3#', 'B3', 'C4', 'C4#', 'D4', 'D4#', 'E4',
            'F4', 'F4#', 'G4', 'G4#', 'A4', 'A4#', 'B4', 'C5', 'C5#', 'D5', 'D5#',
            'E5', 'F5', 'F5#', 'G5', 'G5#', 'A5', 'A5#', 'B5', 'C6', 'C6#', 'D6',
            'D6#', 'E6', 'F6', 'F6#', 'G6', 'G6#', 'A6', 'A6#', 'B6', 'C7', 'C7#',
            'D7', 'D7#', 'E7', 'F7', 'F7#', 'G7', 'G7#', 'A7', 'A7#', 'B7', 'C8'
        ]

        self.held_keys = []

    # Initializes the features such as the transpose and the sustain pedal, and some custom by me such as the trace mode  
    def init_features(self):
        self.transpose = 0
        self.sustain = 1000
        self.trace_mode = False

    # Binds command on the keyboard to the piano app
    def bind_keys(self):
        self.keyboard_layout = {
            '<w>': ['C4'],
            '<s>': ['C4#'],
            '<x>': ['D4'],
            '<d>': ['D4#'],
            '<c>': ['E4'],
            '<v>': ['F4'],
            '<g>': ['F4#'],
            '<b>': ['G4'],
            '<h>': ['G4#'],
            '<n>': ['A4'],
            '<j>': ['A4#'],
            '<,>': ['B4'],
            '<;>': ['C5'],
            '<l>': ['C5#'],
            '<:>': ['D5'],
            '<m>': ['D5#'],
            '<!>': ['E5'],
        }
        
        for i in self.keyboard_layout:
            self.bind(i, lambda event, i=i: (self.color_pressed_key(event, self.keyboard_layout[i][1]), self.play_note(event, self.keyboard_layout[i][0])))
            self.bind('<KeyRelease-'+ i[1:len(i)], lambda event, i=i: (self.uncolor_release_key(event, self.keyboard_layout[i][1], self.keyboard_layout[i][0]), self.release_note(event, self.keyboard_layout[i][0])))

        self.bind("<Left>", self.transpose_to_lower_semitone)
        self.bind("<Right>", self.transpose_to_upper_semitone)
        self.bind("<Shift-Left>", self.transpose_to_lower_octave)
        self.bind("<Shift-Right>", self.transpose_to_upper_octave)
        self.bind("<Control-t>", self.enable_disable_trace_mode)
        self.bind("<Control-s>", self.enable_disable_sustain_pedal)

    # Draws the piano and the background on the screen
    def init_piano_GUI(self):
        self.bg = ImageTk.PhotoImage(file='ressources/piano_rig_v2.png')
        self.my_canvas = Canvas(self, width=WIN_WIDTH, height=WIN_HEIGHT)
        self.my_canvas.pack()
        self.my_canvas.create_image(0, 0, image=self.bg, anchor="nw")


        self.piano_frame = Frame(self)
        self.piano_frame.place(x=WIN_WIDTH/9, y=WIN_HEIGHT*0.22-2)
        self.canvas = Canvas(self.piano_frame, bg="gray", width=698, height=498)
        self.canvas.pack()


        self.button_frame = Frame(self)
        self.button_frame.place(x=WIN_WIDTH*0.91, y=WIN_HEIGHT*0.94)
        self.quit_button = Button(self.button_frame, text='Quit', width=8, command=self.quit_app)
        self.quit_button.grid(row=1, column=0)


        whites = self.get_white_keys()
        blacks = self.get_black_keys()
        for i in range(10):
            rect = self.canvas.create_rectangle(i*70,0,(i+1)*70,500,fill='white', outline="black", width=1)
            try:
                key = whites.pop(0)
                self.keyboard_layout[key].append(rect)
            except IndexError:
                continue
            
        for i in [1,3,6,8,10,13,15]:
            rect = self.canvas.create_rectangle(40*i, 0, 40*i +50, 350,fill='black')
            try:
                key = blacks.pop(0)
                self.keyboard_layout[key].append(rect)
            except IndexError:
                continue
            
        self.canvas.update()


        # Transpose value
        self.transpose_value = StringVar()
        self.transpose_value.set("{0}".format(self.transpose))
        self.transpose_text = Label(self, textvariable=self.transpose_value, fg="red", font=("MS Gothic", 35), bg="gray")
        self.transpose_text.place(x=WIN_WIDTH*0.27, y=WIN_HEIGHT*0.06)






    # Plays the corresponding sound when pressing a key
    def play_note(self, event, note):
        if not (note in self.held_keys): # Since tkinter is looping, it prevents the note to be played several times per second while holding it
            note_with_transpose = self.notes[(self.notes.index(note) + self.transpose) % len(self.notes)]
            self.piano[note_with_transpose].play(maxtime=self.sustain)
            self.held_keys.append(note) # We add it in a held key list to prevent playing the note again by holding it
            if (self.trace_mode):
                print("Note pressed: " + note + "\nNote played: " + note_with_transpose + "\n")

    # Release the note so we can play a note again, prevents holding a note playing several times per seconds
    def release_note(self, event, note):
        if (note in self.held_keys):
            self.held_keys.remove(note)

    # Gets all the white keys on the keyboard
    def get_white_keys(self):
        whites = []
        for i in self.keyboard_layout:
            if self.keyboard_layout[i][0][-1] != '#':
                whites.append(i)
        return whites

    # Gets all the black keys on the keyboard
    def get_black_keys(self):
        blacks = []
        for i in self.keyboard_layout:
            if self.keyboard_layout[i][0][-1] == '#':
                blacks.append(i)
        return blacks

    # Colors any key you press, for feedback purposes
    def color_pressed_key(self, event, key):
        self.canvas.itemconfig(key, fill='green')

    # Puts back to the original color any key you release, for feedback
    def uncolor_release_key(self, event, key, color):
        if (color[-1] != '#'):
            self.canvas.itemconfig(key, fill='white')
        else:
            self.canvas.itemconfig(key, fill='black')

    
    """
    TRACE MODE FEATURE
    See a lot of details on the terminal (at the time i'm writing this part of the code)
    """
    def enable_disable_trace_mode(self, event):
        self.trace_mode = not self.trace_mode
        if (self.trace_mode):
            print('Trace mode enabled')
        else:
            print('Trace mode disabled')


    """
    SUSTAIN PEDAL FEATURE
    Consists of emulate a sustaining note as if we keep the feet on the pedal
    """
    def enable_disable_sustain_pedal(self, event):
        if (self.sustain == 1000):
            self.sustain = 6000
            if (self.trace_mode):
                print('Sustain pedal enabled')
        else:
            self.sustain = 1000
            if (self.trace_mode):
                print('Sustain pedal disabled')


    """
    TRANSPOSE FEATURE
    Feature that exists on some digital piano

    Pressing a key will play the note transposeed by X semitones, 0 by default, goes from -12 to +12 (at least on some Yamaha models)
    Explaination: Without transpose (X=0), pressing the A1 key will play the A1 sound (as a normal piano do), however,
                  with a transpose of 1, pressing the A1 key will play the half step upper note of A1, which is A1#
                  with a transpose of 2, pressing the A1 key will play the 2 half steps upper note of A1, which is B1
                  with a transpose of -1, pressing the A1 key will play the half step lower note of A1, which is G1#

    Though as opposed as a real model, there are no limitations whatsoever on the transpose value in this app
    I also impemented an octave transpose, which is playing the note transposeed by 12 half steps, thus, pressing A1 key will play the A2 note
    """
    def transpose_to_lower_semitone(self, event):
        self.transpose -= 1
        if (self.trace_mode):
            print('Transpose downward by one semitone/half step')
        self.transpose_value.set("{0}".format(self.transpose))

    def transpose_to_upper_semitone(self, event):
        self.transpose += 1
        if (self.trace_mode):
            print('Transpose upward by one semitone/half step')
        self.transpose_value.set("{0}".format(self.transpose))

    def transpose_to_lower_octave(self, event):
        self.transpose -= 12
        if (self.trace_mode):
            print('transpose downward by one octave')
        self.transpose_value.set("{0}".format(self.transpose))

    def transpose_to_upper_octave(self, event):
        self.transpose += 12
        if (self.trace_mode):
            print('transpose upward by one octave')
        self.transpose_value.set("{0}".format(self.transpose))

    def quit_app(self):
        if messagebox.askokcancel("Quit", "Close the app ?"):
            self.destroy()


def main():
    app = Piano()
    app.title("Piano")
    app.geometry(str(WIN_WIDTH) + 'x' + str(WIN_HEIGHT))
    app.minsize(WIN_WIDTH, WIN_HEIGHT)
    app.maxsize(WIN_WIDTH, WIN_HEIGHT)
    app.iconphoto(True, PhotoImage(file="ressources/piano_icon.png")) 
    app.protocol("WM_DELETE_WINDOW", app.quit_app)
    app.mainloop()
