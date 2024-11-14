import random , string                    

upper = string.ascii_uppercase
lower = string.ascii_lowercase
numbers = string.digits
charz = string.punctuation

all_charters = upper + lower + numbers + charz 

password = ""

lenght = int(input("please enter your lenght of password: "))

def add_num():
    return random.choice(all_charters)

for x in range(lenght):
    password += add_num()

print("your password is: ",(password))