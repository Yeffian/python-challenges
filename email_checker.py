import re

def personal_info_checker(personal_info):
    length = len(personal_info) <= 64
    # print(length)
    # return bool(re.match(r"^[a-zA-Z0-9!#$%&'*+\-\/=?^_`{|}~]+$", personal_info)) and length
    return personal_info.isascii() and length

def domain_name_checker(domain):
    if '.' not in domain:
        return False

    length = len(domain) <= 253
    domain_parts = domain.split('.')
    return domain_parts[0].isascii() and domain_parts[1].isascii() and length
    
def check_email(email):
    parts = email.split('@')
    return personal_info_checker(parts[0]) and domain_name_checker(parts[1])


print(check_email('adit.chakraborty2009@gmail.com'))