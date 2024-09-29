import os
import ctypes
import win32gui, win32con
import json
from pystyle import *
from colorama import *
import re

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

def set_fullscreen():
    kernel32 = ctypes.windll.kernel32
    user32 = ctypes.windll.user32
    console_window = kernel32.GetConsoleWindow()
    user32.ShowWindow(console_window, 3)
    user32.SetWindowPos(console_window, 0, 0, 0, 0, 1)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

universe_watermark = """                                 
                                            ++++++*                             
                                      ++++++++++++++@@                           
                                        @@#++++++++++@@@                         
                                        @@@@*+++++++++@@@                        
                                           #++++++++++@@@@                       
                                         *++++++++++++@@@@                        
                                       +++++++++++++++@@@@                        
                                    ****++++++++++++++#@@@                        
                                  #******+++++++++++++%@@@                        
                                ***********+++++++++++@@@@                        
                              **************+++++++++@@@@@                        
                           ******************+++++++%@@@@             ██████╗  █████╗ ██╗   ██╗███████╗███╗   ██╗     ██████╗ █████╗ ██╗      ██████╗           
                        #**********************++++%@@@@@             ██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║    ██╔════╝██╔══██╗██║     ██╔════╝
                     %###***********************++@@@@@@              ██████╔╝███████║██║   ██║█████╗  ██╔██╗ ██║    ██║     ███████║██║     ██║ 
                  #########**********************@@@@@@               ██╔══██╗██╔══██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║    ██║     ██╔══██║██║     ██║                
                ############*******************@@@@@@                 ██║  ██║██║  ██║ ╚████╔╝ ███████╗██║ ╚████║    ╚██████╗██║  ██║███████╗╚██████╗          
              #################%@@@@%*******@@@@@@@@                  ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝          
               #########@@@@@@@@@@@@@%**@%**@@@@@@                               
            ########%@@@@@@@@@@@@@   #**@@***@@@                                 
              ##@@@@@@@@@@@            ***@@******  %                            
              @@@@@@@@@              #**********@@@@*@@                          
                @@@                    @@@@@@@@@@@@@@@@                           
                                       @@@@@@@@@@@@@                             
"""

set_fullscreen()

def is_valid_expression(expression):
    # Regular expression to validate the input for safety
    pattern = re.compile(r'^[0-9+\-*/(). ]+$')
    return pattern.match(expression)

while True:
    clear_console()
    # Print the universe watermark with vertical color effect
    print(Colorate.Vertical(Colors.purple_to_blue, universe_watermark, 1))  # Universe watermark
    print("")  # Print an empty line
    
    expression = input(Colorate.Vertical(Colors.purple_to_blue, "Enter your expression (e.g., 2 + 3 * (4 - 1)): ", 1)).strip()

    if is_valid_expression(expression):
        try:
            result = eval(expression)
            print(Colorate.Vertical(Colors.purple_to_blue, f'The result is: {result}', 1))
        except ZeroDivisionError:
            print(Colorate.Vertical(Colors.purple_to_blue, "Cannot divide by zero.", 1))
        except Exception as e:
            print(Colorate.Vertical(Colors.purple_to_blue, f"Error: {e}", 1))
    else:
        print(Colorate.Vertical(Colors.purple_to_blue, "Invalid expression. Please use numbers and operators only.", 1))

    cont = input(Colorate.Vertical(Colors.purple_to_blue, "Do you want to perform another calculation? [y/n]: ", 1)).strip().lower()
    if cont != 'y':
        break
