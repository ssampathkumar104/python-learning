

if __name__ == "__main__":

    employee = {'Name':'Sampath Sankati',
                'Age':30,
                'Gender':'Male',
                'Qualification':'M.Tech(Data Science & Engineering)',
                'Occupation':'Software Engineer',
                'Experience':'8 Yrs',
                'City':'Hyderabad',
                'College':'BITS Pilani',
                'Grade':7.6
                }
    print("Keys are ",employee.keys())
    print("Values are ",employee.values())
    print('Name of the employee is',employee['Name'])
    print('Name of the employee is',employee['Name'][0])

    ###Nested Dictionaries
    dictionary = {'Name':'Sampath Sankati','Exp':'8 Yrs', 'Skills':{'Language-1':'Java','Language-2':'Python','Tool':'Selenium','Cloud':'AWS'}}
    print("Nested dict reading is ",dictionary['Skills']['Cloud'])

    ###Methods
    print("Keys are ",dictionary.keys())
    print("Values are", dictionary.values())
    print("Items in dictionary are ",dictionary.items())