import time
import keyboard
from functions_2048 import *

if __name__ == '__main__':

    mat = start_game()
    while (True):
        # taking keyboard input
        printmat(mat)

        try:
            key = keyboard.read_event("Press the command : ")
            if key.event_type == keyboard.KEY_DOWN:
                x = key.name

        except:
            print('Invalid Keyboard Input')
        # move up
        if x == 'w' or x == 'up':
            mat = move_up(mat)
        # move down
        elif x == 's' or x == 'down':
            mat = move_down(mat)
        # move left
        elif x == 'a' or x == 'left':
            mat = move_left(mat)
        # move right
        elif x == 'd' or x == 'right':
            mat = move_right(mat)
        else:
            print('Invalid Keyboard Input')
        # get the current state and print it

        # if game not ove then continue
        # and add a new two
        status = get_current_state(mat)
        if status == 2:
            add_new_2(mat)
            time.sleep(0.5)
        else:
            printmat(mat)
            if status == 1:
                print('You Won')
            elif status == 0:
                print('You Lost')
            try:
                key = keyboard.read_event("Press r to restart OR Press e to End: ")
                if key.event_type == keyboard.KEY_DOWN:
                    x = key.name
            except:
                print('Invalid Keyboard Input')
            if x == 'r':
                print('Restart the Game')
                mat = start_game()
                continue
            elif x == 'e':
                print('Game Over')
                break


