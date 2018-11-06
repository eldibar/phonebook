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


def change_password(args):
    aclist = Accounts()
    aclist.read_list()
    if aclist.list[currAccount.login] == args[0]:
        aclist.list[currAccount.login] = args[1]
        acfile = open("accounts.txt","w")
        for key, value in aclist.list.items():
            acfile.write(key + ","+value+"\n")
        return
    else:
        print("Wrong password!\n")
        return


currAccount = Account("None");