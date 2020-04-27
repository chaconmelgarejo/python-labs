#!/usr/bin/env python3
import sys

def howto():

    print("welcome to my python header code:")
    print("This code help you how to use this script!")
    sys.exit()

def main():

    if len(sys.argv) > 1 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        howto()
        sys.exit(1)
    
    if len(sys.argv) > 1 and (sys.argv[1] == "-a" or sys.argv[1] == "--arg"):
        first = sys.argv[2]
        print("Your First Argument is: "+first)


    print("no arguments!")
    print("usage:./header.py -a [first argument] || -h or --help [for help]")

main()
