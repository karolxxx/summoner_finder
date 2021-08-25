import os 
import sys
import time

class System:
        def __init__(self,):
            pass
            
        def restart_program(self): 
            print('Program resetting')
            time.sleep(0.8)
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system("python main.py")

        def exit_app(self):
            sys.exit()

        def clear_terminal(self):
            time.sleep(0.1)
            os.system('cls' if os.name == 'nt' else 'clear')

        def pause(self):
            time.sleep(0.1)
            os.system("PAUSE")
