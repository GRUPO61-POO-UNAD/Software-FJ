
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
    
    def __init__(self, nombre_servicio):
        super().__init__()
        self._nombre_servicio = nombre_servicio
        
    def obtener_nombre_servicio(self):
        return self._nombre_servicio

    # Métodos base para la aplicación de polimorfismo
    def describir_servicio(self):
        return f"Servicio: {self._nombre_servicio}"

    def calcular_costo(self, cantidad):
        return 0.0


# ==============================================================================
# APORTE  HENRY
# ==============================================================================

#Subclase que representa el servicio de alquiler de equipos
class AlquilerEquipo(Servicio):
    
    def __init__(self, nombre_equipo, precio_por_hora):
        self.__validar_nombre_equipo(nombre_equipo)
        self.__validar_precio(precio_por_hora)
        super().__init__(f"Alquiler de {nombre_equipo}")
        self.__nombre_equipo = nombre_equipo
        self.__precio_por_hora = precio_por_hora

    def __validar_nombre_equipo(self, nombre_equipo):
        if nombre_equipo is None or nombre_equipo == "":
            raise ValueError("El nombre del equipo no puede estar vacío.")
        if not isinstance(nombre_equipo, str):
            raise TypeError("El nombre del equipo debe ser una cadena de texto.")

    def __validar_precio(self, precio_por_hora):
        if precio_por_hora is None:
            raise ValueError("El precio por hora no puede ser nulo.")
        if not isinstance(precio_por_hora, (int, float)):
            raise TypeError("El precio por hora debe ser un número.")
        if precio_por_hora <= 0:
            raise ValueError("El precio por hora debe ser mayor a cero.")

    def obtener_nombre_equipo(self):
        return self.__nombre_equipo

    def obtener_precio_por_hora(self):
        return self.__precio_por_hora

    # Sobrescritura de métodos (Polimorfismo)
    def describir_servicio(self):
        return f"[Alquiler Equipos] {self.__nombre_equipo} | Tarifa: ${self.__precio_por_hora}/hora"

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ValueError("La cantidad de horas de alquiler debe ser mayor a cero.")
        return self.__precio_por_hora * horas

    # Sobrecarga de métodos simulada mediante parámetros opcionales (Requerimiento UNAD)
    def calcular_costo_avanzado(self, horas, descuento=0.0, impuesto=0.0):
        costo_base = self.calcular_costo(horas)
        if not (0 <= descuento <= 1):
            raise ValueError("El descuento debe ser un valor decimal entre 0.0 y 1.0.")
        if impuesto < 0:
            raise ValueError("El impuesto asignado no puede ser negativo.")
        return (costo_base * (1 - descuento)) * (1 + impuesto)


#Subclase que representa el servicio de reservas de salas
class ReservaSala(Servicio):
    
    def __init__(self, tipo_sala, precio_por_dia):
        if tipo_sala is None or tipo_sala == "":
            raise ValueError("El tipo de sala no puede estar vacío.")
        if not isinstance(precio_por_dia, (int, float)) or precio_por_dia <= 0:
            raise ValueError("El precio por día de sala debe ser un número positivo mayor a cero.")
            
        super().__init__(f"Reserva de Sala {tipo_sala}")
        self.__tipo_sala = tipo_sala
        self.__precio_por_dia = precio_por_dia

    # Sobrescritura de métodos (Polimorfismo)
    def describir_servicio(self):
        return f"[Reserva Salas] Espacio: {self.__tipo_sala} | Tarifa: ${self.__precio_por_dia}/día"

    def calcular_costo(self, dias):
        if not isinstance(dias, int) or dias <= 0:
            raise ValueError("La cantidad de días para la reserva debe ser un número entero mayor a cero.")
        return self.__precio_por_dia * dias


#Subclase que representa el servicio de asesorías especializadas
class AsesoriaEspecial(Servicio):
    
    def __init__(self, especialidad, tarifa_fija):
        if especialidad is None or especialidad == "":
            raise ValueError("La especialidad de la asesoría no puede estar vacía.")
        if not isinstance(tarifa_fija, (int, float)) or tarifa_fija <= 0:
            raise ValueError("La tarifa de la asesoría debe ser un número positivo mayor a cero.")
            
        super().__init__(f"Asesoría en {especialidad}")
        self.__especialidad = especialidad
        self.__tarifa_fija = tarifa_fija

    # Sobrescritura de métodos (Polimorfismo)
    def describir_servicio(self):
        return f"[Asesorías] Especialidad: {self.__especialidad} | Costo Único: ${self.__tarifa_fija}"

    def calcular_costo(self, sesiones):
        if not isinstance(sesiones, int) or sesiones <= 0:
            raise ValueError("El número de sesiones agendadas debe ser un entero mayor a cero.")
        return self.__tarifa_fija * sesiones


#Subclase que representa una reserva del sistema
class Reserva(Entidad):
    
    def __init__(self, cliente, servicio, duracion):
        if not isinstance(cliente, Cliente):
            raise TypeError("El cliente debe ser una instancia de la clase Cliente.")
        if not isinstance(servicio, Servicio):
            raise TypeError("El servicio debe ser una subclase válida de la clase Servicio.")
        if duracion <= 0:
            raise ValueError("La duración estipulada debe ser mayor a cero.")
            
        super().__init__()
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente" # Estados establecidos: Pendiente, Confirmada, Cancelada
        self.__costo_total = servicio.calcular_costo(duracion)

    def obtener_cliente(self): return self.__cliente
    def obtener_servicio(self): return self.__servicio
    def obtener_duracion(self): return self.__duracion
    def obtener_estado(self): return self.__estado
    def obtener_costo_total(self): return self.__costo_total

    def confirmar_reserva(self):
        if self.__estado == "Cancelada":
            raise RuntimeError("Restricción de flujo: Imposible confirmar una reserva previamente cancelada.")
        self.__estado = "Confirmada"

    def cancelar_reserva(self):
        if self.__estado == "Confirmada":
            raise RuntimeError("Restricción de flujo: Imposible cancelar una reserva que ya cuenta con estado Confirmada.")
        self.__estado = "Cancelada"

    def mostrar_detalle(self):
        return (f"Reserva #{self.obtener_id()} [{self.__estado}] | "
                f"Cliente: {self.__cliente.obtener_nombre()} | "
                f"Servicio: {self.__servicio.describir_servicio()} | "
                f"Duración: {self.__duracion} | "
                f"Total: ${self.__costo_total}")


# ==============================================================================
# SISTEMA DE MANEJO DE ARCHIVOS (LOGS) Y COMPROBACIÓN DE 10 OPERACIONES
# ==============================================================================

def registrar_log(mensaje):
    """Escribe los eventos normales y los rastros de excepciones en un archivo externo .txt."""
    try:
        with open("log_sistema_software_fj.txt", "a", encoding="utf-8") as archivo:
            archivo.write(mensaje + "\n")
    except Exception as e:
        print(f"Error crítico al guardar en archivo de logs: {e}")


# Estructuras internas en memoria (Listas locales de gestión)
clientes_registrados = []
servicios_registrados = []
reservas_registradas = []

print("==========================================================")
print("  EJECUTANDO SISTEMA DE GESTIÓN INTEGRAL: SOFTWARE FJ")
print("==========================================================\n")

registrar_log("\n--- NUEVA SESIÓN DE EJECUCIÓN DEL SISTEMA ---")

# OPERACIÓN 1: Creación correcta de un Cliente
try:
    cl1 = Cliente("Henry Borrero", "henry@unad.edu.co", "3159876543")
    clientes_registrados.append(cl1)
    print(f"[OP 1 SUCCESS] Cliente registrado con éxito: {cl1.obtener_nombre()}")
except (ValueError, TypeError) as err:
    registrar_log(f"[ERROR OP 1] {err}")

# OPERACIÓN 2: Intento de creación de Cliente inválido (Nombre con números)
try:
    cl_error = Cliente("Henry123", "error@unad.edu.co", "3150001122")
except (ValueError, TypeError) as err:
    print(f"[OP 2 CONTROLADA] Excepción capturada en cliente (Nombre no permitido).")
    registrar_log(f"[ERROR OP 2] Excepción esperada: {err}")

# OPERACIÓN 3: Intento de creación de Cliente inválido (Teléfono con longitud errónea)
try:
    cl_error2 = Cliente("Carlos Perez", "carlos@correo.com", "12345")
except (ValueError, TypeError) as err:
    print(f"[OP 3 CONTROLADA] Excepción capturada en cliente (Teléfono fuera de rango).")
    registrar_log(f"[ERROR OP 3] Excepción esperada: {err}")

# OPERACIÓN 4: Creación correcta de Servicio (AlquilerEquipo)
try:
    sv1 = AlquilerEquipo("Guitarra Electrica Fusion", 15000)
    servicios_registrados.append(sv1)
    print(f"[OP 4 SUCCESS] Servicio registrado con éxito: {sv1.obtener_nombre_servicio()}")
except (ValueError, TypeError) as err:
    registrar_log(f"[ERROR OP 4] {err}")

# OPERACIÓN 5: Intento de creación de Servicio inválido (Precio en cero o negativo)
try:
    sv_error = AlquilerEquipo("Consola Audio Atmos", -20000)
except (ValueError, TypeError) as err:
    print(f"[OP 5 CONTROLADA] Excepción capturada en servicio (Tarifa por hora negativa).")
    registrar_log(f"[ERROR OP 5] Excepción esperada: {err}")

# OPERACIÓN 6: Creación correcta de Servicio (ReservaSala)
try:
    sv2 = ReservaSala("Estudio de Grabación A", 250000)
    servicios_registrados.append(sv2)
    print(f"[OP 6 SUCCESS] Servicio registrado con éxito: {sv2.obtener_nombre_servicio()}")
except (ValueError, TypeError) as err:
    registrar_log(f"[ERROR OP 6] {err}")

# OPERACIÓN 7: Generación correcta de una Reserva
try:
    if len(clientes_registrados) > 0 and len(servicios_registrados) > 0:
        res1 = Reserva(clientes_registrados[0], servicios_registrados[0], 5) # 5 horas contratadas
        reservas_registradas.append(res1)
        print(f"[OP 7 SUCCESS] Detalle: {res1.mostrar_detalle()}")
except (ValueError, TypeError, RuntimeError) as err:
    registrar_log(f"[ERROR OP 7] {err}")

# OPERACIÓN 8: Intento de registro de Reserva fallido (Duración negativa)
try:
    if len(clientes_registrados) > 0 and len(servicios_registrados) > 0:
        res_error = Reserva(clientes_registrados[0], servicios_registrados[0], -10)
except (ValueError, TypeError, RuntimeError) as err:
    print(f"[OP 8 CONTROLADA] Excepción capturada en reserva (Duración inválida).")
    registrar_log(f"[ERROR OP 8] Excepción esperada: {err}")

# OPERACIÓN 9: Ejecución de flujo correcto (Confirmación de Reserva)
try:
    if len(reservas_registradas) > 0:
        reservas_registradas[0].confirmar_reserva()
        print(f"[OP 9 SUCCESS] Estado Actualizado: {reservas_registradas[0].mostrar_detalle()}")
except RuntimeError as err:
    registrar_log(f"[ERROR OP 9] {err}")

# OPERACIÓN 10: Intento de alteración inválida de estados (Cancelar reserva ya confirmada)
try:
    if len(reservas_registradas) > 0:
        # Generará un RuntimeError porque fue confirmada en la Operación 9
        reservas_registradas[0].cancelar_reserva()
except RuntimeError as err:
    print(f"[OP 10 CONTROLADA] Excepción capturada en reserva (Transición de estado prohibida).")
    registrar_log(f"[ERROR OP 10] Excepción esperada de negocio: {err}")
else:
    print("Flujo alterno completado.")
finally:
    print("\n[INFO] Bloque estructural de cierre 'finally' procesado con normalidad.")
    registrar_log("--- FIN DE LA EVALUACIÓN DE OPERACIONES SIMULADAS ---")

print("\n==========================================================")
print("   PROCESAMIENTO TERMINADO SIN CAÍDAS DEL PROGRAMA")
print("==========================================================")
print("Los registros y errores controlados se encuentran en 'log_sistema_software_fj.txt'.")