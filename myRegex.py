import re

def PolishPhoneRegex():
    """
    Returns phone regex object
    for most of European area code
    """
    phoneRegex = re.compile(r'''(
        (\+)?(\d{2,3}|\((\+)?\d{2,3}\))?    # area code 
        (\s|-|\.)?                      # separator
        (\d{3})                         # first 3 digits
        (\s|-|\.)?                      # separator
        (\d{3})                         # second 3 digits
        (\s|-|\.)?                      # separator
        (\d{3})                         # last 3 digits
        )''', re.VERBOSE)
    
    return phoneRegex

def MailRegex():
    """
    Returns mail regex object
    for e-mail
    """
    mailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+               # user name
        @                               # @
        [a-zA-Z0-9.-]+                  # domain name
        (\.[a-zA-Z]{2,4})               # dot and anything
        )''', re.VERBOSE)
    
    return mailRegex