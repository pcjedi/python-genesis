import time


def makeitrain(duration=1):
    start = time.time()
    while time.time() - start < duration:
        print("Money!!!")


def whoami():
    print("I am ", __name__)
