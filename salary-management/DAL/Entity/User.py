from DAL.Entity.BaseEntity import BaseEntity


from DAL.Entity.BaseEntity import BaseEntity


class User(BaseEntity):
    def __init__(self):
        self.dict_user = {
        "id_user": int(),
        "login": str(),
        "email": str(),
        "passwd": str()
        }

    def return_dict(self):
        return self.dict_user

    def __str__(self):
        return f'''
                ID: {self.dict_user["id_user"]} 
                Login: {self.dict_user["login"]} 
                Email: {self.dict_user["email"]} 
                Password: {self.dict_user["passwd"]} 
                '''

