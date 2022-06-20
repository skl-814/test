import numpy
import sys
from sys import exit

cmdinlist = [
    '-i',
    '-I',
    '--input',
    '-o',
    '-O',
    '--version',
    '-v',
    '-h','--help',
    ]

def cmdinput(retl):
    if '-i' in retl:
        aa = 0
        for a in retl:
            aa += 1
            if a == "-i":
                break
        return retl[aa+1:]

def retstr(retl):
    retstr = ''
    for a in retstr:
        retstr += ' ' + a


def cmddl():
    if len(sys.argv) > 1:
        retl = sys.argv[0:]
        
    else:
        return None


print(cmddl())