import math


def prime(n):
    prime_list = [0]*(n+1)
    prime_list[0] = prime_list[1] = 1
    i = 2

    while i<=math.sqrt(n) :
        if prime_list[i]==0:
            j=i+i
            while j <= n:
                prime_list[j] = 1
                j+=i
        i+=1
    final_prime = []

    k=0
    while k < n+1:
        if(prime_list[k] == 0):
            final_prime.append(k)
        k+=1

    return final_prime


