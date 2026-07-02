
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
    
    #Constructor que inicializa los datos del cliente y valida la información
    def __init__(self, nombre, correo, telefono):
       
       #Validación de los datos antes de crear el cliente
       self.__validar_nombre(nombre)
       self.__validar_correo(correo)
       self.__validar_telefono(telefono)

       #Llamada al constructor de la clase base para inicializar la entidad asignando un identificador unico
       super().__init__()

       #Atributos privados que almacenan los datos del cliente
       self.__nombre = nombre
       self.__correo = correo
       self.__telefono = telefono
    
    #Metodo privado para validar el nombre del cliente
    def __validar_nombre(self, nombre):
       
       #Valida que el nombre no sea nulo o vacío
       if nombre is None or nombre == "":
           raise ValueError("El nombre del cliente no puede estar vacío.")
       
       #Valida que el nombre sea una cadena de texto
       if not isinstance(nombre, str):
              raise TypeError("El nombre del cliente debe ser una cadena de texto.")
       
       #Valida que el nombre no tenga caracteres especiales o números
       for caracter in nombre:
           if not (caracter.isalpha() or caracter.isspace()):
               raise ValueError("El nombre del cliente no puede contener caracteres especiales o números.")

    #Metodo privado para validar el correo del cliente       
    def __validar_correo(self, correo):
       
       #Valida que el correo no sea nulo o vacío
       if correo is None or correo == "":
           raise ValueError("El correo del cliente no puede estar vacío.")
       
       #Valida que el correo sea una cadena de texto
       if not isinstance(correo, str):
              raise TypeError("El correo del cliente debe ser una cadena de texto.")
       
       #Valida que el correo no tenga espacios 
       if " " in correo:
             raise ValueError("El correo del cliente no puede contener espacios.")
       
       #Valida que el correo contenga un unico "@" y que el dominio tenga al menos un punto
       if correo.count("@") != 1 or "." not in correo.split("@")[1]:
             raise ValueError("El correo del cliente debe tener un formato válido.")
       
    #Metodo privado para validar el telefono del cliente
    def __validar_telefono(self, telefono):
       
       #Valida que el telefono no sea nulo o vacío
       if telefono is None or telefono == "":
           raise ValueError("El teléfono del cliente no puede estar vacío.")
       
       #Valida que el telefono sea una cadena de texto
       if not isinstance(telefono, str):
              raise TypeError("El teléfono del cliente debe ser una cadena de texto.")
       
       #Valida que el telefono solo contenga numeros
       if not telefono.isdigit():
                 raise ValueError("El teléfono del cliente solo puede contener números.")
       
       #Valida que el telefono tenga una longitud de 10 digitos
       if len(telefono) != 10:
                 raise ValueError("El teléfono del cliente debe tener exactamente 10 dígitos.")
       
    #Metodo que devuelve el nombre del cliente
    def obtener_nombre(self):
        return self.__nombre
    
    #Metodo que devuelve el correo del cliente
    def obtener_correo(self):
        return self.__correo
    
    #Metodo que devuelve el telefono del cliente
    def obtener_telefono(self):
        return self.__telefono
       

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