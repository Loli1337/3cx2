from requests import post
from sys import argv

url = 'https://discord.com/api/webhooks/996362386757926912/qt4taoKg1iFZZQA7ShtH1VmECjN983AJYwCEJM3bBJdK9TtMhOZ1KxvaX-NNZEdEuQd4' # Replace with your webhook URL

payload = {
    'content': argv
}

response = post(url, json=payload)
