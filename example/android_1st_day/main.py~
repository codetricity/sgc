import sgc
from sgc.locals import *

import pygame
from pygame.locals import *

import sys

class ClickButton(sgc.Button):
    def on_click(self):
        self.level = 2
        print("Starting Game.  Going to level {}".format(self.level))        
        self.config_set = False

def game_quit():
    pygame.quit()
    sys.exit()


pygame.init()

try: 
    import android
except ImportError:
    android = None


if android:
    android.init()
    android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

menu_top = 30
menu_left = 10

fonts = {"widget": "fnt/FreeSans.ttf", "title": "fnt/FreeSans.ttf", "mono": "fnt/FreeMono.ttf"}
sgc.Font.set_fonts(fonts)

screen = sgc.surface.Screen((480, 320))

clock = pygame.time.Clock()


btn = ClickButton(label="Start", 
                  pos=(menu_left, menu_top),
                  col = (0, 200, 0),
                  label_col = (0, 0, 0))


button2 = sgc.Button(col=(200, 200, 0), 
                     label_col =(0,0,0),  
                     label = "Quit", 
                     pos=(menu_left, menu_top + 60))

# cool use of assigning the method "on_click" to a pre-defined function
button2.on_click = game_quit


combo_a = sgc.Combo(pos=(250, menu_top), 
                    label="Choose Character", 
                    label_side="top",
                    values=("dog", "cat", "mouse", "mongoose"))


radio_a = sgc.Radio(pos = (menu_left, menu_top +200),
                    label = "Enable GPS",
                    lable_side = "right",
                    group = "first_group")

def main():

    btn.add(0)
    button2.add(1)
    combo_a.add(2)
    radio_a.add(3)

    btn.level = 1
    level = btn.level
    btn.config_set = True

    screen_color = (50,50,50)

    while True:

        if android:
            if android.check_pause():
                android.wait_for_resume()

        time = clock.tick(30)

        for event in pygame.event.get():
            sgc.event(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        level = btn.level
        if level == 2:
            if btn.config_set == False:
                screen_color = (0, 200, 0)
                btn.remove(fade=False)
                combo_a.remove(fade=False)
                print("configured 2nd screen settings")
                btn.config_set = True

        screen.fill(screen_color)
        sgc.update(time)
        pygame.display.flip()

if __name__ == "__main__":
    main()
