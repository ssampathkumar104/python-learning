

if __name__=="__main__":
    Skills = ['Java','Selenium','Infor ERP LN',
              'Maven','Git','GitHub','Gitlabs',
              'AWS-EC2, VPC, Security Groups, S3, IAM', 'Docker', 'TestNG','Apache POI']
    print("Length of the List is ",len(Skills))
    print('Type of the data is ',type(Skills))
    print("Sub-string of the list is ",Skills[0])
    print("Sub-string of the list is ",Skills[0:])
    print("Sub-string of the list is ",Skills[:5])
    print("Sub-string of the list is ",Skills[0:-1])
    print("Sub-string of the list is ",Skills[0:-5])
    print("Sub-string of the list is ",Skills[3:])
    print("Sub-string of the list is ",Skills[:-3])
    Skills+['Python']
    print("Length of the List is ",len(Skills+['Python']))
    Skills = Skills+['Python']
    print("Length of the List is ",len(Skills))

    ###Basic Operations
    Skills.append('Machine Learning')
    print("List data is ",Skills)
    Skills.pop(0)
    print("List data is ",Skills)
    Skills.pop(3)
    print("List data is ",Skills)
    Skills.sort()
    print("Sort List is ",Skills)
    Skills.reverse()
    print("Reverse List is ",Skills)

    ###Nested Lists
    list_1=[1,2,3]
    list_2=[4,5,6]
    list_3=[7,8,9]

    matrix = [list_1, list_2, list_3]

    print('Matrix is',matrix)
    print('First row of Matrix is',matrix[0])
    print('First element of Matrix is',matrix[0][0])

    ### List Comprehensions
    first_col = [row[0] for row in matrix]
    print('First column is ',first_col)