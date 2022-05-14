from factory.database import DatabaseConnection
from factory.webserver import Webserver

"""
Criada uma injeção de dependencia na classe CreateCore,
facilitando os testes
"""


class CreateCore:
    def __init__(
            self,
            database_connection: DatabaseConnection = DatabaseConnection(),
            webserver: Webserver = Webserver()
    ):
        self.database_connection = database_connection
        self.webserver = webserver

    def start(self):
        print('> [core] Starting...')
        self.database_connection.start()
        self.webserver.start()
        print('> [core] Starting done! System running!')

    def stop(self):
        print('> [core] Stopping...')
        self.webserver.stop()
        self.database_connection.stop()
        print('> [core] Stopping done!')
