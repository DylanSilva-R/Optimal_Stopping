class calculations:
    def __init__(self, candidates):
        self.candidates = candidates;

    def optimalStoppingCalc(self):
        e = 2.71828
        k = round(self.candidates / e)
        return k