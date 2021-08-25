def sum_complex(x , y ):
    result_calculation={}
    result_calculation['kamel'] = x["kamel"] + y["kamel"]
    result_calculation['mohomi'] = x["mohomi"] + y["mohomi"]
    return result_calculation
def sub_complex(x , y):
    result_calculation={}
    result_calculation["kamel"] = x ["kamel"] - y ["kamel"]
    result_calculation["mohomi"] = x ["mohomi"] - y ["mohomi"]
    return result_calculation
def mult_complex(x , y):
    result_calculation={}
    result_calculation["kamel"] = x["kamel"] * y["kamel"]
    result_calculation["mohomi"] = x["mohomi"] * y ["mohomi"]
    return result_calculation
def show_menu():
    print("1- sum number complex: ")
    print("2- sub number complex: ")
    print("3- mult number complex: ")
    print("4- exit: ")


choice= int(input("enter one choice for calculation : "))
if choice == 1:
    sum=sum_complex(a,m)
    print (sum)
elif choice == 2 :
    sub=sub_complex(a,m)
    print (sub) 
elif choice == 3:
    mul=mult_complex(a,m)
    print (mul )
elif choice == 4:
    exit()