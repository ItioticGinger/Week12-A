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

def FindWordCount(text_list, string_test):
    count = 0
    for i in text_list:
        if string_test in i:
            for j in range(len(i)-len(string_test)):
                if string_test[0] == i[j]:
                    bad = 0
                    for k in range(len(string_test)):
                        if i[j] != string_test[k]:
                            bad = 1
                    if bad == 0:
                        count += 1
    return count
