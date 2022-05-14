class DatabaseConnection:
    def __int__(self):
        ...

    @staticmethod
    def start():
        print('> [database] Starting...')
        print('> [database] Connecting to Postgres...')
        print('> [database] Running migrations...')
        print('> [database] Starting done!')

    @staticmethod
    def stop():
        print('> [database] Stopping...')
        print('> [database] Closing to Postgres connection...')
        print('> [database] Stopping done!')
