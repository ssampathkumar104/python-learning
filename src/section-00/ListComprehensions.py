


if __name__ == "__main__":

    word = 'hello'
    mylist = []
    for letter in word:
        mylist.append(letter)
    print(mylist)


    mylist = [letter for letter in word]
    print(mylist)

    mynumlist = [num for num in range(0,11,2)]
    print(mynumlist)

    mynumlist = [num**2 for num in range(0,11,2)]
    print(mynumlist)

    mylisteven = [x for x in range(0,100) if x%2==0]
    print(mylisteven)

    mylistodd = [num for num in range(0,100) if not num%2 ==0 ]
    print(mylistodd)

    celcius = [0,10,20,34.5]

    fahrenheit = [((9/5)*temp + 32) for temp in celcius]
    print(fahrenheit)

    results = [x if x%2 == 0 else 'ODD' for x in range(0,100)]
    print(results)

    mulpList = []

    for x in [2,4,6]:
        for y in [1,10,1000]:
            mulpList.append(x*y)
    print(mulpList)

    myresults = [ x*y for x in [2,4,6] for y in [1,100,10]]
    print(myresults)