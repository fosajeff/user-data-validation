import random
import string


def get_user_details(user_data):
    print("\n---------------------------------------")
    print("\t   User Accounts")
    print("-----------------------------------------")

    # iterate over the list range and users

    for (id, user) in zip(range(len(user_data)), user_data):
        print(
            f"\nUser {id}:\t   {user['first_name']} {user['last_name']}\nEmail:\t   {user['email']}\nPassword:  {user['password']}"
        )
    print("-----------------------------------------")

    return None


def generate_password(first_name, last_name):
    choices = string.ascii_letters + string.digits + string.punctuation

    # generate 5 random characters
    random_string = "".join(random.sample(choices, 5))

    password = first_name[:2] + last_name[-2:] + random_string
    return password


def get_user_password():
    while True:
        print("Enter your password (password must be seven characters or more)\n")
        password1 = input(": ")
        if len(password1) >= 7:
            print("Confirm password\n")
            password2 = input(": ")
            if password1 == password2:
                break
            print("Password does not match")
            continue
        print("Password must be seven characters or more")
        continue
    return password1


def user_registration():
    user_list = []
    while True:
        user_first_name = input("\nFirstname: ")
        user_last_name = input("Lastname: ")

        # make first letter of names uppercase and others lower

        first_name = (user_first_name[0].upper() + user_first_name[1:].lower()).strip()
        last_name = user_last_name[0].upper() + user_last_name[1:].lower()

        email = input("Email: ").lower()

        temp_password = generate_password(first_name, last_name)
        user_choice = input(
            f"Do you want your password to be {temp_password} [y/N]  : "
        )
        if user_choice.lower() == "y":
            password = temp_password
        else:
            password = get_user_password()

        print(f"\nAccount for {first_name} {last_name} created successfully\n")
        user = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
        }
        user_list.append(user)
        add_again = input("Do you want to add another user? [y/N] : ")
        if add_again.lower() == "y":
            continue
        break
    return get_user_details(user_list)


def main():
    print("*** HNG Tech ***")
    print("Welcome admin, create new users")

    user_registration()


main()

