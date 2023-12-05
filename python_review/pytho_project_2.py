# first


def find_true_password():
    username = input("enter your username:")
    password = input("enter your password:")
    lusername = "admin"
    lpassword = "admin"
    if username == lusername:
        if password == lpassword:
            print("Successful Login")
        else:
            print("Incorrect Password")
    else:
        print("User Not found!")


find_true_password()


# second
def range_number():
    for i in range(1, 11):
        if i == 5:
            continue
        if i == 8:
            break
        print(i)


range_number()


# third
def remix_list(list1, list2):
    merged_list = list1 + list2
    final_list = list(set(merged_list))
    print(final_list[:3])


List_1 = [1, 2, 3, 4, 5]

List_2 = [4, 5, 6, 7, 8]

remix_list(list1=List_1, list2=List_2)
