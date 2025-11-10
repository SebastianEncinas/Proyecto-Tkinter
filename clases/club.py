class Club:
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_de_fundacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.__presidente = presidente
        self.__fecha_de_fundacion = fecha_de_fundacion


    def get_presidente(self):
        return self.__presidente
   
    def get_fecha_de_fundacion(self):
        return self.__fecha_de_fundacion
   
    def set_presidente(self, presidente):
        self.__presidente = presidente


    def set_fecha_de_fundacion(self, fecha_de_fundacion):
        self.__fecha_de_fundacion = fecha_de_fundacion


    def mostrar_info(self):
        print("El nombre del este equipo es: ",self.nombre, "A continuacion dejareemos una breve descripcion del club: ",
        self.descripcion, "Esta es la ubicacion de nuestro estadio: ", self.ubicacion, "y este se nuestro qeridisimo preidente: ", self.__presidente, "y por ultimo la fecha de fundacion de nuestro amado y hermoso club: ", self.__fecha_de_fundacion)

