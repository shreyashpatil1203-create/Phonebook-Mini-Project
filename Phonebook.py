# ContactFlow: The Smart Contact Management System

Contact = {
    "Rana"   :  9155556814,
    "Ganesh" :  9363820961,
    "Rohit"  :  7510923407,
    "Sandy"  :  9834658216,
    "Rahul"  :  7730727120,
}

print("Here is your contact")

print("Rana : Phone_no9155556814 \nGanesh : Phone_no9363820961 \nRohit : Phone_no7510923407 \nSandy : Phone_no9834658216 \nRahul : Phone_no7730727120")

user = input("Enter Your Contact:-")
if user in Contact:
    print(f"Your Contact :-{user} Is Prasent In Phonebook ")
else:
    print("Your Contact Not Prasent In Phonebook")

new_user = input("Enter Your Second Contact :-") 
Phone_no = 9788327683

if new_user not in Contact:
    Contact[new_user] = Phone_no
    print(f"Added : {new_user} Phone_no:-{Phone_no}")
else:
    print(f"Error : {new_user} Already Existed")