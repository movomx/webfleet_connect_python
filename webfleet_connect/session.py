from connection import Connection

class Session:
  def __init__(self, credentials, config):
    self._credentials = credentials
    self._config = config
    self._connection = Connection()

  def has_json(self):
    return self.config.has_json()
  
  def _exec(self, action):
    return self._connection.exec(self._url(action))

  def _url(self, action):
    return f'{self._config}&{self._credentials}&{action}'
