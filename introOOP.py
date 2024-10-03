class Persona:
    def __init__(self, nombre, edad, genero, ocupacion,oN): #<-------------Esto es un constructor
        # Se definen con self.Atributos de la clase Persona
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.ocupacion = ocupacion
        self.oN
    # Método para saludar
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}.")
        #return f"Hola, mi nombre es {self.nombre}."

    # Método para mostrar la edad
    def mostrar_edad(self):
        print(f"Tengo {self.edad} años.")

    # Método para cambiar la ocupación
    def cambiar_ocupacion(self, nueva_ocupacion):
        self.ocupacion = nueva_ocupacion
        print(f"Mi nueva ocupación es {self.ocupacion}.")

    # Método para presentarse completamente
    def presentarse(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años, soy {self.genero} y trabajo como {self.ocupacion}.")

    # Método para verificar si es mayor de edad
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} no es mayor de edad.")

    #Mandar saludo
    def mandar_saludo(oN):
        print(f"Hola {self.nombre}, te manda a saludar,{self.oN}")

# Crear una instancia de la clase Persona
persona1 = Persona("Carlos", 25, "masculino", "ingeniero")
persona2 = Persona("Juan", 19, "masculino", "Estudiante")
#persona3 = Persona("Victor", 10, "masculino", "Docente")
#persona4 = Persona("Brenda", 25, "femenino", "Secretaria")
# Usar los métodos de la clase
persona1.saludar( )               # "Hola, mi nombre es Carlos."
persona1.mostrar_edad()           # "Tengo 25 años."
persona1.presentarse()            # "Soy Carlos, tengo 25 años, soy masculino y trabajo como ingeniero."
persona1.cambiar_ocupacion("profesor")  # "Mi nueva ocupación es profesor."
persona1.es_mayor_de_edad() # "Carlos es mayor de edad."
print(persona1.mandar_saludo(persona2.nombre))
#las funciones dentro de una clase se conocen como metodos
print("\n")
"""persona2.saludar()
persona2.mostrar_edad()
persona2.presentarse()
persona2.cambiar_ocupacion("profesor")
persona2.es_mayor_de_edad()
print("\n")
persona3.saludar()
persona3.mostrar_edad()
persona3.presentarse()
persona3.cambiar_ocupacion("profesor")
persona3.es_mayor_de_edad()
print("\n")
persona4.saludar()
persona4.mostrar_edad()
persona4.presentarse()
persona4.cambiar_ocupacion("profesor")
persona4.es_mayor_de_edad()"""