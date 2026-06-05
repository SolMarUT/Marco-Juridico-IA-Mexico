
#! Proyecto AI-Legal-MX: Un programa de Python para explorar la intersección entre Inteligencia Artificial y Derecho en México.

def menu():

    while True:

        print("\n================================")
        print(" AI Y DERECHO EN MÉXICO ")
        print("================================")
        print("1. Protección de Datos Personales")
        print("2. Derechos Humanos e IA")
        print("3. Propiedad Intelectual e IA")
        print("4. Ciberseguridad")
        print("5. Ética en IA")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":

            print("\nPROTECCIÓN DE DATOS PERSONALES")
            print("Ley Federal de Protección de Datos Personales")
            print("Autoridad: INAI")
            print("https://www.inai.org.mx")

        elif opcion == "2":

            print("\nDERECHOS HUMANOS E IA")
            print("La IA debe respetar los derechos fundamentales")
            print("establecidos en la Constitución Mexicana.")

        elif opcion == "3":

            print("\nPROPIEDAD INTELECTUAL E IA")
            print("Institución responsable: IMPI")
            print("https://www.gob.mx/impi")

        elif opcion == "4":

            print("\nCIBERSEGURIDAD")
            print("La protección de sistemas y datos es fundamental")
            print("en aplicaciones de Inteligencia Artificial.")

        elif opcion == "5":

            print("\nÉTICA EN IA")
            print("Los sistemas de IA deben ser transparentes,")
            print("responsables y supervisados por humanos.")

        elif opcion == "6":

            print("\nGracias por utilizar AI-Legal-MX")
            break

        else:

            print("\nOpción no válida")


menu()