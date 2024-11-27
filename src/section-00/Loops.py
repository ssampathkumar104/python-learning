from random import shuffle
from random import randint

if __name__ == "__main__":
    "For, While loops in python"

    mylist = [1,2,3,4,5,6,7,8,9,10]

    for ele in mylist:

        print(f"Current iteration is ==> {ele}")

    
    mylist2 = [1,2,3,4,5,6,7,8,9,10]

    for num in mylist2:

        if num%2 == 0:
            print(f"Number {num} is Even.")
        else:
            print(f"Number {num} is Odd.")

    
    list_sum = 0
    for num in mylist2:
        list_sum = num + list_sum
    print(f"Sum of list items are {list_sum}")

    myString = 'Birla Institute of technology and Sciences'

    for letter in myString:
        print(f'Letter is {letter}')

    for _ in "Hello World!":
        print('Cool!')

    tup = (1,2,3)

    for item in tup:
        print(f'Items in tuple is {item}')

    mylist3 = [(1,2),(3,4),(5,6),(7,8)]

    for item in mylist3:
        print(f'Item in list is {item}')
    
    for (key, value) in mylist3:
        print(f'Key in tuple is {key}')
        print(f'Value in tuple is {value}')

    mylist4 = [(1,2,3),(4,5,6),(7,8,9)]

    for (a,b,c) in mylist4:

        print(f"'a' value is {a}")
        print(f"'b' value is {b}")
        print(f"'c' value is {c}")
    
    dictry = {'k1':1,'k2':2, 'k3':3}

    for id in dictry:
        print(id)

    for key,value in dictry.items():
        print(value)

    """While loop"""
    x = 0
    while x<5:
        print(f'the current value of x is {x}')
        x = x+1
    else:
        print(f"X is not less than 5.")

    name = 'sampath'

    for letter in name:
        if letter == 'p':
            break
        print(letter)

    for num in range(0,10,2):
        print(f'{num}')

    print(list(range(0,11,2)))

    index_count = 0

    for letter in 'abcdefghijkl':
        print('At index {} the letter is {}'.format(index_count, letter))
        index_count = index_count + 1

    index_counter = 0
    word = 'abcdefghijklmnopq'

    for letter in word:
        print(word[index_counter])
        index_counter = index_counter+1

    word2 = 'sampathkumarsankati'
    for item in enumerate(word2):
        print(item)
        print(type(item))

    word2 = 'sampathkumarsankati'
    for index, letter in enumerate(word2):
        print(index)
        print(letter)

    list1 = [1,2,3,4]
    list2 = ['a','b','c','d']

    for item in zip(list1,list2):
        print(item)

    list1 = [1,2,3,4]
    list2 = ['a','b','c','d']
    list3 = [100,200,300,400]

    for item in zip(list1,list2,list3):
        print(item)

    print(list(zip(list1,list2)))

    print('x' in [1,2,3])

    print('x' in ['x','y','z'])

    print('mykey' in {'mykey':345})

    d = {'mykey':345}
    print(345 in d.keys())

    newList = [10,20,30,40,50,60,70,80,90,100]
    print(min(newList))
    print(max(newList))

    mylist5 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    shuffle(mylist5)
    print(mylist5)

    print(randint(0,1000))

    print(input('What is your name'))