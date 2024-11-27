



if __name__ == "__main__":
    print("Hello")
    print("Hello \n Hi")
    name = 'S Sampath Kumar'
    print("Length of the string is", len(name))
    print("Type of the data is ", type(name))
    print("First letter of the string name is ", name[0])
    print("sub string of the string name is ", name[0:9])
    print("sub string of the string name is ", name[0:-1])
    print("sub string of the string name is ", name[:-1])
    print("sub string of the string name is ", name[3:])
    print("sub string of the string name is ", name[3:7])
    print("To lower case is  ", name.lower())
    print("To upper case is  ", name.upper())
    print(f"Name of the user is {name}")

    """
    Below code is to explain the format string usage in python with details of a person.
    """
    name = 'S Sampath Kumar'
    salutation = 'Mr. '
    age = 30
    gender = 'Male'
    qualification = 'M.Tech (Data Science & Engineering)'
    college = 'BITS Pilani'
    occupation = 'Software Engineer'
    experience = '8 Yrs'
    city = 'Hyderabad'
    Skills = ['Java','Selenium','Infor ERP LN','Maven','Git','GitHub','Gitlabs','AWS-EC2, VPC, Security Groups, S3, IAM', 'Docker', 'TestNG','Apache POI']

    print(f"""INTRODUCTION: 
Name of the Candidate is {salutation}{name}.Gender of the candidate is {gender} with age {age}. 
His qualification is {qualification} from renowned college {college} from the city of {city}.
He is currently working as {occupation} with experience {experience} with below skills,""")
    counter = 0
    for skill in Skills:
        counter = counter + 1
        print(f'Skill{counter}:',skill)

    print('Skills are {3},{0},{1},{2}'.format('Java','Selenium','Maven','TestNG'))
    print('Skills are {c},{b},{d},{a}'.format(a='Java',b='Selenium',c='Maven',d='TestNG'))
    print('A {p} saved is a {p} earned'.format(p='penny'))

    print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
    print('{0:8} | {1:9}'.format('Apples', 3.))
    print('{0:8} | {1:9}'.format('Oranges', 10))

    print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
    print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))

    print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
    print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))

    print(f"He said his name is {name!r}") # to get string representation.
    