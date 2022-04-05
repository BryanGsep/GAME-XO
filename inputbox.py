# import sys module
import pygame
import tools

def draw_input_window(surface, Text, Vpos, Hpos):
    base_font = pygame.font.Font(None, 40)
    user_text = ''
    # create rectangle
    input_rect = pygame.Rect(Vpos, Hpos, 140, 40)
    # color_active stores color(lightskyblue3) which
    # gets active when input box is clicked by user
    color_active = pygame.Color('lightskyblue3')
    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = pygame.Color('chartreuse4')
    color = color_passive

    active = False
    run = True
    while run:
        for event in pygame.event.get():
            # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                # Check for backspace
                if event.key == pygame.K_SPACE:
                    run = False
                elif event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode
        # it will set background color of screen
        surface.fill((0, 0, 0))

        if active:
            color = color_active
        else:
            color = color_passive

        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(surface, color, input_rect)

        text_surface = base_font.render(user_text, True, (255, 255, 255))

        # render at position stated in arguments
        surface.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width() + 10)

        textfont = pygame.font.SysFont('comicsans', 40)
        textlabel = textfont.render(Text, True, (255,255,255))
        surface.blit(textlabel, (input_rect.x - textlabel.get_width()-5, input_rect.y-15))
        # display.flip() will update only a portion of the
        # screen to updated, not full area
        tools.draw_status('!!! Nhan [Space] de hoan thanh ten', (255, 255, 255), surface)
        pygame.display.update()

    return user_text

