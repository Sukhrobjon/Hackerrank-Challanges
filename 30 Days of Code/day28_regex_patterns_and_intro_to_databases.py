#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    total_rows = int(input())
    # to store the email and names in list of list
    name_and_email_list = []
    # for validation the their email
    target = '@gmail.com'
    for i in range(total_rows):
        # get the user input and split by space
        firstNameEmailID = input().split()
        # add the new row, only if the emails has targer('@gmail.com')
        if target in firstNameEmailID[1]:
            name_and_email_list.append(firstNameEmailID)

    # sort the input by name, used 'key' function of sorted()
    sorted_name = sorted(name_and_email_list, key=lambda name: name[0])
    # unzip(put rows and columns seperately) sorted names and emails list
    # and [0] at the end will exract the names
    unzip_names = (list(zip(*sorted_name))[0])
    # print the names on a new line using seperator
    print(*unzip_names, sep='\n')
