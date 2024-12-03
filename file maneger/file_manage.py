import os

class FileMainpulator:
    def read(f_name,read_option):
        with open(f"{f_name}.txt" , "r") as file:
            if read_option == 1:
                    line = int(input("line = "))
                    for i in range(line):
                        content = file.readline()
                    print(content)
            elif read_option == 2:
                content = file.readline()
                for i in range(line):
                    content = file.readline()
                    print(content)
    def write(f_name,value):
        with open(f"{f_name}.txt" , "a") as file:
            file.write(value)
    def newFolder(folder_name):
        os.makedirs(folder_name)
    def remove(remove):
        os.remove(remove)
    def file_exist(file_name):
        try:
            with open(f"{file_name}.txt" , "r") as file:
                a = file.readline()
            print("file exist!")
        except FileNotFoundError:
            print("file not exist here!")
    def copy(first,where):
        with open(f"{first}.txt" , "r") as file:
            a = file.readlines()
            for i in a:
                with open(f"{where}.txt" , "a") as file:
                    file.write(i)
while True:
    try:
        option = int(input("options:\n\t1) read\n\t2) write\n\t3) new_folder\n\t4) remove\n\t5) exist or not\n\t6)copy\n\t7) exit\n"))
        if option == 1:
            f_name = input("please enter file name: ")
            try:
                read_option = int(input("options:\n\t1) line by line\n\t2) all line\n"))
                FileMainpulator.read(f_name,read_option)
            except ValueError:
                print("invalid option")
        elif option == 2:
            f_name = input("enter file name: ")
            value = str(input("enter the text: "))
            FileMainpulator.write(f_name,value)
        elif option == 3:
            folder_name = input("enter folder name thst you want to add: ")
            FileMainpulator.newFolder(folder_name)
        elif option == 5:
            try:
                remove = input("enter the file name that you want to remove: ")
                FileMainpulator.remove(remove)
            except FileNotFoundError:
                print("file not found!")
        elif option == 5:
            file_name = input("enter file name: ")
            FileMainpulator.file_exist(file_name)
        elif option == 6:
            first_fName = input("enter the file that you want to copy: ")
            where = input("where do you want to copy: ")
            FileMainpulator.copy(first_fName,where)
        elif option == 7:
            print("good bye!")
            break
    except ValueError:
        print("invalid option")