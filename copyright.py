#!/usr/bin/python3
import sys
import re


def main():
    try:
        cp_file = sys.argv[1]
        fil_dest = sys.argv[2]
    except Exception:
        print("Please specify BOTH copyright info and file destination.")
    if len(sys.argv) == 5:
        if str(sys.argv[3]) == '-c':
            check_file_type = str(sys.argv[4])
        elif str(sys.argv[3]) == '-u':
            new_file_type = '.' + str(sys.argv[4])

    
        


    
if __name__ == '__main__':
    main()
