from random import shuffle
from random import randint


if __name__ == "__main__":

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