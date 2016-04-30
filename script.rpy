# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.

# Main cast
define narrator = Character(None,
                          
                          what_size=20, #Font size
                          what_xalign=0.5, #Centers text within the window
                          window_xalign=0.5, #Centers the window horizontally
                          window_yalign=0.5, #Centers the window vertically
                          what_text_align=0.5, #Centers text within the window, just in case
                          window_background=None,#Removes the window, so only the text shows
                          window_ymaximum=300,
                          what_outlines=[(3, "#000000", 2, 2), (3, "#808080", 0, 0)],
                          #Gives an outline
                          what_slow_cps=30 #Speed at which the text appears (slow)
                          )
define mc_inner = Character(what_suffix = ' ▼', what_slow_cps=30)
define mc = Character('{b}Seven{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)
define nando = Character('{b}Nando{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)
define rosa =  Character('{b}Rosa{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)

#Supporting cast
define bob = Character('{b}Bob{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)

#mob
define male = Character('{b}Teen Boy{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)
define maleS = Character('{b}Male Student{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)
define otherMS = Character('{b}Other Male Student{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)
define girl = Character('{b}Girl{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)
define girlS = Character('{b}Female Student{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)
define girlA = Character('{b}Female Student A{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)
define girlB = Character('{b}Female Student B{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)
define girlAB = Character('{b}Female Student A & B{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)
define mechanics =  Character('{b}Mechanics{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)

#??? character
define mc_unrevealed = Character('{b}Boy{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)
define oldMan = Character('{b}Old Man{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)
define flashyGuy = Character('{b}Flashy Guy{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)
define highSG = Character('{b}High-Spirited Girl{/b}', color="#FFFFFF",  what_suffix = ' ▼', show_two_window = True, what_slow_cps=30)


# The game starts here.
label start:
    
    jump prolog

    


    
    
    
    



    return
