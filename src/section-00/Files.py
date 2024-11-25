import os

if __name__=="__main__":
    print('Present working directory',os.getcwd())
    my_file = open('C:\\code\\ml\\learning\\src\\section-00\\test.txt')
    print(my_file.read())
    print(my_file.readlines())

    my_file = open('C:\\code\\ml\\learning\\src\\section-00\\test.txt','w+')
    my_file.write('This is a new line')
    print(my_file.seek(0))
    print(my_file.read())

    my_file = open('C:\\code\\ml\\learning\\src\\section-00\\test.txt','a+')
    my_file.write('\nThis is text being appended to test.txt')
    my_file.write('\nAnd another line here.')
    print(my_file.readlines())