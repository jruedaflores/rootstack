
class User:

    def __init__(self, email):
        self.__id = False
        self.__name = False
        self.__email = email
        self.__email_verified_at = False
        self.__created_at = False
        self.__updated_at = False

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def email_verified_at(self):
        return self.__email_verified_at

    @property
    def created_at(self):
        return self.__created_at

    @property
    def updated_at(self):
        return self.__updated_at

    def load_by_json(self, value_json):
        self.__id = value_json.get("id", False)
        self.__name = value_json.get("name", False)
        self.__email = value_json.get("email", False)
        self.__email_verified_at = value_json.get("email_verified_at", False)
        self.__created_at = value_json.get("created_at", False)
        self.__updated_at = value_json.get("updated_at", False)
