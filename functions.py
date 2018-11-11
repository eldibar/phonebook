import contacts, accounts, os


def print_book():
    print(contacts.phoneb);
    return;


def read_book(owner):
    if not os.path.exists(owner):
        os.makedirs(owner);
    bfile = open(owner+"/book.txt","r+");
    content = bfile.read().splitlines();
    bfile.close();
    phoneb = contacts.PhoneBook();
    for line in content:
        contact = line.split(",");
        if len(contact) == 3:
            phoneb.contacts.append(contacts.Person(contact[0],contact[1],contact[2]))
        else:
            phoneb.contacts.append(contacts.Person(contact[0], contact[1], contact[2],contact[3]));
    return phoneb;


def show_book(owner="self"):
    if owner == "self":
        print_book()
        return
    else:
        aclist = accounts.Accounts()
        aclist.read_list()
        if owner[0] not in aclist.list:
            print(owner[0]+" does not exist.")
            return
        elif owner[0] in accounts.currAccount.permitList:
            contacts.phoneb = read_book(owner[0])
            print_book()
            contacts.phoneb = read_book(accounts.currAccount.login)
            return
        else:
            print("You don't have permission to view "+owner[0]+"'s phonebook.")


def allow(person):
    aclist = accounts.Accounts()
    aclist.read_list()
    if person[0] not in aclist.list:
        print(person[0] + " does not exist.")
        return
    else:
        pfile = open(person[0]+"/"+person[0]+".txt","r")
        permitlist = pfile.read().splitlines()
        pfile.close()
        permitlist.append(accounts.currAccount.login)
        pfile = open(person[0]+"/permit.txt","w")
        for login in permitlist:
            pfile.write(login+"\n")
        pfile.close()
        print(person[0]+" was granted access to your book.\n")


def revoke(person):
    aclist = accounts.Accounts()
    aclist.read_list()
    if person[0] not in aclist.list:
        print(person[0] + " does not exist.")
        return
    else:
        pfile = open(person[0] + "/permit.txt", "r")
        permitlist = pfile.read().splitlines()
        pfile.close()
        print(permitlist)
        for login in permitlist:
            if login == accounts.currAccount.login:
                permitlist.remove(login)
        print(permitlist)
        pfile = open(person[0] + "/permit.txt", "w")
        for login in permitlist:
            pfile.write(login + "\n")
        pfile.close()
        print(person[0] + " has no access to your book.\n")



def add_person():
    fname = input("Name: ")
    lname = input("Last name: ")
    number = input("Number: ")
    adress = input("Address(optionel): ")
    contacts.phoneb.contacts.append(contacts.Person(fname,lname,number,adress))
    save_book()
    return


def save_book():
    bfile = open(accounts.currAccount.login+"/book.txt","w+")
    for person in contacts.phoneb.contacts:
        if person.adress != "":
            bfile.write(person.fname+","+person.lname+","+person.number+","+person.adress+"\n")
        else:
            bfile.write(person.fname+","+person.lname+","+person.number+"\n")
    bfile.close()


def account_login():
    aclist = accounts.Accounts();
    aclist.read_list();

    login = input("Login: ");
    password = input("Password: ");

    if login not in aclist.list:
        print("Account: " + login + " does not exist.\n");
    else:
        if aclist.list[login] == password:
            accounts.currAccount = accounts.Account(login);
            accounts.currAccount.read_permit()
            print(accounts.currAccount.permitList)
            os.system('cls' if os.name == 'nt' else 'clear');
            print(accounts.currAccount)
            contacts.phoneb = read_book(login);
        else:
            print("Wrong password");


def account_login_ac(login):
    accounts.currAccount = accounts.Account(login);
    contacts.phoneb = read_book(accounts.currAccount.login);


def account_create(args):
    if len(args) != 2:
        print("Inappropriate number of arguments " + len(args) + " -- cruser [login] [password]");
        return;
    aclist = accounts.Accounts()
    aclist.read_list()
    if args[0] in aclist.list:
        print(args[0] + " -- that account already exists!")
        return
    acfile = open("accounts.txt", "a+");
    acfile.write(args[0] + "," + args[1] + "\n");
    acfile.close();
    os.makedirs(args[0]);
    bfile = open(args[0] + "/book.txt", "w+");
    bfile.close()
    pfile = open(args[0] + "/permit.txt", "w+");
    pfile.close()
    account_login_ac(args[0]);


def account_logout():
    accounts.currAccount = accounts.Account("None");


def show_user():
    print(accounts.currAccount);


def change_password(args):
    aclist = accounts.Accounts()
    aclist.read_list()
    if aclist.list[accounts.currAccount.login] == args[0]:
        aclist.list[accounts.currAccount.login] = args[1]
        acfile = open("accounts.txt","w")
        for key, value in aclist.list.items():
            acfile.write(key + ","+value+"\n")
        return
    else:
        print("Wrong password!\n")
        return
