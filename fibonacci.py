# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:49:46 2021

@author: rodrigo
"""
def fib(n):

        if n==0:
            return 0
        if n==1:
            return 1

        fibon = fib(n-1)+fib(n-2)

        return fibon
    

def fib2(n,memo={0:0,1:1}):
    # print(memo)
    try:
        return memo[n]

    except:
        fibon = fib2(n-1)+fib2(n-2)
        memo[n]=fibon

        return fibon

def fib3(n,lista=[0,1]):
    print(lista)
    # print(f'Calculando Fibo de {n}')    
    if len(lista)>n:  
        # print(f'Retornando da lista Fibo de {n}')
        return lista[n]

    else:
        
        fibon = fib3(n-1)+fib3(n-2)        
        lista.append(fibon)

        return fibon
 
# for i in range(20): 
#     print(f'Fibonacci {i} = {fib3(i)}')

print(fib3(40))
# print(fib2(40))