products = {
    "water(500mm)" : 5000,
    "cola(250mm)" : 12000,
    "water(1500mm)" : 20000,
    "cola(1500mm)" : 35000,
    "milk(small)" : 6500,
    "milk(big)" : 20000,
    "cake" : 35000
}

class Product:
    total = 0
    factor = ''
    def add_product(name,last_name,total,factor):
        with open(f"{name}_{last_name}.txt" , "w")as file:
            file.write(f"name = {name}\nlast name = {last_name}")
        p_name = products.items()
        p = str(p_name)
        p = p.replace("dict_items([('water(500mm)', 5000), ('cola(250mm)', 12000), ('water(1500mm)', 20000), ('cola(1500mm)', 35000), ('milk(small)', 6500), ('milk(big)', 20000), ('cake', 35000)])",
                "======================\n|water(500mm) = 5000T|\n|cola(250mm) = 12000|\n|water(1500mm) = 20000|\n|cola(1500mm) = 35000|\n|milk(small) = 6500|\n|milk(big) = 20000|\n|cake = 35000|\n======================")
        print(p)
        c = 0
        while c == 0:
            try:
                add = str(input("enter your products name with ',' : "))
                add = add.replace("," , " ")
                add = add.split()
                a = 0
                for i in add:
                    i = add[a]
                    total += products[i]
                    # factor.append(f"{a+1}. {i} => {products[i]}T\n")
                    factor[i] = (products[i])
                    a += 1
                    c += 1
                break
            except KeyError:
                print("invalid option!")
    def remove_product(total,factor):
        while True:#remove!!
                if total == 0:
                    try:
                        remove = str(input("enter the items you want to remove(if they are mor than1,write them with ',') : "))
                        remove = remove.replace("," , " ")
                        remove = remove.split()
                        a = 0
                        for i in remove:
                            i = remove[a]
                            a += 1
                            total -= products[i]
                            # factor.pop(f"{a+1}. {i} => {products[i]}T\n")
                            factor.pop(i)
                        break
                    except KeyError:
                        print("invalid option!")
                else :
                    print("you didn't buy anything yet!")
                    break
