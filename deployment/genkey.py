#!/usr/bin/env python3
import random
import os


def main():
    LENGTH = 50
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz0123456789'
    key = ''.join(random.choice(ALPHABET) for c in range(LENGTH))
    with open('/home/%s/key' % os.environ['APP_NAME'], 'w') as key_file:
        key_file.write(key)

if __name__ == '__main__':
    main()
