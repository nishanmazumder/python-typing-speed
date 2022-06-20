email = 'test@test.com'


# validation = {
#     '@': True if '@' in email and email.count('@') == 1 else False,
#     '.': True if '.' in email and ((email[-3] == '.') ^ (email[-4] == '.')) else False,
#     'space': [x for x in email if x == x.isspace()]
# }

email_space = 0

validation = {
    '@': True if '@' in email and email.count('@') == 1 else False,
    '.': True if '.' in email and ((email[-3] == '.') ^ (email[-4] == '.')) else False,
}

if len(email) >= 6:  # 1
    if email[0].isalpha():  # 2
        if (validation.get('@') and validation.get('.')) == True:
            for x in email:
                if x == x.isspace():
                    email_space = 1
            print(email_space)
        else:
            print("wrong email 3!")
    else:
        print("wrong email 2!")
else:
    print("wrong email 1!")


# Package: https://pypi.org/project/email-validator/

# from email_validator import (
#     validate_email,
#     EmailNotValidError
# )

# try:
#     # Check whether email is valid. If it is not, will throw an exception
#     valid_result = validate_email('sad@gmail.com')
#     # if valid_result:
#     #     print('done!')
#     # else:
#     #     print('failed!')

#     print('done')

# except EmailNotValidError as e:
#    # Email not valid. This will be an EmailSyntaxError if the form of the address is invalid or an EmailUndeliverableError if the domain does not resolve.
#     print(str(e))
