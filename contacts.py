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



