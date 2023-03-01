import pygame


from data.classes.Base import Board, baseboard


pygame.init()
screensize = (800, 800)
screen = pygame.display.set_mode(size=screensize)

brd = Board(screensize[0], screensize[1])


def draw(display):
    display.fill((0, 0, 0))
    brd.draw(display)
    pygame.display.update()


if __name__ == '__main__':
    run = True
    pygame.display.set_caption('Шахматы')
    while run:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(mx, my)
                    brd.click(mx, my)
        if brd.checkmate('BL'):
            print('Белый победил')
            run = False
        elif brd.checkmate('WH'):
            print('Чёрный победил')
            run = False
        draw(screen)