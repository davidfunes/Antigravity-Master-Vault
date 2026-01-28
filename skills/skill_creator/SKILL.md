---
name: skill_creator
description: Meta-Habilidad especializada en la generación, estandarización y arquitectura de nuevas capacidades modulares para el ecosistema ANTIGRAVITY.
---

# 🌀 Meta-Skill: Skill Creator

Esta es la "Semilla de Capacidades". Permite al agente (ANTIGRAVITY) expandir sus propias habilidades mediante la generación automatizada de módulos de conocimiento y ejecución.

## 🎯 Objetivos
- **Escalabilidad**: Crear nuevas habilidades en segundos.
- **Consistencia**: Asegurar que todas las habilidades sigan el mismo estándar premium.
- **Localización**: Garantizar que toda la documentación y lógica esté en español.

## 🏗️ Flujo de Trabajo Meta y Creación
1. **Identificación**: Detectar una necesidad recurrente (ej. optimización de audio, despliegue específico).
2. **Generación**: Se puede ejecutar el script `python3 skills/skill_creator/scripts/generate_skill.py <nombre> "<descripción>"` desde la raíz.
3. **Refinamiento**: El agente completa el `SKILL.md` generado siguiendo el estándar YAML frontmatter.
4. **Validación**: Se prueba la nueva habilidad y se integra en el flujo de trabajo.

## 🛠️ Uso y Comandos
Para crear una nueva habilidad:
```bash
python3 skills/skill_creator/scripts/generate_skill.py mi_nueva_habilidad "Descripción de lo que hace"
```

## 📜 Reglas de Oro
- **Naming**: Siempre en `snake_case`.
- **Idioma**: Siempre en **Castellano (Español)**.
- **Arquitectura**: Toda habilidad debe ser modular y no depender de otras a menos que sea estrictamente necesario.
- **Documentation**: El archivo `SKILL.md` es el contrato de ejecución del agente.

---
*Esta habilidad permite que la Antigravity Master Vault crezca con cada nuevo proyecto.*
