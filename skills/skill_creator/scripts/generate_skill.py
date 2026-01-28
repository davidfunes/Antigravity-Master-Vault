import os
import sys
import argparse
import re

def create_skill(name, description):
    # Validar nombre (snake_case)
    if not re.match(r'^[a-z0-9_]+$', name):
        print(f"Error: El nombre '{name}' debe ser snake_case (letras minúsculas, números y guiones bajos).")
        return

    # Obtener el directorio raíz del proyecto (donde está la carpeta skills)
    # Asumimos que el script se ejecuta desde la raíz o que podemos encontrarla
    cwd = os.getcwd()
    skills_root = os.path.join(cwd, "skills")
    
    if not os.path.exists(skills_root):
        print(f"Error: No se encontró el directorio 'skills' en {cwd}")
        return

    base_path = os.path.join(skills_root, name)
    
    if os.path.exists(base_path):
        print(f"Error: La habilidad '{name}' ya existe en {base_path}")
        return

    # Crear directorios
    directories = ["scripts", "examples", "resources"]
    for d in directories:
        os.makedirs(os.path.join(base_path, d), exist_ok=True)
        # Crear un .gitkeep para asegurar que se trackean si están vacíos
        with open(os.path.join(base_path, d, ".gitkeep"), "w") as f:
            pass
    
    # Leer plantilla
    template_path = os.path.join(skills_root, "skill_creator", "resources", "template_skill.md")
    if not os.path.exists(template_path):
        print(f"Error: No se encontró la plantilla en {template_path}")
        return

    with open(template_path, "r") as f:
        content = f.read()

    # Reemplazar placeholders
    content = content.replace("{{skill_name}}", name)
    content = content.replace("{{skill_description}}", description)
    content = content.replace("{{skill_title}}", name.replace("_", " ").title())
    content = content.replace("{{skill_detailed_description}}", description)
    content = content.replace("{{special_considerations}}", "Idioma: Español obligatorio. Seguir principios SOLID.")

    # Escribir SKILL.md
    skill_md_path = os.path.join(base_path, "SKILL.md")
    with open(skill_md_path, "w") as f:
        f.write(content)

    print(f"✅ Habilidad '{name}' creada con éxito en {base_path}")
    print(f"📂 Estructura generada: SKILL.md, scripts/, examples/, resources/")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🚀 ANTIGRAVITY Skill Generator")
    parser.add_argument("name", help="Nombre de la habilidad (snake_case)")
    parser.add_argument("description", help="Breve descripción de la habilidad")
    
    args = parser.parse_args()
    create_skill(args.name, args.description)
