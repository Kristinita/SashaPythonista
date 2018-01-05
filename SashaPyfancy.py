import sys

from time import sleep

words = "This is just a test :P"
for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
