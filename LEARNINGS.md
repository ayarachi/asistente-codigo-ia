# 📚 Aprendizajes: Asistente de Código con IA

## 🎯 El problema que enfrenté

Cuando estaba aprendiendo a programar, los mensajes de error de Python eran confusos y frustrantes. Pasaba mucho tiempo buscando en StackOverflow qué significaba cada error, lo que interrumpía mi flujo de aprendizaje. Necesitaba una forma más rápida de entender mis errores.

## Decisiones técnicas clave

### Por qué elegí Google Gemini sobre otras APIs

1. **Cuota gratuita generosa:** 15 requests/minuto, 1500/día - suficiente para aprender
2. **Documentación clara:** Más fácil de implementar que OpenAI para un primer proyecto
3. **No requiere tarjeta de crédito:** Podía empezar inmediatamente
4. **Modelos actualizados:** gemini-2.5-flash es rápido y económico

### Por qué elegí CLI sobre interfaz web

- Quería aprender las bases antes de agregar complejidad
- Un CLI es más rápido de implementar y probar
- Puedo integrarlo en mi workflow de terminal
- Menos distracciones, más foco en la funcionalidad core

## Obstáculos que superé

### 1. Error 404 con modelos de Gemini

**Problema:** El modelo `gemini-1.5-flash` no existía en mi región.

**Solución:** Creé un script (`verificar_modelos.py`) para listar modelos disponibles y descubrí que debía usar `gemini-2.5-flash`.

**Aprendizaje:** Siempre verificar la disponibilidad de recursos antes de asumir que funcionan.

### 2. Confusión entre librerías de Google

**Problema:** La documentación antigua usaba `google.generativeai` pero ya estaba deprecada.

**Solución:** Cambié a la nueva librería `google-genai` con sintaxis actualizada.

**Aprendizaje:** Las APIs de IA cambian rápido. Siempre verificar la fecha de la documentación.

### 3. Gestión de credenciales

**Problema:** No sabía cómo manejar API keys de forma segura.

**Solución:** Aprendí a usar `.env` + `.gitignore` para proteger credenciales.

**Aprendizaje:** La seguridad no es opcional, es parte del proceso desde el día 1.

## 💡 3 cosas que aprendí sobre LLMs

### 1. El prompt es el 80% del resultado

Un prompt vago como "explica este error" da respuestas genéricas. Un prompt estructurado con contexto específico ("Soy estudiante de programación...") da respuestas mucho más útiles y adaptadas.

### 2. Los LLMs no son mágicos

Fallan, dan respuestas incorrectas, y necesitan ser testeados. No puedo asumir que la respuesta del modelo es correcta - necesito validarla, especialmente para código.

### 3. El costo importa

Aunque Gemini es gratuito para desarrollo, aprendí a ser consciente de los límites de requests. Cada llamada cuenta, y optimizar prompts para obtener la respuesta correcta en el primer intento es importante.

## 🔄 Qué haría diferente en v2

### Mejoras técnicas:

- **Agregar tests unitarios** para asegurar que las funciones manejan casos edge
- **Implementar caché** para errores comunes y evitar requests repetidos
- **Agregar más contexto** al prompt (tipo de error, nivel de experiencia del usuario)
- **Soporte multi-lenguaje** (no solo Python)

### Mejoras de UX:

- **Interfaz web simple** (Streamlit) para usuarios no técnicos
- **Historial de consultas** con búsqueda
- **Modo "aprendizaje"** que explica conceptos además de solo corregir

### Mejoras de proceso:

- **Documentar desde el día 1** en lugar de al final
- **Hacer commits más pequeños** (cada feature individual)
- **Agregar ejemplos** en el README desde el inicio

## 📊 Métricas del proyecto

- **Tiempo total:** ~5 horas distribuidas en 3 días
- **Tiempo efectivo por día:** 20-30 minutos
- **Líneas de código:** ~150
- **Commits:** 5
- **Errores resueltos:** 8 (404 modelos, gitignore, librerías, venv, etc.)

## 🎓 Skills desarrollados

### Técnicos:

- ✅ Integración de APIs REST
- ✅ Manejo de variables de entorno
- ✅ Gestión de dependencias con pip
- ✅ Control de versiones con Git
- ✅ Documentación técnica

### Blandos:

- ✅ Troubleshooting sistemático
- ✅ Lectura de documentación técnica
- ✅ Persistencia ante errores
- ✅ Gestión de proyecto pequeño
- ✅ Capacidad de cerrar (no perfectionism paralysis)

## 🚀 Siguiente nivel

Este proyecto fue un punto de partida. Los próximos pasos en mi aprendizaje:

1. **Proyecto 2:** Integración con Notion API (automatizaciones)
2. **Aprender sobre:** Prompting avanzado y context management
3. **Explorar:** Fine-tuning de modelos para casos específicos
4. **Construir:** Portfolio de 4-5 proyectos pequeños y cerrados

---

_Fecha de creación: 4 de febrero, 2026_  
_Proyecto cerrado: Pendiente (6 de febrero)_
