#Estudiantes:
#Juan David Calderón Amorocho
#Henry Leonardo Borrero Lopez


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


# ==============================================================================
# APORTE JUAN DAVID - DESARROLLO DE LA INTERFAZ GRAFICA 
# ==============================================================================

#Librería necesaria para crear la interfaz grafica
import tkinter as tk
from tkinter import ttk, messagebox



# Se crea la ventana principal de la aplicación.
ventana = tk.Tk()

# Se establece el título que aparecerá en la barra superior de la ventana.
ventana.title("SOFTWARE FJ - Sistema de Gestión Integral")

#Se define el tamaño fijo de la ventana
ventana.geometry("1250x750")

#Se deshabilita la opción de redimensionar la ventana
ventana.resizable(False, False)



# ==============================================================================
# VARIABLES
# ==============================================================================

#Variable de control para el tipo de servicio seleccionado en el combobox
tipo_servicio_var = tk.StringVar(value="Alquiler de Equipos")

#Diccionarios para poder acceder a los objetos de clientes, servicios y reservas desde los combobox
clientes_dict = {}
servicios_dict = {}
reservas_dict = {}



# ==============================================================================
# ACTUALIZADORES DE COMBOBOX
# ==============================================================================

#Metodo que actualiza el combobox de clientes con los clientes registrados
def actualizar_clientes():

    #Se crea una lista de opciones para el combobox 
    valores = []

    #Se limpia el diccionario de clientes 
    clientes_dict.clear()

    #Se recorre la lista de clientes registrados
    for c in clientes_registrados:

        #Se construye el texto que se mostrará en el combobox y se agrega al diccionario de clientes
        key = f"{c.obtener_id()} - {c.obtener_nombre()}"
        clientes_dict[key] = c

        #Se agrega el texto a la lista de opciones del combobox
        valores.append(key)
    
    #Se actualiza el combobox de clientes con los valores generados
    combo_cliente_reserva["values"] = valores


#Metodo que actualiza el combobox de servicios con los servicios registrados
def actualizar_servicios():

    #Se crea una lista de opciones para el combobox 
    valores = []

    #Se limpia el diccionario de servicios
    servicios_dict.clear()

    #Se recorre la lista de servicios registrados
    for s in servicios_registrados:

        #Se construye el texto que se mostrará en el combobox y se agrega al diccionario de servicios
        key = f"{s.obtener_id()} - {s.obtener_nombre_servicio()}"
        servicios_dict[key] = s

        #Se agrega el texto a la lista de opciones del combobox
        valores.append(key)

    #Se actualiza el combobox de servicios con los valores generados
    combo_servicio_reserva["values"] = valores


#Metodo que actualiza el combobox de reservas con las reservas registradas
def actualizar_reservas():

    #Se crea una lista de opciones para el combobox 
    valores = []

    #Se limpia el diccionario de reservas
    reservas_dict.clear()

    #Se recorre la lista de reservas registradas
    for r in reservas_registradas:

        #Se construye el texto que se mostrará en el combobox y se agrega al diccionario de reservas
        key = f"Reserva #{r.obtener_id()} - {r.obtener_cliente().obtener_nombre()}"
        reservas_dict[key] = r

        #Se agrega el texto a la lista de opciones del combobox
        valores.append(key)

    #Se actualiza el combobox de reservas con los valores generados
    combo_reservas["values"] = valores



# ==============================================================================
# RESULTADOS
# ==============================================================================

#Metodo que muestra un texto en el cuadro de resultados de la interfaz
def mostrar(texto):
    txt_resultado.config(state="normal")
    txt_resultado.delete("1.0", tk.END)
    txt_resultado.insert(tk.END, texto)
    txt_resultado.config(state="disabled")



# ==============================================================================
# CLIENTE
# ==============================================================================

#Metodo encargado de registrar un cliente desde la interfaz grafica
def registrar_cliente():

    try:

        #Se crea un objeto Cliente con los datos ingresados por el usuario
        c = Cliente(
            entry_nombre.get(),
            entry_correo.get(),
            entry_telefono.get()
        )

        #Se agrega el cliente a la lista de clientes registrados
        clientes_registrados.append(c)

        #Se actualiza el combobox de clientes con el nuevo cliente registrado
        actualizar_clientes()

        #Se registra el evento en el log
        registrar_log(f"Cliente: {c.obtener_nombre()}")

        #Se muestra la información del cliente registrado en el cuadro de resultados de la interfaz
        mostrar("CLIENTE REGISTRADO\n\n" + f"ID: {c.obtener_id()}\n" + f"Nombre: {c.obtener_nombre()}\n" + f"Correo: {c.obtener_correo()}\n" + f"Teléfono: {c.obtener_telefono()}")

        #Se limpian los campos de entrada de la interfaz 
        entry_nombre.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)

    #Se captura cualquier excepción que ocurra durante el registro del cliente 
    except Exception as e:

        #Se muestra un mensaje de error en la interfaz
        messagebox.showerror("Error", str(e))

        #Se registra el error en el log
        registrar_log(str(e))


#Metodo encargado de mostrar los clientes registrados en el cuadro de resultados de la interfaz
def ver_clientes():

    #Se verifica si hay clientes registrados, si no los hay se muestra un mensaje
    if not clientes_registrados:
        mostrar("NO HAY CLIENTES REGISTRADOS")
        return
    
    #Se construye un texto con la información de la lista de clientes registrados
    texto = "LISTA DE CLIENTES REGISTRADOS\n\n"
    for c in clientes_registrados:
        texto += (
            f"ID: {c.obtener_id()} | "
            f"Nombre: {c.obtener_nombre()} | "
            f"Correo: {c.obtener_correo()} | "
            f"Teléfono: {c.obtener_telefono()}\n"
        )

    #Se muestra el texto en el cuadro de resultados de la interfaz
    mostrar(texto)



# ==============================================================================
# SERVICIO
# ==============================================================================

#Metodo encargado de registrar un servicio desde la interfaz grafica
def registrar_servicio():

    try:

        #Se obtienen los datos ingresados por el usuario en la interfaz
        nombre = entry_servicio_nombre.get()
        precio=(entry_servicio_precio.get())
        tipo = tipo_servicio_var.get()

        #Se valida que el precio del servicio no este vacio
        if precio == "":
            raise ValueError("Debe ingresar el precio del servicio.")
        
        #Se valida que el precio del servicio sea un número
        try:
            precio = float(precio)
        except ValueError:
            raise ValueError("El precio del servicio debe ser un número.")
        
        #Se valida que el precio del servicio sea mayor a cero
        if precio <= 0:
            raise ValueError("El precio del servicio debe ser mayor a cero.")

        #A partir del tipo de servicio seleccionado, se crea un objeto de la subclase correspondiente
        if tipo == "Alquiler de Equipos":
            s = AlquilerEquipo(nombre, precio)
        elif tipo == "Reserva de Salas":
            s = ReservaSala(nombre, precio)
        else:
            s = AsesoriaEspecial(nombre, precio)

        #Se agrega el servicio a la lista de servicios registrados
        servicios_registrados.append(s)

        #Se actualiza el combobox de servicios con el nuevo servicio registrado
        actualizar_servicios()

        #Se registra el evento en el log
        registrar_log(f"Servicio: {s.obtener_nombre_servicio()}")

        #Se muestra la información del servicio registrado en el cuadro de resultados de la interfaz
        mostrar(s.describir_servicio())

        #Se limpian los campos de entrada de la interfaz
        entry_servicio_nombre.delete(0, tk.END)
        entry_servicio_precio.delete(0, tk.END)

    #Se captura cualquier excepción que ocurra durante el registro del servicio                     
    except Exception as e:

        #Se muestra un mensaje de error en la interfaz
        messagebox.showerror("Error", str(e))

        #Se registra el error en el log
        registrar_log(str(e))


#Metodo encargado de mostrar los servicios registrados en el cuadro de resultados de la interfaz
def ver_servicios():

    #Se verifica si hay servicios registrados, si no los hay se muestra un mensaje
    if not servicios_registrados:
        mostrar("NO HAY SERVICIOS REGISTRADOS")
        return
 
    #Se construye un texto con la información de la lista de servicios registrados
    texto = "SERVICIOS REGISTRADOS\n\n"

    #Se recorre la lista de servicios registrados y se obtiene la información correspondiente dependiendo del tipo de servicio
    for s in servicios_registrados:
 
        #Si corresponde a un servicio de alquiler de equipos, se obtiene el nombre del equipo y el precio por hora
        if isinstance(s, AlquilerEquipo):
            tipo = "Alquiler de Equipos"
            nombre = s.obtener_nombre_equipo()
            precio = f"{s.obtener_precio_por_hora()} / hora"

        #Si corresponde a un servicio de reserva de salas, se obtiene el tipo de sala y el precio por día
        elif isinstance(s, ReservaSala):
            tipo = "Reserva de Salas"
            nombre = s._ReservaSala__tipo_sala
            precio = f"{s._ReservaSala__precio_por_dia} / día"

        #Si corresponde a un servicio de asesoría especializada, se obtiene la especialidad y la tarifa fija
        elif isinstance(s, AsesoriaEspecial):
            tipo = "Asesoría Especializada"
            nombre = s._AsesoriaEspecial__especialidad
            precio = f"{s._AsesoriaEspecial__tarifa_fija} / sesión"
 
        #Si no corresponde a ningun tipo de servicio
        else:
            tipo = "Desconocido"
            nombre = "N/A"
            precio = "N/A"

        #Se agrega la información del servicio al texto que sera mostrado en el cuadro de resultados
        texto += (
            f"ID: {s.obtener_id()} | "
            f"Tipo: {tipo} | "
            f"Nombre: {nombre} | "
            f"Precio: {precio}\n"
        )

    #Se muestra el texto en el cuadro de resultados de la interfaz
    mostrar(texto)



# ==============================================================================
# RESERVA
# ==============================================================================

#Metodo encargado de registrar una reserva desde la interfaz grafica
def crear_reserva():

    try:
        
        #Se obtienen las claves seleccionadas en los combobox de cliente y servicio
        c_key = combo_cliente_reserva.get()
        s_key = combo_servicio_reserva.get()

        #Se valida que se haya seleccionado un cliente
        if c_key not in clientes_dict:
            raise ValueError("Seleccione un cliente.")

        #Se valida que se haya seleccionado un servicio
        if s_key not in servicios_dict:
            raise ValueError("Seleccione un servicio.")

        #Se obtienen los objetos de cliente y servicio a partir de las claves seleccionadas
        cliente = clientes_dict[c_key]
        servicio = servicios_dict[s_key]

        #Se obtiene la duración ingresada por el usuario
        duracion_texto = entry_duracion.get()

        #Se valida que la duración no esté vacía
        if duracion_texto == "":
            raise ValueError("Debe ingresar la duración de la reserva.")
        
        #Se valida que la duración sea un número entero
        try:
            duracion = int(duracion_texto)
        except ValueError:
            raise ValueError("La duración debe ser un número entero.")

        #Se crea la reserva y se agrega a la lista de reservas registradas
        r = Reserva(cliente, servicio, duracion)
        reservas_registradas.append(r)

        #Se actualiza el combobox de reservas con la nueva reserva registrada
        actualizar_reservas()
        
        #Se registra el evento en el log
        registrar_log(f"Reserva: {r.obtener_id()}")

        #Se muestra la información de la reserva registrada en el cuadro de resultados de la interfaz
        mostrar(r.mostrar_detalle())
        entry_duracion.delete(0, tk.END)

    #Se captura cualquier excepción que ocurra durante el registro de la reserva
    except Exception as e:
        messagebox.showerror("Error", str(e))
        registrar_log(str(e))
 

#Metodo encargado de mostrar las reservas registradas en el cuadro de resultados de la interfaz
def ver_reservas():

    #Se verifica si hay reservas registradas, si no las hay se muestra un mensaje
    if not reservas_registradas:
        mostrar("NO HAY RESERVAS REGISTRADAS")
        return

    #Se construye un texto con la información de la lista de reservas registradas
    texto = "LISTA DE RESERVAS REGISTRADAS\n\n"

    #Se recorre la lista de reservas registradas y se obtiene la información de cada reserva
    for r in reservas_registradas:
        texto += r.mostrar_detalle() + "\n\n"

    #Se muestra el texto en el cuadro de resultados de la interfaz
    mostrar(texto)



# ==============================================================================
# ACCIONES RESERVA
# ==============================================================================

#Metodo encargado de confirmar una reserva registrada desde la interfaz grafica
def confirmar_reserva():

    #Se obtiene la reserva seleccionada en el combobox 
    try:
        key = combo_reservas.get()

        #Se valida que se haya seleccionado una reserva
        if not key:
            messagebox.showwarning("Validación", "Debe seleccionar una reserva")
            return

        #Se obtiene el objeto de reserva a partir de la clave seleccionada
        r = reservas_dict[key]

        #Llamada al método de la clase Reserva para confirmar la reserva
        r.confirmar_reserva()

        #Actualiza el cuadro de resultados con la información de la reserva confirmada 
        mostrar(r.mostrar_detalle())

        #Se muestra un mensaje de éxito en la interfaz
        messagebox.showinfo("Éxito", "Reserva confirmada correctamente")

    #Se captura cualquier excepción relacionada con la regla de negocio al intentar confirmar la reserva
    except RuntimeError as e:
        messagebox.showerror("Regla de negocio", str(e))

    #Se captura cualquier otra excepción que ocurra durante la confirmación de la reserva
    except Exception as e:
        messagebox.showerror("Error", "No se pudo confirmar la reserva")
        registrar_log(str(e))


#Metodo encargado de cancelar una reserva registrada desde la interfaz grafica
def cancelar_reserva():
    
    #Se obtiene la reserva seleccionada en el combobox
    try:
        key = combo_reservas.get()

        #Se valida que se haya seleccionado una reserva
        if not key:
            messagebox.showwarning("Validación", "Debe seleccionar una reserva")
            return

        #Se obtiene el objeto de reserva a partir de la clave seleccionada
        r = reservas_dict[key]

        #Llamada al método de la clase Reserva para cancelar la reserva
        r.cancelar_reserva()

        #Actualiza el cuadro de resultados con la información de la reserva cancelada
        mostrar(r.mostrar_detalle())

        #Se muestra un mensaje de éxito en la interfaz
        messagebox.showinfo("Éxito", "Reserva cancelada correctamente")

    #Se captura cualquier excepción relacionada con la regla de negocio al intentar cancelar la reserva
    except RuntimeError as e:
        messagebox.showerror("Regla de negocio", str(e))

    #Se captura cualquier otra excepción que ocurra durante la cancelación de la reserva
    except Exception as e:
        messagebox.showerror("Error", "No se pudo cancelar la reserva")
        registrar_log(str(e))


#Metodo encargado de mostrar los detalles de una reserva registrada desde la interfaz grafica
def ver_detalle_reserva():

    #Se obtiene la reserva seleccionada en el combobox
    try:
        key = combo_reservas.get()

        #Se valida que se haya seleccionado una reserva
        if not key:
            messagebox.showwarning("Validación", "Debe seleccionar una reserva")
            return

        #Se obtiene el objeto de reserva a partir de la clave seleccionada
        r = reservas_dict[key]

        #Actualiza el cuadro de resultados con la información de la reserva seleccionada
        mostrar(r.mostrar_detalle())

    #Se captura cualquier excepción que ocurra al intentar mostrar los detalles de la reserva
    except Exception as e:
        messagebox.showerror("Error", "No se pudo mostrar la información de la reserva")
        registrar_log(str(e))



# ==============================================================================
# VISUAL
# ==============================================================================

# 1. REGISTRAR CLIENTE

#Frame para agrupar los elementos relacionados con el registro de clientes
frame1 = tk.LabelFrame(ventana, text="1.Registrar Cliente")
frame1.place(x=10, y=10, width=380, height=230)

#Etiqueta y campo de entrada para el nombre del cliente 
tk.Label(frame1, text="Nombre").pack()
entry_nombre = tk.Entry(frame1, width=40)
entry_nombre.pack()

#Etiqueta y campo de entrada para el correo del cliente
tk.Label(frame1, text="Correo").pack()
entry_correo = tk.Entry(frame1, width=40)
entry_correo.pack()

#Etiqueta y campo de entrada para el teléfono del cliente
tk.Label(frame1, text="Teléfono").pack()
entry_telefono = tk.Entry(frame1, width=40)
entry_telefono.pack()

#Boton para registrar un cliente 
tk.Button(frame1, text="Registrar Cliente", command=registrar_cliente).pack(pady=5)

#Botón para ver los clientes registrados
tk.Button(frame1, text="Ver Clientes", command=ver_clientes).pack(pady=5)


# 2. REGISTRAR SERVICIO

#Frame para agrupar los elementos relacionados con el registro de servicios
frame2 = tk.LabelFrame(ventana, text="2.Registrar Servicio")
frame2.place(x=400, y=10, width=400, height=230)

#Etiqueta y combobox para seleccionar el tipo de servicio 
tk.Label(frame2, text="Tipo").pack()
ttk.Combobox(frame2, textvariable=tipo_servicio_var,values=["Alquiler de Equipos", "Reserva de Salas", "Asesoria Especializada"], width=40).pack()

#Etiqueta y campo de entrada para el nombre del Equipo/Sala/Especialidad 
tk.Label(frame2, text="Nombre del Equipo/Sala/Especialidad").pack()
entry_servicio_nombre = tk.Entry(frame2, width=40)
entry_servicio_nombre.pack()

#Etiqueta y campo de entrada para el precio del servicio
tk.Label(frame2, text="Precio").pack()
entry_servicio_precio = tk.Entry(frame2, width=40)
entry_servicio_precio.pack()

#Botón para registrar un servicio
tk.Button(frame2, text="Registrar Servicio", command=registrar_servicio).pack(pady=5)

#Botón para ver los servicios registrados
tk.Button(frame2, text="Ver Servicios", command=ver_servicios).pack(pady=5)


# 3. REGISTRAR RESERVA

#Frame para agrupar los elementos relacionados con el registro de reservas
frame3 = tk.LabelFrame(ventana, text="3.Registrar Reserva")
frame3.place(x=820, y=10, width=400, height=230)

#Etiqueta y combobox para seleccionar el cliente de la reserva
tk.Label(frame3, text="Cliente").pack()
combo_cliente_reserva = ttk.Combobox(frame3, width=40)
combo_cliente_reserva.pack()

#Etiqueta y combobox para seleccionar el servicio de la reserva
tk.Label(frame3, text="Servicio").pack()
combo_servicio_reserva = ttk.Combobox(frame3, width=40)
combo_servicio_reserva.pack()

#Etiqueta y campo de entrada para la duración de la reserva
tk.Label(frame3, text="Duración").pack()
entry_duracion = tk.Entry(frame3, width=40)
entry_duracion.pack()

#Botón para registrar una reserva
tk.Button(frame3, text="Registrar Reserva", command=crear_reserva).pack(pady=5)

#Botón para ver las reservas registradas
tk.Button(frame3, text="Ver Reservas", command=ver_reservas).pack(pady=5)


# 4. GESTIÓN RESERVAS

#Frame para agrupar los elementos relacionados con la gestión de reservas
frame4 = tk.LabelFrame(ventana, text="4.Gestión de Reservas")
frame4.place(x=300, y=250, width=600, height=200)

#Etiqueta y combobox para seleccionar la reserva registrada
combo_reservas = ttk.Combobox(frame4, width=60)
combo_reservas.pack(pady=5)

#Botón para ver la información de la reserva
tk.Button(frame4, text="Ver Detalles", command=ver_detalle_reserva).pack(padx=10)

#Botón para confirmar una reserva
tk.Button(frame4, text="Confirmar", command=confirmar_reserva).pack(side="left", padx=10)

#Botón para cancelar una reserva
tk.Button(frame4, text="Cancelar", command=cancelar_reserva).pack(side="right", padx=10)


# RESULTADOS

#Frame para mostrar los resultados de las operaciones
frame5 = tk.LabelFrame(ventana, text="Resultados")
frame5.place(x=10, y=460, width=1210, height=250)

#Area de texto para mostrar los resultados de las operaciones
txt_resultado = tk.Text(frame5, state="disabled")
txt_resultado.pack(fill="both", expand=True)



# ==============================================================================
# INICIALIZACIÓN
# ==============================================================================

actualizar_clientes()
actualizar_servicios()
actualizar_reservas()

ventana.mainloop()