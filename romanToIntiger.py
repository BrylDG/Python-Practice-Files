romanNumber = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
total = 0
given = 'IVXLDCM'
length = len(given)
i = 0

while i < length:
    if i < length-1 and romanNumber[given[i]] > romanNumber[given[i+1]]:
        total += romanNumber[given[i]]
        i += 1
    else:
        total += romanNumber[given[i+1]] - romanNumber[given[i]]
        i += 2

print(total)