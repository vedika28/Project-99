def swapFileData():
    file1= input('Enter 1st file to swap: ')
    file2= input('Enter 2nd file to swap: ')
    with open(file1, 'r') as f1:
        data_a = f1.read()
    with open(file2, 'r') as f2:
        data_b = f2.read()

    with open(file2, 'w') as file2:
        file2.write(data_a)   
    with open(file1, 'w') as file1:
        file1.write(data_b)


swapFileData()
