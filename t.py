"""function that checks if every char in string is unique"""

def allunique(str):
    for char in str:
        if str.count(char) > 1:
            return False
    return True

"""check if one str is a permutation of another"""
def anagram(str1, str2):
    lst1 = [i for i in str1 if i in str2.lower()]
    if len(str1) == len(lst1):
        return True
    else:
        return False

"""replaces empy spaces in str with %20"""
def urlhelp(str, length):
    lst1 = [i if not ' ' else '%20' for i in str]
    str = lst1.join('')
    return str

"""check if str is permutation of palindrome"""
def permpalindrome(str1, str2):
    if len(str1) != len(str2):
        return False               # if lengths are not equal it is not perm
    else:
        lst = [i for i in str1.lower() if str1.lower().count(i) == str2.lower().count(i)]
        if len(lst) == len(str1):    # check if each char in str is in the other str and if counts are equal
            return True
        return False

"""check if str is onle one edit away from same as other str"""
def oneway(str1, str2):
    diff = abs(len(str1) - len(str2))
    if diff == 0:
        lst = [i for i in str1 if i in str2]
        if len(lst) == len(str2):
            return True
    elif diff == 1:
        ma = max(len(str1), len(str2))
        mi = min(len(str1), len(str2))
        lst = [i for i in mi if i in ma]
        if len(lst) == len(ma) - 1:
            return True
    else:
        return False

