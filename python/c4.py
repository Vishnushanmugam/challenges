import random
#Find the coming number is odd or even number
def random_number():
    a = int(random.uniform(1, 100))
    if a%2:
        print(f"The coming number is odd: {a}")
    else:
        print(f"The coming number is even: {a}")
    return a
print(random_number())
