# backEnd2

1. Clonar el Repositorio

2. Crear y Activar el Entorno Virtual
      python -m venv vEnv
      cd vEnv\Scripts
      .\Activate
      cd..
      cd..
      
3. Instalar las Dependencias
      pip install -r requirements.txt

4.Configurar y Migrar la Base de Datos
      python manage.py migrate
      python manage.py makemigrations
      python manage.py migrate

5. Crear un Superusuario (con esto se podrá logear en /admin/ y una vez logeado, podras ir a /app/ para poder interactuar en la pagina principal
      python manage.py createsuperuser

6. Ejecutar el Servidor
      python manage.py runserver

7. Entra a http://127.0.0.1:8000/

/app

/admin


si entrá sin logear solo podrá ver informacion, no modificar o agregar (CRUD)

(requiere crear una cuenta de super usuario a traves de la terminal)

después de CREAR la cuenta y LOGEAR, podrá interactuar en la pagina principal, sino solo podrá ver los datos presentes

(una vez logeado, en la pagina principal le aparecera arriba a la derecha su nombre de usuario y podrá interactuar en cada pagina abajo a la derecha)

(la carpeta .env está incluida ya que lo dice las instrucciones)







ALGUNOS DATOS DE EJEMPLO PARA INGRESAR A LA BASE DE DATOS:

-- 1. Insertar usuarios
INSERT INTO auth_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES
('pbkdf2_sha256$600000$WvQxZ8...$fake_hash_placeholder_1', 1, 'admin', 'Administrador', 'General', 'admin@mail.com', 1, 1, NOW()),
('pbkdf2_sha256$600000$WvQxZ8$fake_hash_placeholder_2', 0, 'carlos_dev', 'Carlos', 'Gómez', 'carlos@mail.com', 0, 1, NOW()),
('pbkdf2_sha256$600000$WvQxZ8$fake_hash_placeholder_3', 0, 'maria_code', 'María', 'Pérez', 'maria@mail.com', 0, 1, NOW());

-- 2. Insertar perfiles de usuario (Los usuario_id corresponderán a los IDs 1, 2 y 3 generados arriba)
INSERT INTO redsocial_perfilusuario (fecha_nacimiento, biografia, habilitado, created_at, updated_at, usuario_id) VALUES
('1995-05-12', 'Desarrollador Backend y fanático de Django y DRF.', 1, NOW(), NOW(), 1),
('1998-09-20', 'Estudiante de programación y amante del café ☕', 1, NOW(), NOW(), 2),
('1992-02-15', 'Diseñadora UX/UI explorando el desarrollo web.', 1, NOW(), NOW(), 3);

-- 3. Insertar publicaciones (autor_id apunta a los usuarios 2 y 3)
INSERT INTO redsocial_publicacion (contenido, habilitado, created_at, updated_at, autor_id) VALUES
('¡Hola mundo! Esta es mi primera publicación en la red social con Django y REST Framework.', 1, NOW(), NOW(), 2),
('Configurando bases de datos con WampServer y phpMyAdmin. Todo un éxito al final.', 1, NOW(), NOW(), 3),
('¿Cuáles son sus librerías favoritas de Python para el desarrollo backend?', 1, NOW(), NOW(), 2);

-- 4. Insertar comentarios
INSERT INTO redsocial_comentario (contenido, habilitado, created_at, updated_at, autor_id, publicacion_id) VALUES
('¡Bienvenido Carlos! Gran proyecto.', 1, NOW(), NOW(), 3, 1),
('A mí me encanta Django REST Framework por su velocidad.', 1, NOW(), NOW(), 1, 3),
('¡Sí que lo fue! La interfaz visual ayuda bastante.', 1, NOW(), NOW(), 2, 2);

-- 5. Insertar likes 
INSERT INTO redsocial_like (habilitado, created_at, updated_at, publicacion_id, usuario_id) VALUES
(1, NOW(), NOW(), 1, 1),
(1, NOW(), NOW(), 1, 3),
(1, NOW(), NOW(), 2, 1),
(1, NOW(), NOW(), 3, 3);
