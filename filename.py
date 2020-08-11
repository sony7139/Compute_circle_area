filename=input("Enter the file name: ")
file_extnsns={"python":".py","C":".c","java":".java","C++":".cpp"}
for i in file_extnsns:
    if file_extnsns[i] in filename:
        print("The type of file is " + i)

    
