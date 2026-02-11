s = "abc"
t = "ahdgcb"
j = 0

def isSubSequence(s, t, j) -> bool:
    for i in range(len(t)):
        if t[i] == s[j]:
            j += 1
        else:
            continue

    if j == len(s):
        return True
    else:
        return False


print(isSubSequence(s, t, j))