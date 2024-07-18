f1='Fizz'
f2='Buzz'
f3='FizzBuzz'
def fizzbuzz(n):
    for i in range(1, n+1):
        if i%3==0 and i%5==0:
            print(f3)
        elif i%3==0:
            print(f1)
        elif i%5==0:
            print(f2)
        else:
            print(i)

if __name__== '__main__':
    getting=int(input())
    fizzbuzz(getting)
