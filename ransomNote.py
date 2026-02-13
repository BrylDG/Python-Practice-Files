ransomNote = "aab"
magazine = "aab"

def constructLetter(ransomNote, magazine) -> bool:
    letterCount = {}
    for j in magazine:
        if j in letterCount:
            letterCount[j] += 1
        else:
            letterCount[j] = 1

    for i in ransomNote:
        if i not in letterCount:
            return False
        elif letterCount[i] == 1:
            del letterCount[i]
        else:
            letterCount[i] -= 1

    return True

print(constructLetter(ransomNote, magazine))