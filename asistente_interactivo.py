from google import genai
import os
from dotenv import load_dotenv

# Carga tu API key
load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def explicar_error(codigo, error):
    """
    Toma código con error y lo explica usando Gemini
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

def main():
    print("╔═══════════════════════════════════════════╗")
    print("║   🤖 ASISTENTE DE CÓDIGO INTERACTIVO   ║")
    print("╔═══════════════════════════════════════════╗")
    print()
    print("📝 Pega tu código con error (termina con una línea vacía):")
    print()
    
    # Recolectar el código línea por línea
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
        print("❌ No ingresaste ningún código. Intenta de nuevo.")
        return
    
    print()
    print("🐛 Ahora pega el mensaje de error:")
    error = input()
    
    if not error.strip():
        print("❌ No ingresaste ningún error. Intenta de nuevo.")
        return
    
    print()
    print("⏳ Analizando tu código...")
    print()
    
    try:
        explicacion = explicar_error(codigo, error)
        print("═" * 50)
        print(explicacion)
        print("═" * 50)
        print()
        print("✅ ¡Análisis completado!")
        
    except Exception as e:
        print(f"❌ Error al conectar con Gemini: {e}")
        print("\n💡 Verifica que tu API key esté correcta en el archivo .env")

if __name__ == "__main__":
    main()