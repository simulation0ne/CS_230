"""
    Developer: Daniel Peach
    Project: GUI for a Rectangle builder
             It will display width, height, perimeter, and area
"""

# make tkinter work with python 2 and 3
try:
    from tkinter import *
    from tkinter import messagebox
except ImportError:
    from Tkinter import *
    import tkMessageBox as messagebox

# ========================================================================== #

# Globals
width = 0
height = 0
win_w = 0
win_h = 0
try:
    sorry = "Sorry"
except SyntaxError:
    sorry = "Sorry"

# SyntaxError: Non-ASCII character '\xc2' in file main_gui.py on line 26,
# but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details

# Fonts
header_font = ("Courier", "24")
measure_font = ("Arial", "14")
label_font = ("Arial", "20")

# ========================================================================== #


# Main menu screen
class mainMenu(object):

    def make_rec(self):
        global width, height
        cont = False
        if self.width_e.get().isdigit() and self.height_e.get().isdigit():
            width = int(self.width_e.get())
            height = int(self.height_e.get())
            if width > win_w or height > win_h:
                answer = messagebox.askyesno(title="Rectangle Overflow",
                                             message="Your rectangle will be larger than your window, is this ok?")
                if answer:
                    messagebox.showwarning(title="Program Problems",
                                           message="You may experience issues with the size of your rectangle."
                                                   "You may have to re-run the program.\n{}".format(sorry))
                    cont = True
            else:
                cont = True
        if cont:
            switch_frame(1)
        else:
            self.width_e.delete(0, 'end')
            self.height_e.delete(0, 'end')


    def __init__(self, master):

        # Main Frame
        self.frame = Frame(master, bg="dodgerblue2")
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.build_window()

    def build_window(self):

        # Top Header
        self.header = Label(self.frame, text="Rectangle Builder", bg="grey", font=header_font)
        self.header.grid(row=0, column=0, columnspan=3, sticky="ew")

        # Entries for the dimensions
        self.width_e = Entry(self.frame, highlightbackground="dodgerblue2")
        self.width_e.grid(row=2, column=0, sticky="ne")
        self.height_e = Entry(self.frame, highlightbackground="dodgerblue2")
        self.height_e.grid(row=2, column=2, sticky="nw")

        # Labels for entries
        self.width_l = Label(self.frame, text="Width", fg="white", bg="dodgerblue2", font=label_font)
        self.width_l.grid(row=1, column=0, sticky="se")
        self.width_l = Label(self.frame, text="Height", fg="white", bg="dodgerblue2", font=label_font)
        self.width_l.grid(row=1, column=2, sticky="sw")

        # Creation Button
        self.create_b = Button(self.frame, text="Create Rectangle", highlightbackground="dodgerblue2", command=self.make_rec)
        self.create_b.grid(row=3, column=1, sticky="n")



class showRectangle(object):
    def __init__(self, master):
        # Main Frame
        self.frame = Frame(master, bg="dodgerblue2")
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.build_window()

    def build_window(self):

        global rec_fh, rec_fw

        # Top Header
        self.header = Label(self.frame, text="Here is your Rectangle!", bg="grey", font=header_font)
        self.header.grid(row=0, column=0, columnspan=4, sticky="ew")

        # Dimensions label frame
        self.dimensions = LabelFrame(self.frame, text="Dimensions")
        self.dimensions.grid(row=1, column=0, columnspan=4, sticky="ew")
        self.dimensions.columnconfigure(0, weight=1)
        self.dimensions.columnconfigure(1, weight=1)
        self.dimensions.columnconfigure(2, weight=1)
        self.dimensions.columnconfigure(3, weight=1)

        # Dimensions labels
        self.width_l = Label(self.dimensions, text="width: {}".format(width))
        self.width_l.grid(row=0, column=0)
        self.width_l = Label(self.dimensions, text="height: {}".format(height))
        self.width_l.grid(row=0, column=1)
        self.width_l = Label(self.dimensions, text="perimeter: {}".format(((width * 2) + (height * 2))))
        self.width_l.grid(row=0, column=2)
        self.width_l = Label(self.dimensions, text="area: {}".format((width * height)))
        self.width_l.grid(row=0, column=3)

        # Frame for the rectangle
        self.rec_frame = Frame(self.frame, bg="dodgerblue2")
        self.rec_frame.grid(row=2, column=0, columnspan=4, sticky="nsew")
        self.rec_frame.update()

        # Getting the size of the rectangle frame for padding later
        rec_fw = self.rec_frame.winfo_width()
        rec_fh = self.rec_frame.winfo_height()

        # The actual rectangle
        self.rectangle = Canvas(self.rec_frame, width=width, height=height, bg="green", highlightthickness=0)
        self.rectangle.grid(row=0, column=0, padx=self.get_rec_padx(rec_fw), pady=self.get_rec_pady(rec_fh))

        # New Rectangle Button
        self.new_rect_btn = Button(self.rec_frame, text="New Rectangle", highlightbackground="dodgerblue2", command=lambda: switch_frame(0))
        self.new_rect_btn.grid(row=0, column=0, sticky="s")

    @staticmethod
    def get_rec_padx(w):
        if width > w:
            return 0
        else:
            return (w - width) / 2
    @staticmethod
    def get_rec_pady(h):
        if height > h:
            return 0
        else:
            return (h - height) / 2

# ========================================================================== #

# Function to switch screens
def switch_frame(new_frame):

    if new_frame == 0:
        mainMenu(root)
    if new_frame == 1:
        showRectangle(root)


if __name__ == '__main__':
    root = Tk()
    root.title("PyShapes")
    mon_w = root.winfo_screenwidth()
    mon_h = root.winfo_screenheight()
    win_w = mon_w / 2
    win_h = mon_h / 2
    win_size = "{}x{}".format(int(win_w), int(win_h))
    win_pad = "{}+{}".format(int(win_w / 2), int(win_h / 6))
    win_pos = "{}+{}".format(win_size, win_pad)
    root.geometry(win_pos)
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)
    switch_frame(0)
    root.mainloop()