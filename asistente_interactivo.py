from google import genai
import os
from dotenv import load_dotenv

# Carga tu API key
load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def explicar_error(codigo, error):
    """Explica un error de código"""
    prompt = f"""
Soy estudiante de programación y tengo este error:

CÓDIGO:
{codigo}

ERROR:
{error}

Por favor:
1. Explícame qué significa el error en palabras simples
2. Muéstrame qué está mal en mi código
3. Dame el código corregido
"""
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    return response.text

def explicar_codigo_limpio(codigo):
    """Explica código que funciona (sin errores)"""
    prompt = f"""
Soy estudiante de programación y quiero entender este código:

CÓDIGO:
{codigo}

Por favor:
1. Explícame qué hace este código en lenguaje simple
2. Describe cada parte importante
3. Dame tips de cómo podría mejorarse
"""
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    return response.text

def main():
    print("╔═══════════════════════════════════════════╗")
    print("║   🤖 ASISTENTE DE CÓDIGO INTERACTIVO   ║")
    print("╚═══════════════════════════════════════════╝")
    print()
    print("Elige una opción:")
    print("1. Explicar un error en mi código")
    print("2. Explicar código que funciona")
    print()
    
    opcion = input("Tu elección (1 o 2): ")
    print()
    
    if opcion == "1":
        print("📝 Pega tu código con error (termina con línea vacía):")
        print()
        
        lineas = []
        while True:
            try:
                linea = input()
                if linea == "":
                    break
                lineas.append(linea)
            except EOFError:
                break
        
        codigo = "\n".join(lineas)
        
        if not codigo.strip():
            print("❌ No ingresaste código")
            return
        
        print()
        print("🐛 Ahora pega el mensaje de error:")
        error = input()
        
        if not error.strip():
            print("❌ No ingresaste error")
            return
        
        print()
        print("⏳ Analizando...")
        print()
        
        try:
            explicacion = explicar_error(codigo, error)
            print("═" * 50)
            print(explicacion)
            print("═" * 50)
            
        except Exception as e:
            print(f"❌ Error: {e}")
    
    elif opcion == "2":
        print("📝 Pega tu código (termina con línea vacía):")
        print()
        
        lineas = []
        while True:
            try:
                linea = input()
                if linea == "":
                    break
                lineas.append(linea)
            except EOFError:
                break
        
        codigo = "\n".join(lineas)
        
        if not codigo.strip():
            print("❌ No ingresaste código")
            return
        
        print()
        print("⏳ Analizando...")
        print()
        
        try:
            explicacion = explicar_codigo_limpio(codigo)
            print("═" * 50)
            print(explicacion)
            print("═" * 50)
            
        except Exception as e:
            print(f"❌ Error: {e}")
    
    else:
        print("❌ Opción inválida. Usa 1 o 2.")

if __name__ == "__main__":
    main()