class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._historia = [0]

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi
        self._historia.append(self._arvo)

    def plus(self, operandi):
        self._arvo = self._arvo + operandi
        self._historia.append(self._arvo)

    def nollaa(self):
        self._arvo = 0
        self._historia.append(self._arvo)

    def kumoa(self):
        if len(self._historia)>1:
            self._historia.pop()
        self._arvo = self._historia[-1]

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
