---
name: Web Design Analyzer & Executive Reporter
description: Habilidad especializada en la disección de sitios web para extraer patrones de diseño, estructura funcional y activos visuales, generando informes ejecutivos para inspiración y arquitectura de nuevos proyectos.
---

# 🕵️‍♂️ Skill: Web Design Analyzer

Esta habilidad capacita al agente para actuar como un **Analista de Producto y UX Senior**, capaz de descomponer cualquier sitio web de referencia en sus átomos constituyentes para alimentar el proceso creativo y técnico.

## 📋 Protocolo de Ejecución

Cuando el usuario proporcione una URL de referencia, se deben seguir estos pasos:

### 1. Exploración y Mapeo Estructural
- Utilizar `browser_subagent` para navegar por la página principal y secciones clave.
- Identificar la jerarquía de navegación (Menús, Sticky Bars, Footers).
- Listar las secciones por su propósito (Hero, Social Proof, Portfolio, Pricing, etc.).

### 2. Auditoría Visual (The DNA)
- **Paleta de Colores**: Identificar colores primarios, secundarios y de acento (HEX/HSL).
- **Tipografía**: Extraer las familias de fuentes (Headings vs Body) y escalas de tamaño.
- **Atmósfera**: Describir el estilo (Minimalista, Cinematic, Industrial, Glassmorphism, etc.).
- **Imágenes**: Identificar el tipo de assets (Fotografía real, Ilustración 3D, Vectores, Video backgrounds).

### 3. Análisis de Contenido y UX
- **Tono de Voz**: ¿Es corporativo, cercano, épico, técnico?
- **Estrategia de CTAs**: Ubicación y mensaje de los botones de acción.
- **Interacciones**: Notar micro-animaciones, efectos de hover o scroll dinámico.

## 📊 Plantilla de Informe Ejecutivo

El resultado de este análisis debe ser un documento markdown estructurado de la siguiente manera:

```markdown
# 📑 Informe Ejecutivo de Auditoría Web: [Nombre del Sitio]

## 🎯 Resumen Ejecutivo
Breve descripción del valor percibido y la "vibe" general del sitio.

## 🏗️ Estructura y Arquitectura
- **Layout**: (ej: Bento Grid, Single Column, Split Screen).
- **Secciones Críticas**: Lista de secciones identificadas.
- **Navegación**: Comportamiento del menú y flujo de usuario.

## 🎨 ADN Visual
| Elemento | Detalle |
| :--- | :--- |
| **Colores** | Listado de códigos y uso (fondo, acento, texto). |
| **Fuentes** | Familias detectadas. |
| **Assets** | Tipología de imágenes y tratamiento visual. |

## 💡 Insights para [Proyecto Actual]
3-5 puntos clave que podemos "robar" o adaptar para mejorar nuestro diseño actual basado en esta referencia.

## 📸 Capturas de Referencia
(Insertar imágenes capturadas con la herramienta de navegación si es posible).
```

## 🛠️ Herramientas de Apoyo
- `browser_subagent`: Para navegación visual y captura de DOM.
- `read_url_content`: Para extracción rápida de texto y metadatos SEO.
- `generate_image`: Para crear borradores basados en los estilos detectados.

---
**Protocolo de Calidad**: Nunca copies el sitio directamente. El objetivo es **analizar y destilar la esencia** para evolucionar nuestros propios diseños de forma original y premium.
