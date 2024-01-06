#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    la = len(sys.argv) - 1
    if la == 0:
        print("0 arguements.")
    elif la == 1:
        print("1 argument:")
    elif la > 1:
        print("{} arguments:".format(la))

    for i in range(1, la + 1):
        print("{}: {}".format(la, sys.argv[i]))
    
