# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma ohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"Lukujen {x} ja {y} summa on {x} + {y} = {summa(x, y)}")  # muutos bugikorjaus-branchissa # muutos mainissa
print(f"Lukujen {x} ja {y} erotus on {x} - {y} = {erotus(x, y)}")  # muutos bugikorjaus-branchissa # muutos mainissa

logger("lopetetaan ohjelma")
print("goodbye!")