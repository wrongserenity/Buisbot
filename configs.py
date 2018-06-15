# token here
TOKEN = '419143379:AAFMAMFerBxUajJfsCv_q6GpBFYG4od93DA'
BOTNAME = 'BuisnessLessonsBot'
URL = "https://t.me/"+BOTNAME+'?start='
LINK = "https://t.me/"+BOTNAME

WEBHOOK_HOST = '185.159.128.139'                   # Write your host's IP
WEBHOOK_PORT = 443              # 443, 80, 88 or any free port
WEBHOOK_LISTEN = '185.159.128.139'          # Sometimes may need to write your host's IP again

WEBHOOK_SSL_CERTIFICATE = 'webhook_cert.pem'  # Path to the ssl certificate
WEBHOOK_SSL_PRIVATE_KEY = 'webhook_pkey.pem'  # Path to the ssl private key
WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % TOKEN
WEBHOOK_URL_BASE2 = "http://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)

db_configs = dict(user='postgres', host='localhost', port='5432', password='89/b/3?!MK', database='postgres')
mongo_configs = dict(host='localhost', port=27017, name='test-database')
