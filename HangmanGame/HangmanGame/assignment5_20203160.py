import time

def iterfibo(nbr) :
    l = [0 , 1]
    cnt = 1
    if nbr <= 1 :
        return nbr

    else :
        a = 0
        while cnt != nbr :
            a = sum(l)
            l.append(a)
            del l[0]
            cnt += 1
        return a
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


while True :
    nbr = int(input("Enter a number: "))
    if nbr == -1 :
        break
    ts = time.time()

    fibonumber = iterfibo(nbr)

    ts = time.time() - ts

    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))

    ts = time.time()

    fibonumber = fibo(nbr)

    ts = time.time() - ts

    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))



