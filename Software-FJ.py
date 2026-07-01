
#Libreria necesaria para crear clases abstractas
from abc import ABC


#Clase abstracta que representa entidades generales del sistema
class Entidad(ABC):

    #Contador para asignar identificadores unicos a cada entidad
    contador_entidades = 0
    
    #Constructor que inicializa la entidad asignando automaticamente un identificador unico
    def __init__(self):

        #Aumenta el contador cada vez que se crea una nueva entidad
        Entidad.contador_entidades += 1

        #Atributo privado que almacena el identificador unico de la entidad
        self.__id = Entidad.contador_entidades

    #Metodo que devuelve el identificador unico de la entidad
    def obtener_id(self):
        return self.__id



#Subclase que representa un cliente del sistema
class Cliente(Entidad):
    pass


#Clase abstracta que representa un servicio del sistema
class Servicio(Entidad, ABC):
    pass


#Subclase que representa el servicio de reservas de salas
class ReservaSala(Servicio):
    pass


#Subclase que representa el servicio de alquiler de equipos
class AlquilerEquipo(Servicio):
    pass


#Subclase que representa el servicio de asesorías especializadas
class AsesoriaEspecial(Servicio):
    pass


#Subclase que representa una reserva del sistema
class Reserva(Entidad):
    pass