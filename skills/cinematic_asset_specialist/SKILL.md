---
name: cinematic_asset_specialist
description: Especialista en la generación de activos visuales cinemáticos y coherentes para proyectos de audio. Traducción de conceptos musicales en prompts visuales de alta gama.
---

# 🧠 Instrucciones de la Habilidad: Cinematic Asset Specialist

Esta habilidad permite al agente transformar la atmósfera de un proyecto musical en activos visuales potentes, coherentes y de grado profesional.

## 🎯 Objetivos de la Habilidad
- **Coherencia Atmosférica**: Traducir adjetivos musicales (ej. "glitchy", "epic orchestral", "noir") en descriptores visuales precisos.
- **Calidad de Prompting**: Generar prompts para `generate_image` que utilicen terminología fotográfica y cinematográfica (ej. "anamorphic lens", "vray render", "8k hyper-realistic").
- **Asset Alignment**: Asegurar que las imágenes generadas se ajusten a la estructura de la web (fondos 16:9, retratos 4:5, etc.).

## 🏗️ Arquitectura y Flujo: Traducción Sensorial
1.  **Input Audio/Concept**: El agente recibe información sobre el estilo musical o el propósito de la sección.
2.  **Mapeo Visual**: Se asignan paletas de colores y estilos (ej. Futurista -> Neon/Carbon Fiber; Épico Studio -> Warm lighting/Dust motes).
3.  **Refinamiento de Prompt**: Se construye el prompt final añadiendo modificadores de calidad técnica.
4.  **Generación**: Se invoca a la herramienta de generación de imágenes.

## 🛠️ Uso y Comandos
Activa esta habilidad cuando necesites:
- Cambiar un fondo de sección cinemático.
- Crear portadas para nuevos tracks o álbumes.
- Generar assets visuales para el blog de estudio.

## 🧪 Protocolo de Verificación
1. **Prueba A**: ¿La imagen generada evoca el mismo sentimiento que la música del proyecto?
2. **Prueba B**: ¿Mantiene la coherencia de color con el resto de la web?

## 📜 Estructura de Archivos
- `SKILL.md`: Diccionario de traducción visual-sonora.
- `resources/`: Librería de estilos visuales predefinidos (Dark Synth, Orchestral Gold, etc.).
- `examples/`: Prompts de éxito para secciones de la web.

## ⚠️ Consideraciones Especiales
Idioma: Español para el razonamiento; Prompts finales en Inglés para máxima compatibilidad con motores de generación.
