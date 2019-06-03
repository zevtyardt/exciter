import time
import sys


def start(delay):
    while 1:
        sys.stdout.write('\r[kuzuri-chan]: sleeping for %s seconds ' % delay),
        sys.stdout.flush()

        if delay == 0:
            print()
            break

        time.sleep(1)
        delay -= 1
