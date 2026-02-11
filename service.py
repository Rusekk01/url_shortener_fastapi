from random import choice
from string import ascii_letters, digits


class ShortURl():
    def __init__(self):
        self.url = self.link_gen()

    def link_gen(self):
        res = ""
        for _ in range(6):
            res += choice(ascii_letters+digits)
        return res