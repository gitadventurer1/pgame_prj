class Piece:
    def __init__(self, pos, race):
        self.pos = pos
        self.x, self.y = pos[0], pos[1]
        self.color = race
        self.pchanged = False

    def pmvs(self, brd):
        possiblef = []
        for a in self.mvs(brd):
            for b in a:
                if b.piece:
                    if b.piece.color == self.color:
                        break
                    else:
                        possiblef.append(b)
                        break
                else:
                    possiblef.append(b)
        return possiblef

    def valid(self, brd):
        out = []
        for a in self.mvs(brd):
            if not brd.check(self.color, turn=[self.pos, a.pos]):
                out.append(a)
        return out

    def attsq(self, brd):
        return self.mvs(brd)

    def move(self, brd, square, force=False):
        for b in brd.i:
            if b != '':
                b.colalt = False
        if square in self.valid(brd) or force:
            ps = brd.sq_fr_pos(self.pos)
            self.pos, self.x, self.y = square.pos, square.y, square.x
            ps.piece = None
            square.piece = self
            brd.clicked_on = None
            self.pchanged = True
            if self.type == 'pawn':
                if self.y == 0 or self.y == 7:
                    from data.classes.pieces.Queen import Queen
                    square.piece = Queen((self.x, self.y), self.color, brd)
            if self.type == 'king':
                if ps.x - self.x == 2:
                    b = brd.sq_fr_pos([0, self.y]).piece
                    if b:
                        b.move(brd, brd.sq_fr_pos([3, self.y]), force=True)
                elif ps.x - self.x == -2:
                    b = brd.sq_fr_pos([7, self.y]).piece
                    if b:
                        b.move(brd, brd.sq_fr_pos([5, self.y]), force=True)
            return True
        else:
            brd.clicked_on = None
            return False