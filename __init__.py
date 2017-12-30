from pycube256 import CubeHash

class RegMaker:

    def __init__(self, letters=15, numbers=10, maxlength=64, separator="-", spacing=5, charset=None):
        if charset == None:
            self.charset = range(65,91)
        else:
            self.charset = charset
        self.separator = separator
        self.spacing = spacing
        self.letters = letters
        self.numbers = numbers
        self.hash_length = maxlength * 8
        if (self.letters + self.numbers) > maxlength or maxlength > 64:
            raise ValueError('Error: maxlength exceeded')

    def gen(self, mac, mode=1):
        m = "".join(mac.split(':'))
        if mode == 1:
            k = CubeHash(mode=self.hash_length).hash(m)
        else:
            k = m * 64
        f = []
        a = []
        y = 0
        for b in k:
            c = ord(b) % 10
            f.append(c)
            a.append(chr(self.charset[c]))
            y += ord(b)
        z = []
        for x in range(self.numbers):
            z.append(str(f.pop()))
        for x in range(self.letters):
            z.append(a.pop())
        for x in range(y):
            z.append(z.pop(0))
            z.append(z.pop(x % len(z)))
        p = "".join(z)
        if self.spacing > 0:
            q = []
            start = 0
            end = self.spacing
            for x in range(len(z) / self.spacing):
                if x == ((len(z) / self.spacing) - 1):
                    q.append(p[start:end])
                else:
                    q.append(p[start:end]+self.separator)
                start += self.spacing
                end += self.spacing
            return "".join(q)
        else:
            return p

        return "".join(z)
