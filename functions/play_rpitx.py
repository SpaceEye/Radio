import os
def play_music(filename):
    path = "sudo ~/rpitx/pifmrds -freq 98.5 -audio " + str(filename) + " & ^C"
    print(path)
    os.system(path)

