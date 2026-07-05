# Software-FJ
Repositorio para el desarrollo de la Fase 4 - Componente practico - Practicas simuladas

PROGRAMACIÓN - (213023A_2202) - Grupo 61
Juan David Calderón Amorocho
Henry Leonardo Borrero Lopez



1. Introducción al aplicativo
Se describe el funcionamiento del aplicativo SOFTWARE FJ, desarrollado en Python bajo el paradigma de Programación Orientada a Objetos y utilizando la biblioteca Tkinter para la construcción de la interfaz gráfica.
El sistema permite gestionar de manera sencilla la información relacionada con clientes, servicios y reservas, ofreciendo una interfaz intuitiva para registrar, consultar y administrar los datos del sistema.


2. Requisitos para su ejecución
Para utilizar el aplicativo es necesario disponer de:
2.1	Python 
2.2 Visual Studio Code
2.3	Biblioteca Tkinter 
2.4	Archivos fuente del proyecto 
2.5	Sistema operativo Windows, Linux o macOS 


3. Organización de la interfaz gráfica
La interfaz gráfica se encuentra organizada en cinco secciones principales:
1.	Registro de clientes. 
2.	Registro de servicios. 
3.	Registro de reservas. 
4.	Gestión de reservas. 
5.	Panel de resultados.


4. Secciones de la Interfaz
4.1 Registro de clientes: Permite registrar un nuevo cliente 
Campos:
•	Nombre 
•	Correo electrónico 
•	Teléfono 
Botones:
•	Registrar Cliente 
•	Ver Clientes

4.2 Registro de servicios: Permite registrar un nuevo servicio 
Tipos de servicio
•	Alquiler de equipos 
•	Reserva de salas 
•	Asesoría especializada 
Campos:
•	Tipo 
•	Nombre del equipo/sala/especialidad
•	Precio 
Botones:
•	Registrar Servicio 
•	Ver Servicios 

4.3 Registro de reservas: Permite crear una reserva asociando un cliente con un servicio previamente registrado.
Campos
•	Cliente 
•	Servicio 
•	Duración 
Botones
•	Registrar Reserva 
•	Ver Reservas 

4.4 Gestión de reservas: Permite administrar las reservas registradas.
Botones
•	Ver detalles. 
•	Confirmar reserva. 
•	Cancelar reserva. 
El sistema controla automáticamente las reglas de negocio para impedir operaciones inválidas, como confirmar una reserva previamente cancelada.

4.5 Panel de resultados
Muestra los resultados de todas las operaciones realizadas por el usuario, incluyendo registros, consultas y detalles de las reservas


5. Flujo de uso recomendado
5.1	Registrar uno o varios clientes. 
5.2	Registrar uno o varios servicios. 
5.3	Crear una o varias reservas reserva. 
5.4	Consultar las reservas registradas. 
5.5	Confirmar o cancelar alguna reserva según corresponda. 
5.6	Consultar nuevamente el estado actualizado de la reserva. 

