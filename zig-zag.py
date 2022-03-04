import time, sys

indent = 0 #for setting the number of spaces
indentInc = True #for specifying if the indent should increase or not

try:
    while True: #running an infinite loop until interrupted
        print(' ' * indent, end='')
        print('*****')
        time.sleep(0.1) #sleep for 1/10th of a second for the pattern to be visible
        
        if indentInc: #if indentInc is true, increase the indent
            indent += 1
            if indent == 10:
                indentInc = False
        else: #if indentInc if false, decrease the indent
            indent -= 1
            if indent == 0:
                indentInc = True

except KeyboardInterrupt: #exit the program on KeyboardInterrupt
    sys.exit() #this handles the KeyboardInterrupt error cleanly

