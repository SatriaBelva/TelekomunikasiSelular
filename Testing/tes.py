import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

errors = {
    "username": ["Field must be between 2 and 30 characters long.", 'errors'],
    "email": ["Invalid email address."],
    "password1": ["Field must be at least 6 characters long."],
    "password2": ["Field must be equal to password1."]
}

errors_tuple = [
    ('username', ['Field must be between 2 and 30 characters long.', 'errors'],2), 
    ('email', ['Invalid email address.']), 
    ('password1', ['Field must be at least 6 characters long.']), 
    ('password2', ['Field must be equal to password1.'])
]

a = [
    ('danger', 'username: Username already exists. Please choose a different username',1), 
    ('danger', 'email: Email already exists. Please choose a different email',2), 
    ('danger', 'password1: Field must be at least 6 characters long.',3), 
    ('danger', 'password2: Field must be equal to password1.',4)
]

clear()
print(errors_tuple[0][-1])
# a = errors.items()
# print(a)
# for field,messages in errors.items():
#     print(f'{field.capitalize()}')
#     for message in messages :
#         print(f'- {message}')
#     print('')





