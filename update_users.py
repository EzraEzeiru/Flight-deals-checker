import requests

# print("Welcome to Ezra's Flight Club")
# print("We find the best flight deals and email you")
# first_name = input("What is your first name?\n")
# last_name = input("What is your last name?\n")
# email = input("What is your email?\n").lower()
# confirm_email = input("Type your email again.\n").lower()

user_data = {
    "user": {
        "First Name": "Ezra",
        "Last Name": "Ezeiru",
        "Email": "ezeiru.ezra@gmail.com"
    }
}

sheety_header = {
       "Content-Type": "application/json"
}

# if email == confirm_email:
put_end_point = "https://api.sheety.co/06544ea584a763d682260465198ce764/copyOfFlightDeals/users"
response = requests.post(url=put_end_point, json=user_data, headers=sheety_header)
print(response.content)
print("You're in the club")
# else:
#     print("Check your email address for errors")
