import accounts,os

class Person:
    def __init__(self,fname,lname,number,adress = ""):
        self.fname = fname;
        self.lname = lname;
        self.number = number;
        self.adress = adress;

    def __str__(self):
        stri = "Name: " + self.fname + "\nLast Name: " + self.lname + "\nNumber: " + self.number + "\n";
        if self.adress != "":
            stri += "Adress: " + self.adress + "\n";
        return stri;


class PhoneBook:
    def __init__(self):
        self.contacts = [];

    def __str__(self):
        stri = "";
        for person in self.contacts:
            stri += str(person) + "\n";
        return stri;


def show_book():
    print(phoneb);
    return;

def read_book(owner=accounts.currAccount.login):
    if not os.path.exists(owner):
        os.makedirs(owner);
    bfile = open(owner+"/book.txt","r+");
    content = bfile.read().splitlines();
    bfile.close();
    phoneb = PhoneBook();
    for line in content:
        contact = line.split(",");
        if len(contact) == 3:
            phoneb.contacts.append(Person(contact[0],contact[1],contact[2]))
        else:
            phoneb.contacts.append(Person(contact[0], contact[1], contact[2],contact[3]));
    return phoneb;


phoneb = PhoneBook();