def add_dots(a):
    s=".".join(a)
    return s
print(add_dots("test"))

def remove_dots(a):
    s=a.replace(".","")
    return s
print(remove_dots("t.e.s.t"))

def add_dot(s):
    return ".".join(s)
print(add_dot("test"))

def remove_dots(s):
    return s.replace(".","")
print(remove_dots("t.e.s.t"))
