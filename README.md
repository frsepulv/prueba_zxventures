# prueba_zxventures
Resolución de *challenge* ZX Ventures (Back end).

## Ejecución
La aplicación se despliega a través de un contenedor Docker:

    docker build -t prueba_zxventures .
    docker run -d -p 127.0.0.1:8000:8000/tcp prueba_zxventures