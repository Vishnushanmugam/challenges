statuses={
    "Alice":"online",
    "Bob":"offline",
    "Eve":"online",
}
l=[]
def online_count(a):
    c=0
    for i in a:
        if a[i]=="online":
            c+=1
    return c

print(online_count(statuses))