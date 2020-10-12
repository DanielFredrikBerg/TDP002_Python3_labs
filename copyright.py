#!/usr/bin/python3
import sys
import os
import re


def main():
    check_file_type = ''
    new_file_name = ''
    try:
        cp_file = sys.argv[1]
        file_dest = sys.argv[2]
    except Exception:
        print("Please specify BOTH copyright info file and file destination.")
    if len(sys.argv) == 5:
        if str(sys.argv[3]) == '-c':
            check_file_type = str(sys.argv[4])
        elif str(sys.argv[3]) == '-u':
            if file_dest.__contains__('.'):
                new_file_name = file_dest.split('.')[0] + str(sys.argv[4])
            else:
                new_file_name = file_dest + str(sys.argv[4])

    is_file = True
    #if str(file_dest)[-1] == '/':
        #is_file = False

    if is_file:
        with open(str(cp_file), 'r') as cr_file:
            copyright_text = cr_file.read()

        with open(str(file_dest), 'r') as destination_f:
            dest_content = destination_f.read()
    #else:
        

    rewritten = re.sub(r'(?<=BEGIN COPYRIGHT)([\S\s]*?)(?=END COPYRIGHT)', copyright_text, dest_content)
                
    if check_file_type:
        if filename[-len(check_file_type):] == check_file_type:
            if new_file_name:
                with open(str(new_file_name), 'w') as rw_file:
                    rw_file.write(rewritten)
            else:    
                with open(str(file_dest) + new_file_type, 'w') as rw_file:
                    rw_file.write(rewritten)
        else:
            print(file_dest, ': Invalid file')
    else:
        with open(str(file_dest), 'w') as rw_file:
            rw_file.write(rewritten)
        

    
if __name__ == '__main__':
    main()
