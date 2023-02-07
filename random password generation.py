import random
import array

MAX_LEN = 24

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
LOWER_CASE = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER_CASE = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
SPECIAL_CHARACTERS= ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

COMBINED_LIST = DIGITS + LOWER_CASE + UPPER_CASE + SPECIAL_CHARACTERS

rand_digits = random.choice(DIGITS)
rand_upper = random.choice(UPPER_CASE)
rand_lower = random.choice(LOWER_CASE)
rand_special = random.choice(SPECIAL_CHARACTERS)

temp_password = rand_digits + rand_lower + rand_special + rand_upper

for x in range(MAX_LEN - 4):
    temp_password = temp_password + random.choice(COMBINED_LIST)
    temp_pass_list = array.array('u', temp_password)
    random.shuffle(temp_pass_list)
password = ""
for x in temp_pass_list:
    password = password + x

print (password)
