import requests
import kapital
import rhyme

with open('botId') as f:
    botId=f.read().rstrip()

chatId='-1001341864617'
chatId='-598658109'
message=kapital.getRandomSentence()
requests.get(f'https://api.telegram.org/bot{botId}/sendMessage?chat_id={chatId}&text={message}')
message=rhyme.getRhyme()
requests.get(f'https://api.telegram.org/bot{botId}/sendMessage?chat_id={chatId}&text={message}')
