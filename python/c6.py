def double_letters(a):
    for i in range(len(a)-1):
        if a[i]== a[i+1]:
            return True
    return False
a="hi"
print(double_letters(a))
