string1 = "aabbcc"
string2 = "abcabc"


def isAnagram(string1, string2) -> bool:
    string1 = sorted(list(string1))
    string2 = sorted(list(string2))

    for i in string1:
        if i not in string2 or string1.count(i) != string2.count(i):
            return False
            break
        else:
            continue

    return True


print(isAnagram(string1, string2))