import requests
import kapital

botId=open('botId').read()
chatId='-1001341864617'
message=kapital.getRandomSentence()
requests.get(f'https://api.telegram.org/bot{botId}/sendMessage?chat_id={chatId}&text={message}')
