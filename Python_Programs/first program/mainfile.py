import os # imports os file
# r is rowstring it keeps the string as it is.

#first folder
picPath=r"C:\Users\AIJAZ\Desktop\PYTHON\Python_Programs\first program\pics"
pics=os.listdir(picPath)

#second folder
picPath2=r"C:\Users\AIJAZ\Desktop\PYTHON\Python_Programs\first program\pics2"
pics2=os.listdir(picPath2)


for pic in pics:
    if pic in pics2:
        commonPic=os.path.join(picPath2,pic)
        os.remove(commonPic)
