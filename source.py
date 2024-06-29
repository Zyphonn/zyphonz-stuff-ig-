import colorama, time, os, keyboard, pyperclip, curses
os.system("title Zyphonz stuff - V0.1")
print(colorama.Fore.MAGENTA,"""
███████╗██╗   ██╗██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗              
╚══███╔╝╚██╗ ██╔╝██╔══██╗██║  ██║██╔═══██╗████╗  ██║╚══███╔╝              
  ███╔╝  ╚████╔╝ ██████╔╝███████║██║   ██║██╔██╗ ██║  ███╔╝               
 ███╔╝    ╚██╔╝  ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║ ███╔╝                
███████╗   ██║   ██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗              
╚══════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝              
                                                                          
                                ███████╗████████╗██╗   ██╗███████╗███████╗
                                ██╔════╝╚══██╔══╝██║   ██║██╔════╝██╔════╝
                                ███████╗   ██║   ██║   ██║█████╗  █████╗  
                                ╚════██║   ██║   ██║   ██║██╔══╝  ██╔══╝  
                                ███████║   ██║   ╚██████╔╝██║     ██║     
                                ╚══════╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝     
                                                                          
                                                     ██╗██╗ ██████╗ ██╗   
                                                    ██╔╝██║██╔════╝ ╚██╗  
                                                    ██║ ██║██║  ███╗ ██║  
                                                    ██║ ██║██║   ██║ ██║  
                                                    ╚██╗██║╚██████╔╝██╔╝  
                                                     ╚═╝╚═╝ ╚═════╝ ╚═╝   
                                                                                
""")
print(colorama.Fore.LIGHTMAGENTA_EX,"R o b l o x   s c r i p t s :")
print(colorama.Fore.MAGENTA,"1:  Project Kali (Actively being worked on so expect bugs)")
print(colorama.Fore.MAGENTA,"2:  ROTX (discontinued)")
print(colorama.Fore.MAGENTA,"3:  Synapse X Remake (discontinued ofc)")
print(colorama.Fore.MAGENTA,"4:  Patchma V28 Redesign (discontinued)")
print(colorama.Fore.LIGHTMAGENTA_EX,"O t h e r   s t u f f :")
print(colorama.Fore.MAGENTA,"5:  NanoBatch (content warning mm i made cuz idkifdfijojgsdfjcx)")
print(colorama.Fore.LIGHTBLACK_EX,"Console:")
LINE_CLEAR = '\x1b[2K'
print(end=LINE_CLEAR)
print("     Console Initialized", end='\r')
while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        
        if event.name == '1':
            pyperclip.copy("loadstring(game:HttpGet('https://raw.githubusercontent.com/Zyphonn/ProjectKaliUpdated/main/main.lua'))()")
            print(end=LINE_CLEAR)
            print("     Copied loadstring to clipboard for Project Kali", end='\r')
        elif event.name == '2':
            pyperclip.copy("loadstring(game:HttpGet('https://raw.githubusercontent.com/Zyphonn/rotx/main/main.lua'))()")
            print(end=LINE_CLEAR)
            print("     Copied loadstring to clipboard for ROTX", end='\r')
        elif event.name == '3':
            pyperclip.copy("loadstring(game:HttpGet('https://raw.githubusercontent.com/Zyphonn/synapse-x-remake/main/source.lua'))()")
            print(end=LINE_CLEAR)
            print("     Copied loadstring to clipboard for Synapse X Remake", end='\r')
        elif event.name == '4':
            pyperclip.copy("loadstring(game:HttpGet('https://raw.githubusercontent.com/Zyphonn/patchma-v28-redesign/main/main.lua'))()")
            print(end=LINE_CLEAR)
            print("     Copied loadstring to clipboard for Patchma V28 Redesign", end='\r')
        elif event.name == '5':
            os.system("start https://github.com/Zyphonn/NanoBatch-/raw/main/NanoBatch.zip")
            print(end=LINE_CLEAR)
            print("     Downloaded NanoBatch | Open content warning and launch nano batch to open the mod menu", end='\r')