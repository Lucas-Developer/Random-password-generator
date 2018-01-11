# !/usr/bin/python
import random, string
myrg = random.SystemRandom()
length = 10
alphabet = string.ascii_letters + string.digits
pw = str().join(myrg.choice(alphabet) for _ in range(length))
print (pw)