#!/usr/bin/env python3

import os


def find_replace(find: str, replace: str):  # type check, only strings allowed as input
    os.makedirs(replace)  # make directory called replace in working directory
    for file_name in os.listdir("."):
        if file_name.endswith(".txt"):
            file = open(file_name, "r")
            for line in file:  # for every line
                if find in line:
                    file.close()  # close file and reopen to read from first line
                    file = open(file_name, "r")
                    transfer = file.read()
                    transfer = transfer.replace(find, replace)
                    new_file = open(".\\" + replace + "\\" + file_name, "w+")
                    new_file.write(transfer)
                    new_file.close()
                break
            file.close()


find = input("Enter the word to find: ")
replace = input("Enter the word to replace: ")
find_replace(find, replace)
