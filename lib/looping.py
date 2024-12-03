#!/usr/bin/env python3

def happy_new_year():
    counter = 10

    while counter > 0:
        print(counter)
        counter -= 1
    print('Happy New Year!')
happy_new_year()


def square_integers(int_list):
    squared_integers = [num**2 for num in int_list]
    
    return squared_integers
    
square_integers([1, 2, 3, 4, 5])


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            i = 'FizzBuzz'
            print(i)

        elif i % 3 == 0:
            i = 'Fizz'
            print(i)
            
        elif i % 5 == 0:
            i = 'Buzz'
            print(i)
        
        else: 
            print(i)
           
fizzbuzz()


# fizzbuzz()