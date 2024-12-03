with open ("test.txt" , "r") as file:
    line = int(input("line = "))
    for i in range(line):
        content = file.readline()
    print(content)
    print("========================")
with open ("test.txt" , "r") as file:
    a = file.readlines()
    for i in a:
        print(i)