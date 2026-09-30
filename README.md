<div align="center">

# 🐾 Prados Pets

### Sistema de gestión para clínica veterinaria

Consulta · Hospitalización · Peluquería · Inventario · Facturación · Directorio · Reportes

![Django](https://img.shields.io/badge/Django-6.1-092E20?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-336791?logo=postgresql&logoColor=white)
![Metodología](https://img.shields.io/badge/Metodolog%C3%ADa-Scrum-7c3aed)
![Entregable](https://img.shields.io/badge/Entregable-E1-f472b6)

</div>

---

## 📋 Contenido

- [Acerca del proyecto](#-acerca-del-proyecto)
- [Módulos del alcance (E1)](#-módulos-del-alcance-e1)
- [Funcionalidades destacadas](#-funcionalidades-destacadas)
- [Stack tecnológico](#-stack-tecnológico)
- [Estructura del repositorio](#-estructura-del-repositorio)
- [Cómo levantar el proyecto en local](#-cómo-levantar-el-proyecto-en-local)
- [Cuentas de prueba](#-cuentas-de-prueba-para-desarrollo-por-rol)
- [Pruebas](#-pruebas)
- [Despliegue](#-despliegue)
- [Flujo de trabajo con Git](#-flujo-de-trabajo-con-git)
- [Gestión del proyecto](#-gestión-del-proyecto)
- [Equipo](#-equipo)
- [Cliente](#-cliente)

---

## 🩺 Acerca del proyecto

**AppWeb Prados Pets** es el sistema de gestión para la clínica veterinaria **Prados Pets** (Cúcuta). Centraliza en una sola aplicación web el agendamiento de citas, la atención clínica, el servicio de peluquería, el inventario, la facturación, el directorio de clientes y los reportes.

Proyecto desarrollado para la asignatura *Administración de Proyectos Informáticos*, entregable **E1**.

---

## 🧩 Módulos del alcance (E1)

| # | Módulo | Descripción |
|---|---|---|
| 1 | **Agendamiento** | Citas de consulta y de peluquería (la hospitalización no se agenda) |
| 2 | **Consulta y hospitalización** | Historia clínica y orden de medicamentos |
| 3 | **Peluquería** | Servicios de grooming y comprobante en PDF |
| 4 | **Facturación** | Facturación consolidada |
| 5 | **Inventario y alertas** | Stock bajo y vencimiento por lote |
| 6 | **Directorio y fidelización** | Dueños, mascotas y programa de fidelización |
| 7 | **Reportes y estadísticas** | Indicadores de la operación de la clínica |

---

## ✨ Funcionalidades destacadas

- 📅 **Calendario visual (HU08):** vistas por día y por semana que unen las citas de consulta y de peluquería, con colores por servicio, citas cruzadas en columnas, línea de hora actual, tarjetas de resumen que funcionan como filtros y atajos de teclado.
- ✂️ **Agendamiento de peluquería:** búsqueda de mascota por nombre, dueño o teléfono; duración estimada según el tamaño; selección del groomer responsable.
- 🧴 **Servicios de peluquería:** *Solamente Baño*, *Corte Despuntado (solo tijera)* y *Corte Total (máquina y tijera)*.
- 💵 **Precio en pesos colombianos:** el campo de precio formatea automáticamente con puntos de miles y el sufijo COP (por ejemplo, `$123.456 COP`).
- 📄 **Comprobante en PDF:** al agendar un servicio de peluquería se genera el comprobante para el cliente.
- 🔐 **Roles y permisos:** administrador, veterinario, auxiliar, groomer y domiciliario.

---

## 🛠️ Stack tecnológico

| Capa | Tecnología |
|---|---|
| Backend / Frontend | Django (Python) — arquitectura de 3 capas (MVT) |
| Base de datos | PostgreSQL (Supabase) |
| Generación de PDF | xhtml2pdf |
| Servidor de producción | Gunicorn + WhiteNoise |
| Metodología | Scrum, sprints de 2 semanas |
| Gestión de tareas | GitHub Issues + GitHub Projects |

---

## 🗂️ Estructura del repositorio

```
prados-pets/
├── apps/
│   ├── agendamiento/        # citas de consulta y calendario visual
│   ├── clinico/             # consulta, hospitalización, historia clínica
│   ├── directorio/          # dueños y mascotas
│   ├── facturacion/         # facturas consolidadas
│   ├── inventario/          # productos, stock, alertas
│   ├── peluqueria/          # servicio de grooming y comprobante PDF
│   ├── reportes/            # estadísticas y fidelización
│   └── usuarios/            # autenticación, roles y permisos
├── config/                  # proyecto Django (urls, wsgi, asgi)
│   └── settings/
│       ├── base.py
│       ├── dev.py           # PostgreSQL (Supabase), DEBUG=True
│       └── prod.py          # PostgreSQL, DEBUG=False
├── requirements/
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
├── static/
├── templates/
│   ├── base.html
│   ├── agendamiento/
│   ├── directorio/
│   ├── peluqueria/
│   └── usuarios/
├── .env.example             # plantilla de variables de entorno
├── Procfile                 # comandos de release y web para el despliegue
├── manage.py
├── requirements.txt         # dependencias completas del proyecto
└── README.md
```

---

## 🚀 Cómo levantar el proyecto en local

### Requisitos previos

- Python 3
- Git
- Credenciales de la base de datos compartida (las entrega el administrador del equipo por un canal privado)

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/Cruz-Fernando/prados-pets.git
cd prados-pets

# 2. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate        # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env            # En Windows: copy .env.example .env
# Abre .env y completa DB_USER, DB_PASSWORD y DB_HOST

# 5. Aplicar migraciones
python manage.py migrate

# 6. Crear superusuario (para entrar al admin de Django)
python manage.py createsuperuser

# 7. Levantar el servidor de desarrollo
python manage.py runserver
```

Luego abre `http://127.0.0.1:8000/` en el navegador.

> 🔒 El archivo `.env` contiene credenciales: **nunca lo subas al repositorio** (ya está en `.gitignore`).

> 🔄 Si trabajas con cambios de otros compañeros, recuerda hacer `git pull` y volver a correr `python manage.py migrate` para aplicar las migraciones nuevas.

---

## 👤 Cuentas de prueba para desarrollo (por rol)

> **⚠️ AVISO IMPORTANTE DE SEGURIDAD:**
> Las siguientes cuentas y contraseñas son de **uso exclusivo para pruebas y desarrollo local**.
> La seguridad de estas credenciales es deliberadamente baja para facilitar el testing del equipo.
> **Bajo ninguna circunstancia deben utilizarse en entornos de producción.**

Puedes sincronizar o restablecer estas cuentas en cualquier momento ejecutando:

```bash
python manage.py crear_usuarios_prueba
```

| Rol | Usuario | Contraseña | Nombre completo | Permisos |
|---|---|---|---|---|
| **Administrador** | `administrador` | `Admin123*` | Administrador General | Superusuario / Staff |
| **Veterinario** | `veterinario` | `Vet123*` | Dr. Veterinario Pruebas | Personal clínico |
| **Auxiliar** | `auxiliar` | `Auxiliar123*` | Auxiliar Veterinario Pruebas | Apoyo clínico |
| **Groomer** | `groomer` | `Groomer123*` | Groomer / Estilista Canino | Peluquería |
| **Domiciliario** | `domiciliario` | `Domicilio123*` | Repartidor / Domiciliario | Envíos |

---

## 🧪 Pruebas

```bash
python manage.py test
```

---

## ☁️ Despliegue

El `Procfile` define cómo se ejecuta el proyecto en producción:

- **release:** aplica las migraciones y recolecta los archivos estáticos.
- **web:** sirve la aplicación con Gunicorn.

Las variables de entorno necesarias están descritas en `.env.example`. En producción se usa la configuración `config.settings.prod`.

---

## 🌿 Flujo de trabajo con Git

- `main`: rama estable, solo recibe merges desde `develop`.
- `develop`: rama de integración de cada sprint.
- `feature/HUxx-nombre-corto`: una rama por historia de usuario (por ejemplo `feature/HU11-registrar-consulta`), creada desde `develop`.

Cada Pull Request debe referenciar el issue correspondiente (por ejemplo, escribir `Closes #13` en la descripción del PR para el HU11).

> 📝 **Commits:** escribe mensajes claros y en español. Revisa que el mensaje no incluya líneas de co-autor que no correspondan (por ejemplo `Co-authored-by`) antes de subir tus cambios.

---

## 📊 Gestión del proyecto

- **Backlog e historias de usuario:** ver la pestaña [Issues](../../issues) — cada una está etiquetada con `sprint:N`, `modulo:*` y `resp:*`.
- **Tablero Scrum:** ver la pestaña [Projects](../../projects) → *Prados Pets - Sprints*.
- **Sprints:** 6 sprints de 2 semanas, del 07 de septiembre al 30 de noviembre de 2026 (cierre de E1).

---

## 👥 Equipo

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

---

## 🏥 Cliente

**Prados Pets** — clínica veterinaria (Cúcuta), representada por Omar (propietario), patrocinador y cliente del proyecto.
