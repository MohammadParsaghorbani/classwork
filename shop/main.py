#start
#import
from function import *

name = input("enter your name: ")
last_name = input("enter your last name: ")
total = 0
factor = {}

while True:
    option = int(input("=================\n\t1. add product\n\t2. remove product\n\t3. check the factor\n\t4. exit\n"))
    if option == 1:
        Product.add_product(name,last_name,total,factor)
    elif option == 2:
        Product.remove_product(total,factor)
    elif option == 3:
        if factor == "":
            print("at first you must by something")
            Product.add_product(name,last_name,total,factor)
        else:
            num = 1
            print("ok...")
            for key , value in factor.items():
                print(f"{num}. {key} => {value} T")
                num += 1
    elif option == 4:
        print("good bye!")
        with open(f"{name}_{last_name}.txt" , "a") as file:
            a = 1
            for key , value in factor.items():
                file.write(f"\n\t{a}. {key} => {value} T")
                a += 1
            if total >= 200000:
                total= total * 20 /100
                print(f"total price with discount = {total}")
            elif total >= 400000:
                total = total * 40 /100
                print(f"total price with discount = {total}")
            if total >= 600000:
                total= total * 60 /100
                print(f"total price with discount = {total}")
            file.write(f"total price => {total} T")
        break