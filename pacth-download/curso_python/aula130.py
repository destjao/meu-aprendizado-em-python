class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.passoword = None


    def set_user(self, user):
        self.user = user
        
    def set_password(self, passoword):
        self.passoword = passoword

    @classmethod
    def crated_user_auth(cls, user, passoword):
        connection = cls()
        connection.user = user
        connection.password = passoword
        return connection
    
    @staticmethod
    def soma(x, y):
        return x + y

c1 = Connection.crated_user_auth('Luiz', '1234')
print(c1.user)
print(c1.passoword)

# c1 = Connection()
# c1.set_user('Luiz')
# c1.set_password('1234')
# print(c1.user)
# print(c1.passoword)