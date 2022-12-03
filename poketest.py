import pypokedex
import random


r = random.randint(1,251)
p=pypokedex.get(dex=r)

if __name__ == "__main__":
    print(p.dex)
    print(p.name)
    print(p.get_descriptions())
    print(str(p))



