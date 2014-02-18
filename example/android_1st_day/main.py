import pygame, sys
import key2str

try:
    import android
except ImportError:
    android = None

pygame.init()

if android:
    android.init()
    android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)


BLACK = (0, 0,0)
GREEN = (0, 200, 0)
YELLOW = (0, 200, 200)
GRAY = (120, 120, 120)
WHITE = (255, 255, 255)


screen = pygame.display.set_mode((480, 320))

button = pygame.Rect(10, 10, 100, 50)
button_fnt = pygame.font.Font("animeace2_reg.ttf", 14)
button_surf1 = button_fnt.render("Show/Hide", True, BLACK)
button_surf2 = button_fnt.render(" Keyboard", True, BLACK)
button_line2 = (10, 28)

text3 = button_fnt.render("Back = close keyboard or exit", True, WHITE)
text3_line = (120, 36)

inputbox = pygame.Rect (10, 70, 460, 30)
textsurface = pygame.Surface((460, 30))
textsurface.fill(GRAY)


keyboard_up = False

maintext = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            maintext = key2str.update(maintext, event)
            textstring = ''.join(maintext)
            textsurface = button_fnt.render(textstring, True, WHITE)
            if event.key == pygame.K_ESCAPE:
                if keyboard_up:
                    android.hide_keyboard()
                    keyboard_up = False
                else:
                    pygame.quit()
                    sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            touch_pos = pygame.mouse.get_pos()
            if button.collidepoint(touch_pos):
                if keyboard_up == False:
                    keyboard_up = True
                elif keyboard_up == True:
                    keyboard_up = False
            if android:
                if keyboard_up:
                    android.show_keyboard()
                else:
                    android.hide_keyboard()

    pygame.draw.rect(screen, GREEN, button)
    screen.blit(button_surf1, button)
    screen.blit(button_surf2, button_line2)
    screen.blit(text3, text3_line)

    pygame.draw.rect(screen, GRAY, inputbox)
    screen.blit(textsurface, inputbox)

    
    pygame.display.update()

