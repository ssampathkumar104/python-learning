

if __name__=="__main__":
    tu = (1,2,3)
    print("Type of the data is ",type(tu))
    tu2 = (1, 'two',3)
    print("Type of the data is ",type(tu2))
    print("Read data from tuple is ",tu2[1])
    print("Last value in tuple is ",tu2[-1])

    ###Methods
    print("index of the value is ",tu2.index('two'))
    print("Count of the value is ",tu2.count(3))