# 'r'-> read-only (we need to create txt file)
# 'w'->write-only(creates txt file and writes message)
# 'a'->append
# 'r+'->read+write(file must exist)
# 'w+'->write+read
# 'a+'->append+read
# 'rb'-> read binary
# 'wb'-> write binary
# 'ab'->append binary



# file=open("filename.txt","w")
# file.write("hello world!\n")
# file.write("This is a new file.\n")

# file=open("notes.txt","r")
# content=file.read()
# print("File content:\n",content)
# file.close()

# file=open("notes.txt","a")
# file.write("\nAdding a new line\n")
# file.close()

# it will print in terminal
# with open("notes.txt","r") as f:
#     for line in f:
#         print(line.strip())

# writing a log-user feedback will append
# feedback=input("Enter your feedback : ")
#
# with open("feedback.txt","a") as log:
#     log.write(feedback+"\n")
# print("Thanks! your feedback is saved")

# readline is used to read line by line
# with open("data.txt","r") as f:
#     print(f.readline().strip()) #first line

# with open("data.txt","r") as f:
#     for line in f:
#         print(line.strip())

# with open("file.txt") as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         if "ERROR" in line:
#             print(line.strip())

#it will print first 10 lines from the text file (_ throw away variable)
# limit is a pagination
# with open("file.txt") as file:
#     for _ in range(10):
#         print(file.readline().strip())

# from one file to another file
# with open("input_file.txt","r") as f, open("output_file.txt","w") as g:
#     for line in f:
#         print(line.strip())
#         g.write(line)




