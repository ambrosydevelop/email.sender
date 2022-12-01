class GetItems():
    @classmethod
    def get_user_account(self) -> list:
        """Get user accounts of gmail"""
        try:
            with open('data/accounts.txt','r') as f:
                return [x.split(':') for x in f.readlines()] # Split on email and special password for apps
        except FileNotFoundError:
            print('ERROR [File not found "accounts.txt"]')
    @classmethod
    def get_adress(self) -> list:
        """Get email adresses"""
        try:
            with open('data/adresses.txt','r') as f:
                return [x for x in f.readlines()] 
        except FileNotFoundError:
            print('ERROR [File not found "adresses.txt"]')
