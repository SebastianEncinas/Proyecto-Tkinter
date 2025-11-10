class Socio:
    def __init__(self, fecha_inscripcion, estado, usuario, contraseña):
        self.fecha_inscripcion = fecha_inscripcion
        self.estado = estado
        self.__usuario = usuario
        self.__contraseña = contraseña


    def get_usuario(self):
        return self.__usuario
   
    def set_usuario(self, usuario):
        self.__usuario = usuario


    def get_contraseña(self):
        return self.__contraseña
   
    def set_contraseña(self, contraseña):
        self.__contraseña = contraseña