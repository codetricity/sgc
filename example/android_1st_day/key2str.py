import pygame

def update(text, event):
    if event.key == pygame.K_a:
        text.append("a")
    elif event.key == pygame.K_b:
        text.append("b")
    elif event.key == pygame.K_c:
        text.append("c")
    elif event.key == pygame.K_d:
        text.append("d")
    elif event.key == pygame.K_d:
        text.append("d")
    elif event.key == pygame.K_e:
        text.append("e")
    elif event.key == pygame.K_f:
        text.append("f")
    elif event.key == pygame.K_g:
        text.append("g")
    elif event.key == pygame.K_h:
        text.append("h")
    elif event.key == pygame.K_i:
        text.append("i")
    elif event.key == pygame.K_j:
        text.append("j")
    elif event.key == pygame.K_k:
        text.append("k")
    elif event.key == pygame.K_l:
        text.append("l")
    elif event.key == pygame.K_m:
        text.append("m")
    elif event.key == pygame.K_n:
        text.append("n")
    elif event.key == pygame.K_o:
        text.append("o")
    elif event.key == pygame.K_p:
        text.append("p")
    elif event.key == pygame.K_q:
        text.append("q")
    elif event.key == pygame.K_r:
        text.append("r")
    elif event.key == pygame.K_s:
        text.append("s")
    elif event.key == pygame.K_t:
        text.append("t")
    elif event.key == pygame.K_u:
        text.append("u")
    elif event.key == pygame.K_v:
        text.append("v")
    elif event.key == pygame.K_w:
        text.append("w")
    elif event.key == pygame.K_x:
        text.append("x")
    elif event.key == pygame.K_y:
        text.append("y")
    elif event.key == pygame.K_z:
        text.append("z")
    elif event.key == pygame.K_0:
        text.append("0")
    elif event.key == pygame.K_1:
        text.append("1")
    elif event.key == pygame.K_2:
        text.append("2")
    elif event.key == pygame.K_3:
        text.append("3")
    elif event.key == pygame.K_4:
        text.append("4")
    elif event.key == pygame.K_5:
        text.append("5")
    elif event.key == pygame.K_6:
        text.append("6")
    elif event.key == pygame.K_7:
        text.append("7")
    elif event.key == pygame.K_8:
        text.append("8")
    elif event.key == pygame.K_9:
        text.append("9")
    elif event.key == pygame.K_SPACE:
        text.append(" ")
    elif event.key == pygame.K_AT:
        text.append("@")
    elif event.key == pygame.K_BACKSPACE:
        del text[-1]
    return (text)
