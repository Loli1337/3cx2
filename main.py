from requests import post
from sys import argv
url = 'https://api.telegram.org/bot5113940874:AAFDT9PN52fIlKbbOWmtF9DF503sde-9P0M/sendMessage'
if {argv[1]} == '1001':
    telegram_id = '5280692596'
elif {argv[1]} == '1002':
    telegram_id = '1197549044'
elif {argv[1]} == '1003':
    telegram_id = '685382438'
elif {argv[1]} == '1004':
    telegram_id = '5368332363'
elif {argv[1]} == '9998':
    telegram_id = '1907961854'
data = {
    'chat_id': '-1001767516513',
    'text': f'{telegram_id}\n{argv[2]}'
}
post(url, json=data)
