# 🚀 SKILL: Release Master (Ciclo de Vida Senior+)

Esta habilidad dota al agente de la capacidad de gestionar el ciclo de vida completo de un cambio: desde el commit atómico hasta el despliegue en producción, siguiendo los estándares de excelencia de Marcha Fúnebre.

## 🎯 Propósito
Garantizar que cada cambio sea trazable, seguro y se despliegue sin errores humanos, manteniendo la integridad de la base de datos y la experiencia del usuario.

## 🧠 Mentalidad: El Tono Antigravity
- **Atómico**: Commits pequeños y con un único propósito.
- **Seguro**: Los tests son ley. Nunca se despliega con fallos.
- **Trazable**: Uso estricto de tags y registros de cambios (Changelogs).
- **Automatizado**: Preferencia por scripts y GitHub Actions sobre comandos manuales.

## 🛡️ Reglas de Oro de Ejecución

### 1. Commits (Conventional Commits)
Todo commit debe seguir el formato: `<tipo>(<ámbito>): <descripción>`
- `feat`: Nueva funcionalidad.
- `fix`: Corrección de errores.
- `chore`: Tareas de mantenimiento (dependencias, configuraciones).
- `docs`: Cambios en documentación.
- `style`: Cambios visuales que no afectan la lógica.

### 2. Validaciones Críticas (Pre-Commit & Pre-Release)
Antes de cualquier commit o release, es **mandatorio**:
1. **Tests**: `npm run test` para asegurar lógica impecable.
2. **Build Local**: `npm run build`. No confíes solo en los tests; los errores de tipado de TypeScript (frecuentes en el Pipeline) solo se detectan aquí.

### 3. El Flujo de Release e Integridad
1. **Narrativa**: Invocar `SKILL: Changelog Expert` para el contenido.
2. **Ejecución**: Usar **estrictamente** `npm run release`. 
   - Prohibido usar `standard-version` directamente.
   - El script unificado (`release.sh`) se encarga de: versionar, sincronizar `public/CHANGELOG.md`, crear el tag y hacer el push.
3. **Validación**: La versión en `package.json` es la **Única Fuente de Verdad**.

### 4. Producción (Trigger Awareness)
- **Push != Deploy**: Un simple `git push` solo valida el código en GitHub.
- **Tag = Deploy**: El paso a producción en Firebase **SOLO** se activa mediante un Tag de Versión (`vX.Y.Z`). Si quieres ver los cambios en la web, DEBES hacer un release formal.

## 🛠️ Procedimiento Experto
1. **Auditoría**: `git status` y `git diff` para entender el alcance.
2. **Blindaje**: `npm run test` && `npm run build`.
3. **Commit/Release**: Decidir si es un fix atómico o un hito de versión.
4. **Push Maestro**: `git push --follow-tags origin main`.
