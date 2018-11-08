import accounts, functions;


def welcome_message():
    msg = "==============================\n";
    msg += "\t\t\tPHONEBOOK\n";
    msg += "==============================\n\n";
    msg += "Welcome to your personal phonebook!\n If you already have an account type login and just well.. log in ;)\n";
    msg += "Otherwise you can create new account by typing";
    msg += '\033[92m' + " cruser [login] [password]\n" + '\033[0m';
    msg += "To see list of available commands type help just after you log in and have fun!\n\n\n";
    return msg;


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
    "login": functions.account_login,
    "cruser": functions.account_create,
    "exit": quit,
};

commandListLI = {
    "logout": functions.account_logout,
    "current": functions.show_user,
    "cruser": functions.account_create,
    "pwd": functions.change_password,
    "show": functions.show_book,
    "add": functions.add_person,
    "exit": quit,
};

if __name__ == "__main__":
    print(welcome_message());
    while True:
        command = get_input();
        execute_command(command);