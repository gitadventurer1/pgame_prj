import pygame


class Square:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.ax = x * w
        self.ay = y * h
        self.pos = [x, y]
        self.col = (220, 210, 200) if (x + y) % 2 == 0 else (50, 50, 50)
        self.col2 = (100, 250, 100) if (x + y) % 2 == 0 else (0, 200, 0)
        self.piece = None
        self.colalt = False
        self.rect = pygame.Rect(
            self.ax,
            self.ay,
            self.w,
            self.h
        )

    def draw(self, dis):
        if self.colalt:
            pygame.draw.rect(dis, self.col2, self.rect)
        else:
            pygame.draw.rect(dis, self.col, self.rect)
        if self.piece:
            cr = self.piece.img.get_rect()
            cr.center = self.rect.center
            dis.blit(self.piece.img, cr.topleft)
