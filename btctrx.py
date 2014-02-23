class Trx:
    def __init__(self, d, r, f):
        " ctor(date, rate, face)"
        self.date = d
        self.rate = r
        self.face = f # negative means short


class Trade:
   "grouping of basis and the offseting trades"
   def __init__(self, b, o):
       " Trx basis, [Trx] offsets"
       self.basis = b
       self.offseting = o


