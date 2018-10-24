import accounts;


def account_login():
    aclist = accounts.Accounts();
    aclist.read_list();

    login = input("Login: ");
    password = input("Password: ");

    if login not in aclist.list:
        print("Account: " + login + " does not exist.\n");
    else:
        if aclist.list[login] == password:
            currAccount = accounts.Account(login);
        else:
            print("Wrong password");


def get_input():
    if accounts.currAccount is None:
        pass;

commandListLO = {
    "login":account_login,
    "cruser":account_create,
}



