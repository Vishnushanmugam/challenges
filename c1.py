def capital_indexes(s):
    b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    r=[]
    for i in range(0,len(s)):
        if s[i] in b:
            r.append(i)
    return r    
print(capital_indexes('ApPlE'))

def capital_indexes(s):
    lower= "abcdefghijklmnopqrstuvwxys"
    result = []
    for i, l in enumerate(s):
        if l in lower:
            result.append(i)
    return result
print(capital_indexes('ApPlE'))
