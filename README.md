# testsf2
Antes de empezar es necesario crear una carpeta llamada mysql.

una vez creada la carpeta ejecute el docker compose

        docker-compose up -d

# LARAVEL Conocimiento en PHP
En la carpeta src se encuentra el codigo en LARAVEL para usar laravel se debe tener compose instalado, ve a la carpeta src y ejectuta composer install

        cd src
        composer install

La carpeta storage molestara asi que dale permisos

        docker exec sellr_php chmod -R 777 storage/
        docker exec sellr_php chmod -R 777 storage/logs/

Corre las migraciones para que se cree las tablas de la base de datos

        docker exec php php artisan migrate

# Django Conocimiento en Python
En la carpeta Django se encuentra el codigo en python pero no esta en docker asi que se debe tener en el pc instalado python, este usa sqlite3 que es la base de datos  por defecto de DJANGO asi que se debe ejecutar las migraciones

        cd Django
        python3 manage.py migrate

cuando la migracion cargue se debe ejecutar el servidor 

        python3 manage.py runserver