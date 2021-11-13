
import re
def validateEmail(email):
    regex = '^[a-z0-9](\.?[a-z0-9]){5,}@gmail\.com$'

    if re.match(regex,email):
        return True
    else:
        return False

e =validateEmail('sure@gmail.com')

print(e)