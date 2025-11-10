from club import Club
class ClubCategoria(Club):
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_de_fundacion,):
        super().__init__(nombre, descripcion, ubicacion, presidente, fecha_de_fundacion)
        self.__socios = []
        self.actividades = []


    def get_socios(self):
        return self.__socios
   
    def set_socios(self, lista_socios):
            self.__socios = list(lista_socios)
