#! python 3
# phone_mail.py - the program looks up phone numbers and e-mail addresses 
# in the user's clipboard, then copy output data to user's clipboard.

import pyperclip
import areaCode
import myRegex

# Search for matches in the clipboard
text = str(pyperclip.paste())
area_code = areaCode.areaCode()
matches = []

for groups in myRegex.PolishPhoneRegex().findall(text):
    phoneNum = '-'.join([area_code, groups[5], groups[7], groups[9]])
    matches.append(phoneNum)
for groups in myRegex.MailRegex().findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    result = '\n'.join(matches)
    pyperclip.copy(result)
    print(f'Copied do clipboard:\n{result}\n')
else:
    print('No phone number or e-mail address found.')
    print('Are you sure you copied text correctly?\n')
