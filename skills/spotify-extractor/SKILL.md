---
name: spotify-extractor
description: "Habilidad especializada en el mapeo de metadatos de Spotify hacia fuentes de audio públicas (YouTube) para permitir descargas sin conflictos de DRM."
---

# 🎵 Skill: Spotify Audio Extractor

Esta habilidad permite al agente identificar, analizar y procesar enlaces de Spotify (Tracks, Álbumes y Playlists) para su posterior descarga utilizando YouTube como fuente de audio.

## 🧠 Lógica de Funcionamiento

El proceso se divide en tres fases críticas para garantizar la máxima calidad y fidelidad:

1. **Detección de Enlaces**:
   - Identificar URLs tipo `open.spotify.com/track/...`, `/album/...` o `/playlist/...`.
   - Normalizar la URL eliminando parámetros de rastreo (`?si=...`).

2. **Extracción de Metadatos (Bypass DRM)**:
   - **IMPORTANTE**: No intentar acceder al stream de audio directo de Spotify (bloqueado por DRM).
   - Utilizar `yt-dlp` con `extract_flat: True` para obtener exclusivamente el título de la canción y el artista.
   - En el caso de Álbumes/Playlists, realizar una extracción plana para obtener la lista de entradas sin procesar cada track individualmente.

3. **Mapeo Spotify -> YouTube (Método MediaHuman/spotDL)**:
   - Construir una consulta de búsqueda altamente específica: `ytsearch1:{Artista} {Canción} Official Audio`.
   - Utilizar el primer resultado de YouTube/YouTube Music para obtener la URL del video.
   - Si la extracción de metadatos de Spotify falla por DRM, utilizar el título preliminar capturado en la fase de expansión para forzar la búsqueda.
   - Preservar los metadatos originales de Spotify (incluyendo portada) para el etiquetado del archivo final, ignorando los de YouTube.

## 🛠️ Herramientas y Configuraciones Recomendadas

- **yt-dlp**: Motor principal.
- **Configuración ydl_opts para Spotify**:
  ```python
  {
      'extract_flat': True,
      'ignoreerrors': True,
      'quiet': True
  }
  ```

## ⚠️ Restricciones Éticas y Técnicas

- Prohibido intentar el bypass de DRM mediante ingeniería inversa de los reproductores oficiales.
- El mapeo debe basarse en la búsqueda de contenido equivalente en plataformas de alojamiento público de video (YouTube/Music).
- Priorizar siempre la fidelidad de los metadatos de Spotify sobre los de YouTube para mantener la organización de la biblioteca del usuario.
