---
description: Prototipo de pruebas manuales para el CEO
---

# 🚀 Protocolo de Pruebas Manuales (CEO Edition)

Este workflow define cómo validar los cambios visuales y funcionales ahora que Antigravity no realiza grabaciones de navegador.

## Pasos para la Validación

1. **Notificación de Hito**: Antigravity te avisará cuando un cambio esté listo para ser probado.
2. **Acceso Local**: Abre o refresca [http://localhost:3000](http://localhost:3000) en tu navegador.
3. **Checklist Visual**:
    - [ ] ¿La estética es "Premium/Wowsome"?
    - [ ] ¿Las animaciones son fluidas?
    - [ ] ¿El diseño responde correctamente a diferentes tamaños?
4. **Feedback**:
    - Si todo es correcto, simplemente di: "Validado" o "Continúa".
    - Si hay fallos, descríbelos o pega un pantallazo. Antigravity ajustará el código basándose en tu descripción.

// turbo
5. **Comando de Verificación**: Puedes pedirle a Antigravity que ejecute `npm run build` si quieres asegurar que no hay errores de tipado o compilación antes de dar tu OK.
