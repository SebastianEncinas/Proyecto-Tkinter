class Persona:
    def __init__(self, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad):
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.__tipo_identificacion = tipo_identificacion
        self.__identificacion = identificacion
        self.__nacionalidad = nacionalidad


    def get_TipoDeIdentificacion(self):
        return self.__tipo_identificacion
   
    def set_TipoDeIdentificacion(self, tipo_identificacion):
        self.__tipo_identificacion = tipo_identificacion
   
    def get_identificacion(self):
        return self.__identificacion
   
    def set_identificacion(self, identificacion):
        self.__identificacion = identificacion


    def get_nacionalidad(self):
        return self.__nacionalidad
   
    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

