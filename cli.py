import accounts, inspect;


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
        else:
            print("Wrong password");

def account_login_ac(login):
    accounts.currAccount = accounts.Account(login);


def account_create(login,password):
    acfile = open("accounts.txt","a+");
    acfile.write(login + "," + password);
    account_login_ac(login);


def account_logout():
    accounts.currAccount = None;


def show_user():
    print(accounts.currAccount);


def get_input():
    if accounts.currAccount is None:
        command = input("/>").split(" ");
        if command[0] not in commandListLO:
            print(command[0] + " - command not fount.");
            return;
        return command;
    else:
        command = input("@"+accounts.currAccount.login+"/>").split(" ");
        if command[0] not in commandListLI:
            print(command[0] + " - command not fount.");
            return;
        return command;


def execute_command(command):
    commandListLO(command[0])();

commandListLO = {
    "login":account_login,
    "cruser":account_create,
};

commandListLI = {
    "logout":account_logout,
    "current":show_user
};


if __name__ == "__main__":
    command = get_input();
    commandListLO.get(command[0])();



