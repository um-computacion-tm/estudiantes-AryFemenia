print("DATOS PROFESOR")
########################################################
##############CLASE PROFESOR
########################################################
class Profesor:
    def __init__(self, param_nombre, param_email):
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def asistencia_clase(self):
        self.asistencia += 1

profesor_pepe:Profesor = Profesor("Pepe", "jose@um.edu.ar")
print(id(profesor_pepe))
print("el nombre del profesor es:",profesor_pepe.nombre)
print("el email del profesor es:",profesor_pepe.email)
print("su asistencia del profesor es:",profesor_pepe.asistencia)

#ejemplo asistencia
print("EL PROFESOR FUE A CLASE...")
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()

print("la asistencia del profesor es: ")
print(profesor_pepe.asistencia)

print()
print("DATOS ALUMNO")
########################################################
################CLASE ALUMNO
########################################################
class Alumno:
    def __init__(self, param_nombre, param_email, param_legajo):
        self.nombre = param_nombre
        self.email = param_email
        self.legajo = param_legajo
        self.asistencia = 0

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def cambiar_legajo(self, param_legajo):
        self.legajo = param_legajo

    def asistencia_clase(self):
        self.asistencia += 1

alumno_juan:Alumno = Alumno("Juan", "juan@alumno.um.edu.ar", "42611")
print(id(alumno_juan))
print("el nombre del alumno es: ")
print(alumno_juan.nombre)
print("el email del alumno es: ")
print(alumno_juan.email)
print("el legajo del alumno es: ")
print(alumno_juan.legajo)
print("la asistencia del alumno es: ")
print(alumno_juan.asistencia)

print("EL ALUMNO FUE A CLASE...")
alumno_juan.asistencia_clase()

print("la asistencia del alumno es: ")
print(alumno_juan.asistencia)

print()
print("DATOS MATERIA")
########################################################
###############CLASE MATERIA
########################################################
#agregar materia a alumno usando el metodo de selF


print()
print("DATOS HERENCIA")
########################################################
##############CLASE HERENCIA
########################################################
#super es para tener preferencia en crear 
'''
class Profesor(Persona):
    def __init__(self, param_nombre, paran_email):
        self.legajo_empleado = legajo_empleado
        super().__init__(param_nombre, param_email)
'''
