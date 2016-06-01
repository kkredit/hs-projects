# lampParadox.py
#   A program to test the lamp paradox
# kevin kredit
import time

def main():
    x = 30.0
    on(x)

def m(x):
    xf = x / 2.0
    return xf

def off(x):
    if x != 60:
        x = m(x)
        print "off"
        time.sleep(x)
        on(x)

def on(x):
    if x != 60:
        x = m(x)
        print "on"
        time.sleep(x)
        off(x)

main()
