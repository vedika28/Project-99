import os, shutil

path2=input("Please enter the file path you want to remove: ")
trash='C:/Users/vedik/OneDrive/Desktop/Python Projects/SwappingFile/trash'
shutil.move(path2,trash)

listOfFiles=os.listdir(trash)
for file in listOfFiles:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext=='':
        continue
    if os.path.exists(trash+'/'+ext):
        shutil.move(trash+'/'+ file, trash+'/'+ext+ '/' +file)
    else:
        os.makedirs(trash+'/'+ext)
        shutil.move(trash+'/'+ file, trash+'/'+ext+ '/' +file)


