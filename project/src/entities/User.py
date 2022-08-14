class User:
    """
    Esta clase contiene 4 atributos básicos. Su constructor inicializa todos los atributos.
    Los métodos definidos en esta clase son los get y set para operar con los atributos.
    """

    """Builder"""

    def __init__(self, user_code, name, surnames, pwd):
        self.__user_code = user_code
        self.__name = name
        self.__surnames = surnames
        self.__pwd = pwd

    """Getters"""

    def get_user_code(self):
        return self.__user_code

    def get_name(self):
        return self.__name

    def get_surnames(self):
        return self.__surnames

    def get_pwd(self):
        return self.__pwd

    """Setters"""

    def set_user_code(self, user_code):
        self.__user_code = user_code

    def set_surnames(self, surname1, surname2=None):
        if surname2 is not None and len(surname2) > 0:
            self.__surnames = surname1 + " " + surname2
        else:
            self.__surnames = surname1

    def set_pwd(self, pwd):
        self.__pwd = pwd

    def set_name(self, name):
        self.__name = name
