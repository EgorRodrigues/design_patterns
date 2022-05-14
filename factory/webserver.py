class Webserver:
    def __int__(self):
        ...

    @staticmethod
    def start():
        print('> [webserver] Starting...')
        print('> [webserver] Waiting for port to be available...')
        print('> [webserver] Starting done!')

    @staticmethod
    def stop():
        print('> [webserver] Stopping...')
        print('> [webserver] Gracefully waiting for all clients...')
        print('> [webserver] Close all ports...')
        print('> [webserver] Stopping done!')
