# #FILE HANDLEING

# #CREATE FILE
# # f=open("filename.extension", "w")
# # f.write("your msg")
# # f.close()

# # write data into file : Syntax
# # f=open("filename.ext","w")
# # f.write("your msgg")
# # f.close()

# # read data from  file : Syntax
# # f=open("filename.ext","r")
# # f.read()

# # delete file : Syntax
# # import os 
# # os.remove("filename.ext")


# # check file exist or not : Syntax
# # import os 
# # os.path.exists("filename.ext")



# #to open the file
f=open("hansi.txt", "w")

# #to write in the file
f.write("WHY TF R U HERE BITCH?!")

# #TO CLOSE THE FILE
f.close()

# #READ DAta from file
readFile=open("hansi.txt","r")
print(readFile.read())

#DELETE FILE
#import os
#os.remove("hansi.txt")