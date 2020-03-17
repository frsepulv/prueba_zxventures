# prueba_zxventures
Resolución de *challenge* ZX Ventures (Back end).

## Ejecución
Se recomienda construir y desplegar la aplicación a través de un contenedor Docker:

    docker build .
    docker run -d -p 127.0.0.1:8000:8000/tcp <image_id>

Para ejecución directa en el computador donde se clona este repositorio, por favor siga leyendo este documento.

## Requisitos
La ejecución de esta aplicación requiere los siguientes componentes:

- [GEOS](https://trac.osgeo.org/geos/).
- [GDIS](https://gdal.org/).
- [PROJ4](https://proj.org/).
- [SpatiaLite](https://docs.djangoproject.com/en/3.0/ref/contrib/gis/install/spatialite/).

