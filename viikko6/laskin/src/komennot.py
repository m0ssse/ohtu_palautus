class Summa:
    def __init__(self, sovelluslogiikka, io):
        self._sovelluslogiikka = sovelluslogiikka
        self._io = io

    def suorita(self):
        return self._sovelluslogiikka.plus(int(self._io()))
    
class Erotus:
    def __init__(self, sovelluslogiikka, io):
        self._sovelluslogiikka = sovelluslogiikka
        self._io = io

    def suorita(self):
        return self._sovelluslogiikka.miinus(int(self._io()))
    
class Nollaus:
    def __init__(self, sovelluslogiikka, io):
        self._sovelluslogiikka = sovelluslogiikka
        self._io = io

    def suorita(self):
        return self._sovelluslogiikka.nollaa(self._io())
    
class Kumoa:
    def __init__(self, sovelluslogiikka, io):
        self._sovelluslogiikka = sovelluslogiikka
        self._io = io

    def suorita(self):
        self._sovelluslogiikka.kumoa()