# Matthew Brause
# CSCI 102 – Section C
# Week 12 - Part A

def PrintOutput(output):
    print("OUTPUT", output)

def LoadFile(filename):
    with open(filename, "r") as f:
        return f.readlines()

def UpdateString(string, update, num):
    string_list = list(string)
    string_list[num] == update
    string_updated = ''
    for i in string_list:
        string_updated += i
    return string_updated
