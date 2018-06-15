import random
import string
import cherrypy
from configs import *


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="generate">
              <input type="text" value="8" name="length" />
              <button type="submit">Give it now!</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))


cherrypy.config.update({
        'server.ssl_module': 'builtin',
        'server.ssl_certificate': WEBHOOK_SSL_CERTIFICATE,
        'server.ssl_private_key': WEBHOOK_SSL_PRIVATE_KEY,
        'server.socket_host': WEBHOOK_LISTEN,
        'server.socket_port': WEBHOOK_PORT,
    })



cherrypy.quickstart(StringGenerator())