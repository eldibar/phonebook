import accounts, inspect,contacts,os;


def welcome_message():
    msg = "==============================\n";
    msg += "\t\t\tPHONEBOOK\n";
    msg += "==============================\n\n";
    msg += "Welcome to your personal phonebook!\n If you already have an account type login and just well.. log in ;)\n";
    msg += "Otherwise you can create new account by typing";
    msg += '\033[92m'+" cruser [login] [password]\n" + '\033[0m';
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
        print("Inappropriate number of arguments "+len(args)+" -- cruser [login] [password]");
        return;
    acfile = open("accounts.txt","a+");
    acfile.write("\n"+args[0] + "," + args[1]);
    account_login_ac(args[0]);


def account_logout():
    accounts.currAccount = "None";


def show_user():
    print(accounts.currAccount);


def get_input():
    if accounts.currAccount.login == "None":
        comm = input("/>").split(" ");
        if comm[0] not in commandListLO:
            print(comm[0] + " - command not fount.");
            return;
    else:
        comm = input("@"+accounts.currAccount.login+"/>").split(" ");
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
        commandListLI.get(command[0])();


def exit():
    exit();


commandListLO = {
    "login":account_login,
    "cruser":account_create,
    "exit": quit,
};

commandListLI = {
    "logout":account_logout,
    "current":show_user,
    "cruser": account_create,
    "show": contacts.show_book,
    "exit": quit,
};


if __name__ == "__main__":
    print(welcome_message());
    while True:
        command = get_input();
        execute_command(command);


