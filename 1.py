import sys

print(sys.argv)
if len(sys.argv) >1:
    for a,b in sys.argv[0:],range(len(sys.argv[0:])):
        print(a)