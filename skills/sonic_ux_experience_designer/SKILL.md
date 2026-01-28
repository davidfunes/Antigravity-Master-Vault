---
name: sonic_ux_experience_designer
description: Diseñador de experiencia de usuario sónica: micro-interacciones de interfaz, branding sonoro y cohesión estética-acústica.
---

# 🧠 Instrucciones de la Habilidad: Sonic Ux Experience Designer

Esta habilidad permite al agente diseñar e implementar capas de interacción sonora que conviertan la navegación en una experiencia inmersiva y memorable.

## 🎯 Objetivos de la Habilidad
- **Inmersión Interactiva**: Diseñar micro-sonidos para botones, hovers y modales que refuercen el feedback visual.
- **Narrativa Atmosférica**: Implementar transiciones sonoras entre secciones del sitio alineadas con los fondos cinemáticos.
- **Identidad Acústica**: Asegurar que todos los sonidos sigan una paleta tímbrica coherente con la marca David Funes.

## 🏗️ Arquitectura y Flujo
- **Entrada**: Assets de audio (WAV/MP3/OGG), eventos de la interfaz (React hooks).
- **Procesamiento**: Implementación de reproductores ligeros (Howler.js o similar) y lógica de "mute" global.
- **Salida**: Web audible de alta calidad sin comprometer el rendimiento.

## 🛠️ Uso y Comandos
Activa esta habilidad cuando necesites:
- Añadir efectos de sonido a un componente de la interfaz.
- Diseñar la lógica de reproducción de música de fondo o transiciones entre tracks.

## 🧪 Protocolo de Verificación
1. **Prueba A**: Comprobar que los sonidos no se solapan de forma caótica.
2. **Prueba B**: Validar que el botón de "Silencio" funciona globalmente y persiste en la sesión.

## 📜 Estructura de Archivos
- `SKILL.md`: Lógica de implementación sonora y UX.
- `scripts/`: Utilidades para compresión de audio web.
- `resources/`: Librerías de sonidos base (UI clicks, swooshes).

## ⚠️ Consideraciones Especiales
Idioma: Español obligatorio. Priorizar la sutileza: el sonido debe acompañar, no molestar.
