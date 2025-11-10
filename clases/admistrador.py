class Adminitrador:
    def __init__(self, nombre, usuario, contraseña):
        self.nombre = nombre
        self.__usuario = usuario
        self.__contraseña = contraseña


    def get_usuario(self):
        return self.__usuario
   
    def set_usuario(self,usuario):
        self.__usuario = usuario


    def get_contraseña(self):
        return self.__contraseña
   
    def set_contraseña(self, contraseña):
        self.__contraseña = contraseña
