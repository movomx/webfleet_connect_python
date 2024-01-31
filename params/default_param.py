from .param import Param
from .default_param import webfleet_connect


class DefaultParam(Param):

    params = {
        'account': 'rogermartin',
        'username': 'username',
        'password': 'my-pswd',
        'apikey': 'my api'
        }
    
    config = {
        'lang' : 'en',
        'format' : 'csv',
        'useUTF8' : 'true'
        }
    
    params =config
    

    
    wc = webfleet_connect.create(params)
