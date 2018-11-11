class Account:
    def __init__(self,login):
        self.login = login;
        self.permitList = [];

    def __str__(self):
        stri = "You are logged in as " + self.login + "\n";
        return stri;

    def read_permit(self):
        pfile = open(self.login+"/"+"permit.txt","r")
        content = pfile.read().splitlines();
        for item in content:
            self.permitList.append(item)


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


currAccount = Account("None");