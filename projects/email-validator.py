import re

email = 'test@test.com'

# Regex
email_condition = '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
# email_condition = '^[a-z 0-9]+(?:[._][a-z0-9]+)*@(?:\w+\.)+\w{2,3}$' // https://regex101.com/r/UxYi3A/1

if re.search(email_condition, email):
    print('Success!')
else:
    print("wrong email!")


# Manual
# validation = {
#     '@': True if '@' in email and email.count('@') == 1 else False,
#     '.': True if '.' in email and ((email[-3] == '.') ^ (email[-4] == '.')) else False
# }

# if len(email) >= 6 and ' ' not in email:  # 1
#     if email[0].isalpha():  # 2
#         if (validation.get('@') and validation.get('.')) == True:
#            print('Success!')
#     else:
#         print("wrong email 2!")
# else:
#     print("wrong email 1!")




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
