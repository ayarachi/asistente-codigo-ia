# 🤖 Asistente de Código con IA

Mi primer proyecto integrando Large Language Models (LLMs) en Python. Este proyecto surgió de mi deseo de superar un estancamiento profesional y aprender a trabajar con IA de forma práctica.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![Status](https://img.shields.io/badge/Status-v1.0_Ready-success)

---

## 📖 ¿Qué hace este proyecto?

Este asistente utiliza Google Gemini (un LLM) para ayudar a desarrolladores a entender y corregir errores en su código Python.

**Características:**

- ✅ Explica errores en lenguaje simple
- ✅ Identifica qué está mal en el código
- ✅ Proporciona código corregido
- ✅ Versión interactiva donde el usuario ingresa su propio código
- ✅ Modo "Explicar código": analiza código sin errores para aprender

---

## 🛠️ Tecnologías utilizadas

- **Python 3.x**
- **Google Gemini API** (`google-genai`) - Para procesamiento de lenguaje natural
- **python-dotenv** - Para manejo seguro de variables de entorno
- **Git/GitHub** - Control de versiones

---

## 📦 Instalación

### **Requisitos previos:**

- Python 3.x instalado
- Una API key de Google Gemini ([Obtener aquí](https://aistudio.google.com/app/apikey))

### **Paso 1: Clona el repositorio**

``bash
git clone https://github.com/ayarachi/asistente-codigo-ia.git
cd asistente-codigo-ia

````

### **Paso 2: Crea y activa el entorno virtual**

**En Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
````

**En Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**💡 Nota:** Verás `(venv)` al inicio de tu línea de comando cuando el entorno esté activo.

**Para desactivar el entorno virtual:**

```bash
deactivate
```

### **Paso 3: Instala las dependencias**

```bash
pip3 install -r requirements.txt
```

O si prefieres instalarlas manualmente:

```bash
pip3 install google-genai python-dotenv
```

### **Paso 4: Configura tu API key**

1. Ve a https://aistudio.google.com/app/apikey
2. Genera una API key
3. Crea un archivo `.env` en la raíz del proyecto:

```bash
touch .env
```

4. Abre el archivo `.env` y agrega tu clave:

```
GOOGLE_API_KEY=tu-clave-aquí
```

⚠️ **IMPORTANTE:** Nunca compartas tu archivo `.env` ni lo subas a GitHub.

---

## 🚀 Uso

### **Versión 1: Con código de ejemplo (asistente.py)**

```bash
python3 asistente.py
```

Este script ejecuta un ejemplo predefinido y muestra cómo funciona el asistente.

### **Versión 2: Interactiva (asistente_interactivo.py)**

```bash
python3 asistente_interactivo.py
```

**Flujo de uso:**

1. El programa te pedirá que pegues tu código con error
2. Presiona Enter en una línea vacía cuando termines
3. Ingresa el mensaje de error que recibiste
4. ¡El asistente te dará una explicación detallada!

---

## 📚 Ejemplos de uso

### **Ejemplo 1: Variable mal escrita**

**Código con error:**

```python
def saludar(nombre):
    mensaje = f"Hola {nombre}!"
    print(mesaje)  # Error de tipeo
```

**Error:**

```
NameError: name 'mesaje' is not defined
```

**El asistente te explicará:**

- Qué significa el error
- Que escribiste "mesaje" en lugar de "mensaje"
- Te dará el código corregido

---

## 🧠 Lo que aprendí construyendo este proyecto

### **Conceptos técnicos:**

- ✅ Qué son los LLMs (Large Language Models) y cómo funcionan
- ✅ Integración de APIs externas en Python
- ✅ Manejo seguro de credenciales con variables de entorno
- ✅ Entornos virtuales en Python (venv)
- ✅ Control de versiones con Git y GitHub

### **Habilidades desarrolladas:**

- ✅ Troubleshooting real de problemas de configuración
- ✅ Lectura de documentación técnica
- ✅ Manejo de errores con try/except
- ✅ Diseño de prompts efectivos para LLMs
- ✅ Documentación de proyectos

### **Desafíos superados:**

- 🔥 Error 404 con modelos de Gemini → Solucionado identificando modelos disponibles
- 🔥 Problemas con Git y .gitignore → Aprendí a proteger credenciales
- 🔥 Confusión entre librería antigua y nueva de Google → Actualicé a google-genai
- 🔥 Gestión de entornos virtuales → Entendí la importancia de aislar dependencias

---

## 📁 Estructura del proyecto

```
asistente-codigo-ia/
├── .env                      # Variables de entorno (NO subir a Git)
├── .gitignore                # Archivos a ignorar en Git
├── README.md                 # Este archivo
├── requirements.txt          # Dependencias del proyecto
├── asistente.py              # Versión con ejemplo predefinido
├── asistente_interactivo.py  # Versión interactiva
├── verificar_modelos.py      # Script para listar modelos disponibles
└── venv/                     # Entorno virtual (NO subir a Git)
```

---

## 🎯 Próximos pasos

- [x] Crear proyecto base con API de Gemini
- [x] Hacer versión interactiva del asistente
- [x] Agregar soporte para explicar código sin errores
- [ ] Guardar historial de consultas en archivo
- [ ] Implementar análisis de múltiples lenguajes
- [ ] Crear interfaz web con Streamlit
- [ ] Agregar tests unitarios

## 🔐 Seguridad

Este proyecto implementa buenas prácticas de seguridad:

- ✅ API keys almacenadas en `.env` (no en el código)
- ✅ `.env` incluido en `.gitignore`
- ✅ Documentación clara sobre protección de credenciales

**Nunca compartas tu API key públicamente.**

---

## 🔧 Cómo integrar esto en tu workflow diario

### **Caso 1: Durante desarrollo**

Cuando te salga un error mientras programas:

1. Copia tu código
2. Copia el mensaje de error
3. Ejecuta: `python3 asistente_interactivo.py`
4. Opción 1 → Pega código → Pega error
5. Lee la explicación y aplica la solución

**Tiempo ahorrado:** 5-15 minutos vs buscar en StackOverflow

### **Caso 2: Aprendiendo código nuevo**

Cuando encuentres código que no entiendes (tutorial, repo, etc.):

1. Copia el fragmento de código
2. Ejecuta: `python3 asistente_interactivo.py`
3. Opción 2 → Pega el código
4. Aprende qué hace cada parte

**Beneficio:** Entiendes código antes de copiarlo ciegamente

### **Caso 3: Code review**

Antes de hacer PR, revisa tu código:

1. Copia tu función/módulo
2. Opción 2 para verificar si es claro
3. Usa los tips de mejora sugeridos

---

---

## 📄 Licencia

MIT License - Siéntete libre de usar este código para aprender.

---

## 👩‍💻 Autora

**Eliana Ayarachi**

- GitHub: [@ayarachi](https://github.com/ayarachi)
- Ubicación: Buenos Aires, Argentina
- Proyecto: Parte de mi journey para superar el estancamiento profesional y dominar el desarrollo con IA

---

## 📊 Progreso del proyecto

**Inicio del proyecto:** 30 de enero, 2026  
**Última actualización:** 4 de febrero, 2026

### **Timeline:**

- **Día 1 (30/01):** ✅ Configuración inicial, integración de Gemini API
- **Día 2 (02/02):** ✅ Versión interactiva, README completo
- **Día 3 (03/02):** ✅ Feature explicar código, requirements.txt
- **Día 4 (04/02):** ✅ LEARNINGS.md completo

---

_"El estancamiento se supera con acción constante, no con planes perfectos."_
