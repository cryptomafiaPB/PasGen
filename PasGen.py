#importing random
import random

def randlatters(x,y):
    return chr(random.randint(ord(x), ord(y)))
    
def pas_gen():
    cap_later = list() #capital latters
    sm_later = list() #small latters
    nums = list() #numbers
    sym = ["!", "@", "#", "$", "%", "&"]
    for cap in range(5):
        cap_later.append(randlatters("A", "Z"))
    for sm in range(5):
        sm_later.append(randlatters("a", "z"))
    for num in range(5):
        nums.append(str(random.randint(0,9)))
    password = cap_later + sm_later + nums + sym
    random.shuffle(password)
    gen_pas = "".join(password)
    return gen_pas
print(pas_gen())
