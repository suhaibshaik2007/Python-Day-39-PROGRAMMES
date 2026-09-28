# PASSWORD SETTER
class Account:
    def __init__(self,password):
        self._password = password

        @property
        def password(self):
            return self._password

        @password.setter
        def password(self,value):
            if len(value) >= 6:
                self._password = value
            else:
                print("Password must contain at leasr 6 chcaracters")
                a = Account("abc123")
                print(a.password)

                a.password ="python12"
                print(a._password)

                a.password = 12522536