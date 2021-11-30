
import re
def validateEmail(email):
    regex = '^[a-z0-9](\.?[a-z0-9]){5,}@gmail\.com$'
    if re.match(regex,email):
        return True
    else:
        return False

# e =validateEmail('sure@gmail.com')


def mailSendOtp(email,otp,message):
    try:
        print("call function mail",email,otp,message)
        return True
    except:
        return False
