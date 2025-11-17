class Socio:
    def __init__(self, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad ,fecha_inscripcion, estado, usuario, contraseña):
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.__tipo_identificacion = tipo_identificacion
        self.__identificacion = identificacion
        self.__nacionalidad = nacionalidad
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

    def get_tipo_identificacion(self):
        return self.__tipo_identificacion
   
    def set_tipo_identificacion(self, tipo_identificacion):
        self.__tipo_identificacion = tipo_identificacion 

    def get_identificacion(self):
        return self.__identificacion
   
    def set_identificacion(self, identificacion):
        self.__identificacion = identificacion
    
    def get_nacionalidad(self):
        return self.__nacionalidad
   
    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad
