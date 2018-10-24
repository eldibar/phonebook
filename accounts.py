class Account:
    def __init__(self,login):
        self.login = login;
        self.permitList = [];

    def __str__(self):
        stri = "You are logged in as " + self.login + "\n";
        return stri;


class Accounts:
    def __init__(self):
        self.list = {};

    def read_list(self):
        acfile = open("accounts.txt", "r");
        content = acfile.read().splitlines();
        acfile.close();
        for line in content:
            acc = line.split(",");
            self.list[acc[0]] = acc[1];
        content.clear();


aclist = Accounts();
aclist.read_list();

login = input("Login: ");
password = input("Password: ");

if login not in aclist.list:
    print("Account: " + login + " does not exist.\n");
else:
    if aclist.list[login] == password:
        currAccount = Account(login);
    else:
        print("Wrong password");

command = input(">");
if command == "current":
    print(currAccount);
