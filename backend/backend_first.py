import csv


reg = input('1. Login'
                '\n2. Register'
                '\n3. Log Out \n__')

if reg == '3':
    print('out')


def check_name(name):
    with open("names.csv","r") as f:
        users = f.read().splitlines()
        for user in users:
            args = user.split(",")

        while True:
            if args[0] == name:

                break
            else:
                print('Its not right, plz rewrite ur name')




def check_email(email):
    with open("names.csv","r") as f:
        users = f.read().splitlines()
        for user in users:
            args = user.split(",")
        while True:
            if args[2] == email:

                break
            else:
                print('Its not right, plz rewrite ur name')



def check_password(password):
    with open("names.csv","r") as f:
        users = f.read().splitlines()
        for user in users:
            args = user.split(",")
        while True:
            if args[1] == password:

                break
            else:
                print('Its not right, plz rewrite ur name')




while reg == '1':

    in_name = input('Ur name:')
    in_email = input('Ur email:')
    in_password = input('Ur password:')

    if check_name(in_name):
        pass
    elif check_email(in_email):
        pass
    elif check_password(in_password):
        pass
    else :
        print('U successfully enter')

    print(f'U successfully enter to ur account {in_name}\n*********Hello*World***********')

    # in_name = input('Ur name:')
    # if check_name(in_name):
    #     print('a')
    # else :
    #     continue
    #
    # in_email = input('Ur email:')
    # if check_email(in_email):
    #     print('a')
    # else:
    #     continue
    #
    # in_password = input('Ur password:')
    # if check_password(in_password):
    #     print('a')
    # else :
    #     continue



    break


while reg == '2':
    name = input('Ur name:\n')

    if not name.isalpha():
        print('Dont write numbers or probels')
        continue
    email = input('Ur email:')
    if '@' not in email:
        print('Email must have "@"')
        continue

    password = input('Ur password:')
    if len(password) < 6:
        print('Ur password must have more than 6 symbols!')
        continue

    card = input('Ur card:')

    if len(card) != 16 :
        print('Card must include 16 numbers, no more')
        continue
    print('User is appended successfully')

    while True:
        try:
            money = int(input('how much money u want to donate:'))
        except ValueError:
            print('Only numbers')
            continue
        break




    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Password', 'Email', 'Money']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow(
            {f'Name': f'{name}', 'Password': f'{password}', 'Email': f'{email}', 'Money': f'{money}'})
    break



while reg == '2':
    main_menu = input('Okay, choose option'
                 '\n    1.shop'
                 '\n    2.balance'
                     '\n    3.Out\n__')

    if main_menu == '1' :
        print('1. GTA 5 -> 10$'
                  '\n2. Detroit: Become Human -> 8$')
        choose_game = input('__')
        gta = 10
        detroit = 8
        if choose_game == '1':
            print('U sure that u want to buy GTA 5'
                  '\n1.yes'
                  '\n2.no'
                  f'\n                                                 (ur balance is: {money})')
            gta_choose_yes_no = input('__')
            if gta_choose_yes_no == '1' and money >= gta:
                print('U successfully bought the product')
                result = money - gta
                print(f'Money left: {result}')

            elif gta_choose_yes_no != '1':
                print('U cancelled the purchase')
                continue
            else :
                print('Unfortunately, u dont have 10$ in ur balance')
        elif choose_game == '2':
            print('U sure that u want to buy Detroit'
                  '\n1.yes'
                  '\n2.no'
                  f'\n                                                 (ur balance is: {money})')
            detroit_choose_yes_no = input('__')
            if detroit_choose_yes_no == '1' and money >= gta:
                print('U successfully bought the product')
                result = money - detroit
                print(f'Money left: {result}')

            elif detroit_choose_yes_no != '1':
                print('U cancelled the purchase')
                continue
            else :
                print('Unfortunately, u dont have 8$ in ur balance')
    elif main_menu == '2':
        print(f'Ur balance is {money}')
    elif main_menu == '3':
        break









