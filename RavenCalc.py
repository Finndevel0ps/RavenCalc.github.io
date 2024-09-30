import os
import ctypes
import subprocess
import json
from pystyle import *
import win32gui, win32con

def install_requirements():
    try:
        # Install required packages from requirements.txt
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    except Exception as e:
        print(f"Error installing packages: {e}")
        print("Please install the required packages manually.")

# Call the install function before your main logic
install_requirements()

# Change the title of the Command Prompt window using ctypes
def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

set_console_title("RavenCalc Made by Faranpc and digitaluserr on Discord")

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
