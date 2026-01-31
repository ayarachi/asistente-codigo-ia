from google import genai
import os
from dotenv import load_dotenv

# Carga tu API key
load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def explicar_error(codigo, error):
    """
    Toma código con error y lo explica
    """
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

# Prueba tu asistente
if __name__ == "__main__":
    codigo_con_error = """
def sumar(a, b):
    resultado = a + b
    return resultado
    
print(sumar(5))  # ¡Error! Falta un argumento
"""
    
    mensaje_error = "TypeError: sumar() missing 1 required positional argument: 'b'"
    
    print("🤖 ASISTENTE DE CÓDIGO\n")
    print("Analizando tu error...\n")
    
    try:
        explicacion = explicar_error(codigo_con_error, mensaje_error)
        print(explicacion)
    except Exception as e:
        print(f"❌ Error al conectar con Gemini: {e}")
        print("\nVerifica que tu API key esté correcta en el archivo .env")
