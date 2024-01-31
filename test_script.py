from webfleet_connect.webfleet_connect_response import WebfleetConnectResponse
from webfleet_connect.format_handlers.json_response_parser import JsonResponseParser
from webfleet_connect.format_handlers.csv_response_parser import CsvResponseParser
from webfleet_connect.session import Session
from webfleet_connect.credentials import Credentials
from webfleet_connect.config import Config
from session import create



params = {
    'account': 'rogermartin',
    'username': 'Clugand',
    'password': 'RM-21-geoloc',
    'apikey': 'a00ab50e-32db-41f3-bfe8-c436a920ab7b'
}

session = create(params)

response = session.show_object_report_extern()

print("Statut de la réponse:", response.status_code())
print("URL de la requête:", response.url())
print("Contenu de la réponse:")
print(response.to_dataframe()) 