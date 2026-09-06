# AppWeb Prados Pets

Sistema de gestión para la clínica veterinaria **Prados Pets**: consulta, hospitalización, peluquería, inventario, facturación, directorio y fidelización de clientes, y reportes/estadísticas.

Proyecto desarrollado para la asignatura *Administración de Proyectos Informáticos*, entregable **E1**.

## Stack tecnológico

| Capa | Tecnología |
|---|---|
| Backend / Frontend | Django (Python) — arquitectura de 3 capas (MVT) |
| Base de datos | SQLite (desarrollo) → PostgreSQL (antes de E2) |
| Metodología | Scrum, sprints de 2 semanas |
| Gestión de tareas | GitHub Issues + GitHub Projects |

## Módulos del alcance (E1)

1. Agendamiento (consulta y peluquería — la hospitalización no se agenda)
2. Consulta y hospitalización (historia clínica, orden de medicamentos)
3. Peluquería
4. Facturación (consolidada)
5. Inventario y alertas (stock bajo, vencimiento por lote)
6. Directorio y fidelización de clientes
7. Reportes y estadísticas

## Estructura del repositorio

```
prados-pets/
├── config/                 # proyecto Django (settings, urls, wsgi)
│   └── settings/
│       ├── base.py
│       ├── dev.py           # SQLite, DEBUG=True
│       └── prod.py          # PostgreSQL, DEBUG=False (E2)
├── apps/
│   ├── directorio/          # dueños, mascotas
│   ├── usuarios/            # auth, roles, permisos
│   ├── agendamiento/        # citas de consulta y peluquería
│   ├── clinico/             # consulta, hospitalización, historia clínica
│   ├── inventario/          # productos, stock, alertas
│   ├── peluqueria/          # servicio de grooming
│   ├── facturacion/         # facturas consolidadas
│   └── reportes/            # estadísticas y fidelización
├── templates/
├── static/
├── requirements/
│   ├── base.txt
│   └── dev.txt
├── manage.py
└── README.md
```

## Cómo levantar el proyecto en local

```bash
# 1. Clonar el repositorio
git clone https://github.com/Cruz-Fernando/prados-pets.git
cd prados-pets

# 2. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate        # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements/dev.txt

# 4. Aplicar migraciones
python manage.py migrate

# 5. Crear superusuario (para entrar al admin de Django)
python manage.py createsuperuser

# 6. Levantar el servidor de desarrollo
python manage.py runserver
```

Luego abre `http://127.0.0.1:8000/` en el navegador.

> Nota: mientras el proyecto base de Django no esté creado, los pasos 3 a 6 no aplican todavía. Este README se actualiza en cuanto se suba el esqueleto inicial (HU31).

## Flujo de trabajo con Git

- `main`: rama estable, solo recibe merges desde `develop`.
- `develop`: rama de integración de cada sprint.
- `feature/HUxx-nombre-corto`: una rama por historia de usuario (por ejemplo `feature/HU11-registrar-consulta`), creada desde `develop`.

Cada Pull Request debe referenciar el issue correspondiente (por ejemplo, escribir `Closes #13` en la descripción del PR para el HU11).

## Gestión del proyecto

- **Backlog e historias de usuario:** ver la pestaña [Issues](../../issues) — cada una está etiquetada con `sprint:N`, `modulo:*` y `resp:*`.
- **Tablero Scrum:** ver la pestaña [Projects](../../projects) → *Prados Pets - Sprints*.
- **Sprints:** 6 sprints de 2 semanas, del 07 de septiembre al 30 de noviembre de 2026 (cierre de E1).

## Equipo

| Nombre | Rol |
|---|---|
| Jhojan Cruz Bulla | Director de Proyecto / Product Owner / Scrum Master |
| David Torres Ovallos | Líder Tecnológico / Backend |
| Daniel Alejandro Pacheco Villamizar | Frontend |
| Juan Camilo Guarín Solano | Backend |
| Oscar Enrique Arias Cardile | Fullstack |
| Samuel Alexander García Sandoval | Backend |
| Abel Stiven Ayala Llanes | Fullstack |
| Jeiner Duván Carvajal Araque | Frontend |

## Cliente

**Prados Pets** — clínica veterinaria (Cúcuta), representada por Omar (propietario), patrocinador y cliente del proyecto.
