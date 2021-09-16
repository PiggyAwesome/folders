"""
Bruteforce all possible name combonations for folders and create them.
Author: PiggyAwesome

"""



from math import trunc
import random
import os
import glob


where = "Folders/" # Where to create folders


e = open("existing_files.txt", "r") # Open separately to make sure there is no confusion.
f = open("existing_files.txt", "a") #

current = e.read().splitlines()


os.chdir(where)

e.close()
num = glob.glob("*").__len__()
num2 = 000000
num3 = 000000



while True:
    try:
         a = random.choice("abcdefghijklmnopqrstuvwxyz0123456789 "); b = random.choice("abcdefghijklmnopqrstuvwxyz0123456789 "); c = random.choice("abcdefghijklmnopqrstuvwxyz0123456789 "); d = random.choice("abcdefghijklmnopqrstuvwxyz0123456789 ")
     
         if f"{a}{b}{c}{d}" not in current:
              os.mkdir(f"{a}{b}{c}{d}")
              num += 1
              print(f"#{num} {True} ---{a}{b}{c}{d}--- {True}") # Comment this for faster, less satisfying results
              f.write(f"{a}{b}{c}{d}\n")
              current.append(f"{a}{b}{c}{d}")
    except FileExistsError:   
        num2 += 1
        print(f"#{num2} {False} ---{a}{b}{c}{d}--- {False}") # Comment this for faster, less satisfying results
        f.write(f"{a}{b}{c}{d}\n")
        current.append(f"{a}{b}{c}{d}")
    except NotADirectoryError:
        num3 += 1
        print(f"#{num3} {None} ---{a}{b}{c}{d}--- {None}") # Comment this for faster, less satisfying results
        f.write(f"{a}{b}{c}{d}\n")
        current.append(f"{a}{b}{c}{d}")
    except Exception as error:
        print(error)
        pass