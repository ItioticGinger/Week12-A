# Matthew Brause
# CSCI 102 – Section C
# Week 12 - Part A

def PrintOutput(output):
    print("OUTPUT", output)

def LoadFile(filename):
    with open(filename, "r") as f:
        return f.readlines()
