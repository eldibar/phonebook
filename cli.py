import accounts, inspect, contacts, os;


def welcome_message():
    msg = "==============================\n";
    msg += "\t\t\tPHONEBOOK\n";
    msg += "==============================\n\n";
    msg += "Welcome to your personal phonebook!\n If you already have an account type login and just well.. log in ;)\n";
    msg += "Otherwise you can create new account by typing";
    msg += '\033[92m' + " cruser [login] [password]\n" + '\033[0m';
    msg += "To see list of available commands type help just after you log in and have fun!\n\n\n";
    return msg;


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
            os.system('cls' if os.name == 'nt' else 'clear');
            print(accounts.currAccount)
            contacts.phoneb = contacts.read_book(accounts.currAccount.login);
        else:
            print("Wrong password");


def account_login_ac(login):
    accounts.currAccount = accounts.Account(login);
    contacts.phoneb = contacts.read_book(accounts.currAccount.login);


def account_create(args):
    if len(args) != 2:
        print("Inappropriate number of arguments " + len(args) + " -- cruser [login] [password]");
        return;
    aclist = accounts.Accounts()
    aclist.read_list()
    if args[0] in aclist.list:
        print(args[0]+" -- that account already exists!")
        return
    acfile = open("accounts.txt", "a+");
    acfile.write(args[0] + "," + args[1]+"\n");
    acfile.close();
    os.makedirs(args[0]);
    bfile = open(args[0] + "/book.txt","w+");
    bfile.close()
    pfile = open(args[0]+"/permit.txt","w+");
    pfile.close()
    account_login_ac(args[0]);


def account_logout():
    accounts.currAccount = accounts.Account("None");


def show_user():
    print(accounts.currAccount);


def show_book(owner="self"):
    if owner == "self":
        contacts.print_book()
        return
    else:
        aclist = accounts.Accounts()
        aclist.read_list()
        if owner[0] not in aclist.list:
            print(owner[0]+" does not exist.")
            return
        elif owner in accounts.currAccount.permitList:
            contacts.phoneb = contacts.read_book(owner[0])
            contacts.print_book()
            contacts.read_book(accounts.currAccount.login)
            return
        else:
            print("You don't have permission to view "+owner[0]+"'s phonebook.")


def get_input():
    if accounts.currAccount.login == "None":
        comm = input("/>").split(" ");
        if comm[0] not in commandListLO:
            print(comm[0] + " - command not fount.");
            return;
    else:
        comm = input("@" + accounts.currAccount.login + "/>").split(" ");
        if comm[0] not in commandListLI:
            print(comm[0] + " - command not fount.");
            return;
    return comm;


def execute_command(command):
    if accounts.currAccount.login == "None":
        if len(command) == 1:
            commandListLO.get(command[0])();
        else:
            commandListLO.get(command[0])(command[1:]);
    else:
        if len(command) == 1:
            commandListLI.get(command[0])()
        else:
            commandListLI.get(command[0])(command[1:])


commandListLO = {
    "login": account_login,
    "cruser": account_create,
    "exit": quit,
};

commandListLI = {
    "logout": account_logout,
    "current": show_user,
    "cruser": account_create,
    "pwd": accounts.change_password,
    "show": show_book,
    "exit": quit,
};

if __name__ == "__main__":
    print(welcome_message());
    while True:
        command = get_input();
        execute_command(command);