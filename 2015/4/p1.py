import hashlib
import sys
import itertools

secret = sys.stdin.readline().strip()

for i in itertools.count(1):
    input = secret + str(i)
    hash = hashlib.md5(input.encode()).hexdigest()
    if hash.startswith('000000'):
        print(i)
        break   
