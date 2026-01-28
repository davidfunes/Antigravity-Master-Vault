---
name: performance-expert
description: Especialista en Core Web Vitals, Optimización de Assets y Eficiencia en Next.js.
---

# ⚡ Skill: Experto en Rendimiento Web (Protocolo Antigravity)

Esta skill garantiza que la experiencia del usuario sea instantánea, fluida y eficiente, maximizando los Core Web Vitals y la retención.

## 🧠 Mentalidad del Experto
- **Cada milisegundo cuenta**: El rendimiento es una característica, no una tarea secundaria.
- **Percepción vs Realidad**: La carga progresiva y los esqueletos (skeletons) son tan importantes como el tiempo de carga absoluto.
- **Eficiencia de Recursos**: No cargues lo que no se ve. No proceses lo que no es necesario.

## 🛠️ Protocolos de Acción

### 1. Core Web Vitals (CWV)
- [ ] **LCP (Largest Contentful Paint)**: Priorizar la carga de la imagen principal o texto hero. Usar `priority` en `next/image`.
- [ ] **INP (Interaction to Next Paint)**: Minimizar el bloqueo del hilo principal por JavaScript pesado (especialmente en animaciones).
- [ ] **CLS (Cumulative Layout Shift)**: Reservar espacio para imágenes y elementos dinámicos para evitar saltos visuales.

### 2. Optimización de Assets (Imágenes y Vídeo)
- [ ] **Next/Image**: Uso obligatorio de componentes de imagen optimizados con formatos modernos (WebP/AVIF).
- [ ] **Responsive Sizes**: Configurar el atributo `sizes` para no descargar imágenes más grandes de lo necesario.
- [ ] **Lazy Loading**: Asegurar que todo contenido fuera del viewport se cargue bajo demanda.
- [ ] **Vídeo Eficiente**: Usar formatos comprimidos y evitar el autoplay sin mute para no penalizar el ancho de banda.

### 3. Código y Paquetes
- [ ] **Tree Shaking**: Eliminar código muerto y librerías redundantes.
- [ ] **Code Splitting**: Cargar dinámicamente componentes pesados (ej. reproductores de audio o carruseles de vídeo).
- [ ] **Font Optimization**: Usar `next/font` para evitar el destello de texto sin formato (FOUT).

### 4. Estrategia de Cache y Delivery
- [ ] **Static Generation (SSG)**: Preferir páginas estáticas siempre que sea posible.
- [ ] **Edge Delivery**: Aprovechar la CDN para servir contenido cerca del usuario.
- [ ] **Hydration Strategy**: Minimizar el JS necesario para la hidratación inicial.

## 🎨 Estándares "Wowsome" para el CEO
- La navegación debe sentirse como una aplicación nativa: instantánea y sin fricciones.
- Los efectos visuales y granos de fondo deben estar optimizados para no consumir excesiva CPU/GPU en dispositivos móviles.

## 🚫 Prohibido
- Imágenes de más de 200KB sin una justificación artística extrema.
- Librerías de terceros sin analizar su impacto en el bundle size.
- Scroll blocking innecesario por JS.
- Olvidar la optimización de animaciones CSS (usar `transform` y `opacity`).
