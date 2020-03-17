# prueba_zxventures
Resolución de *challenge* ZX Ventures (Back end).

## Dependencias
Para la construcción del proyecto se requiere tener instalado Docker.

## Construcción y ejecución
La aplicación se despliega en Docker:

    docker-compose up

Esto descarga y genera las imágenes requeridas para desplegar dos contenedores:

* Un servidor de base de datos PostgreSQL con PostGIS, para almacenamiento de datos de proveedores.
* La aplicación que expone un API REST para manipulación de proveedores.

## Uso
La aplicación, ubicada por defecto en `http://localhost:8000`, ofrece 4 *endpoints*:

    /users/
    /auth/
    /providers/
    /providers/{pk}

Al iniciarse por primera vez la aplicación, los endpoints `/providers/` y `/providers/{pk}/` requieren de autorización para su uso. Para ello, se debe registrar al menos un usuario en el sistema. Luego, con las credenciales de dicho usuario debe solicitarse un *token* al sistema en el *endpoint* `/auth/`, el cual se debe usar para acceder a los demás *endpoints*.

## *Endpoints*

* `/users/`
    * Método(s) soportado(s): `POST`.
    * Acepta: `application/json`.
    * Atributos de cuerpo POST:
        * `username` (`string`): único, obligatorio, máx. 150 caracteres.
        * `password` (`string`): obligatorio.
        * `email` (`string`): opcional.
    * Retorna: datos registrados en el sistema (`201 Created`), detalles de error.
* `/auth/`
    * Método(s) soportado(s): `POST`.
    * Acepta: `application/json`.
    * Atributos de cuerpo POST:
        * `username` (`string`): obligatorio, máx. 150 caracteres.
        * `password` (`string`): obligatorio.
    * Retorna: *token* de autenticacióm (`200 OK`), detalles de error.
* `/providers/`
    * Método(s) soportado(s): `GET`, `POST`.
    * Cabeceras HTTP requeridas: `Authorization Token <token>`.
    * Parámetros de consulta GET requeridos: `lat` (`float`), `lgn` (`float`).
    * Atributos de cuerpo POST:
        * `id` (`number`): único, obligatorio.
        * `ownerName` (`string`): obligatorio, máx. 64 caracteres.
        * `document` (`string`): único, obligatorio, máx. 32 caracteres.
        * `coverageArea` (`object`): obligatorio, objeto compatible con tipo `MultiPolygon` de especificación [GeoJSON](https://geojson.org/).
        * `address` (`object`): obligatorio, objeto compatible con tipo `Point` de especificación [GeoJSON](https://geojson.org/).
    * Retorna: datos de proveedor registrados en el sistema (`POST`: `201 Created`; `GET`: `200 OK`), detalles de error. Si no hay un proveedor que cumpla con los criterios de búsqueda, retorna vacío (`204 No Content`).
* `/providers/{pk}`
    * Método(s) soportado(s): `GET`.
    * Cabeceras HTTP requeridas: `Authorization Token <token>`.
    * Parámetros de ruta requeridos: `pk` (`int`).
    * Retorna: Retorna: datos de proveedor solicitado (`200 OK`), detalles de error. Si la clave primaria no existe, retorna vacío (`404 Not Found`).

## Observaciones
La configuración por defecto de la aplicación no considera persistencia de datos. Para habilitar la persistencia, debe modificarse `docker-compose.yml` de manera que la capa de almacenamiento de la base de datos viva fuera del contenedor Docker:

    volumes:
      - "<ruta-carpeta-externa>:/var/lib/postgresql/data"

## Atribuciones
El *script* `wait-for-it.sh` fue obtenido desde [GitHub](https://github.com/vishnubob/wait-for-it`) y le son aplicables los términos de la licencia respectiva, que se adjunta en este repositorio.