# Chat IA

Un chatbot inteligente que integra múltiples modelos de IA para brindar respuestas personalizadas a los clientes.

## Descripción

Este proyecto implementa un chatbot capaz de conectarse con diferentes modelos de inteligencia artificial como ChatGPT, Claude y Gemini para responder consultas de clientes. El sistema selecciona automáticamente el modelo más adecuado según el tipo de pregunta o puede combinar respuestas de varios modelos para obtener la mejor respuesta posible.

## Características

- Integración con múltiples modelos de IA (OpenAI/ChatGPT, Anthropic/Claude, Google/Gemini)
- Interfaz de chat intuitiva
- Enrutamiento inteligente de consultas al modelo más adecuado
- Posibilidad de combinar respuestas de varios modelos
- Personalización del tono y estilo de respuestas

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/dasalazarr/Chat-IA.git
cd Chat-IA

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno (API keys)
cp .env.example .env
# Editar el archivo .env con tus claves API
```

## Uso

```bash
# Iniciar la aplicación
python app.py
```

Abrir http://localhost:5000 en el navegador.

## Estructura del Proyecto

```
Chat-IA/
├── app.py                  # Aplicación principal
├── config.py               # Configuración del proyecto
├── requirements.txt        # Dependencias
├── .env.example            # Plantilla para variables de entorno
├── static/                 # Archivos estáticos
│   ├── css/                # Estilos
│   └── js/                 # JavaScript
├── templates/              # Plantillas HTML
├── models/                 # Módulos para cada modelo de IA
│   ├── openai_model.py     # Integración con OpenAI/ChatGPT
│   ├── anthropic_model.py  # Integración con Anthropic/Claude
│   └── google_model.py     # Integración con Google/Gemini
└── utils/                  # Utilidades
    ├── router.py           # Enrutador de consultas
    └── response_mixer.py   # Combinador de respuestas
```

## Configuración

Para usar este chatbot, necesitarás obtener claves API para los servicios que desees integrar:

- [OpenAI API](https://platform.openai.com/)
- [Anthropic API](https://www.anthropic.com/product)
- [Google AI Studio (Gemini)](https://ai.google.dev/)

## Licencia

MIT