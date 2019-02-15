diccionario = {1:'hola', 
                2:'mundo',
                3:'desde',
                'cuatro':'diccionarios'}

print(type(diccionario))

print(diccionario["cuatro"])

for keys, value in diccionario.items():
    print(f"""llave {keys}: valor - {value}""")

persona = {}

persona['Nombre'] = "Cesar"
persona['Apellido'] = "Perez"
persona['Edad'] = 20
persona['Edad'] = 21

for datos, value in persona.items():
    print(f"""{datos} - {value}""")

persona['Correo'] = "cesar_dany2009@hotmail.com"

if "Correo" in persona:
    print(f"el correo es {persona['Correo']}")
else:
    print("No tiene correo")

if persona.get("Altura") == None:
    persona["Altura"]="1.70mts"

print(persona.get("Altura"))