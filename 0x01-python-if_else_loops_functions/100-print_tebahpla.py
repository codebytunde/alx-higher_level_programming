#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}{}".format(chr(i).lower(), chr(i - 1).upper()), end='')
