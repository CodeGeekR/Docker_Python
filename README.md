# ¡Bienvenido al proyecto "Dockerized Django eCommerce"! 🚀

## Descripción

Este proyecto es un eCommerce desarrollado en Python con el framework Django, que te permite tener una tienda en línea lista para funcionar rápidamente utilizando contenedores Docker. La combinación de Django y Docker proporciona un entorno de desarrollo y despliegue consistente y fácil de configurar.

## Características

- Tienda en línea totalmente funcional desarrollada con Django.
- Contenedores Docker preconfigurados para un entorno de desarrollo y despliegue fácil.
- Gestión de usuarios, productos, busqueda de productos y procesamiento de pedidos.
- API Rest para consumir los servicios desde el Frontend.
- Escalabilidad y rendimiento optimizados gracias al uso de Docker.

## Instrucciones de instalación

## Prerrequisitos

Docker instalados en tu sistema.

## Pasos

1. Clona este repositorio en tu máquina local:

   ```bash copyable
   git clone https://github.com/CodeGeekR/Docker_Python.git

   ```

2. Navega hasta el directorio del proyecto en la terminal:

   ```bash copyable
   cd <ruta_carpeta>
   ```

3. Construye una imagen de Docker a partir del archivo Dockerfile y etiquetarla con un nombre personalizado.

   ```bash copyable
   docker build -t <nombre_imagen> .
   ```

4. Ejecuta el contenedor de Docker a partir de una imagen llamada "app" y configura los puertos y volúmenes necesarios

   ```bash copyable
   docker run -it -p 3000:80 -v <ruta_del_contenedor_incluye_folder_app>:/app <nombre_imagen>
   ```

   - docker run: Este comando se utiliza para ejecutar un contenedor de Docker.
   - -it: Estos parámetros se utilizan para iniciar el contenedor en modo interactivo y asignarle una terminal.
   - -p 3000:80: Este parámetro se utiliza para mapear el puerto 80 del contenedor al puerto 3000 del host. Esto permite que el contenedor sea accesible desde el exterior a través del puerto 3000.
   - -v <ruta_del_contenedor_incluye_folder_app>:/app ==> Este parámetro se utiliza para montar un volumen compartido en el contenedor.

## Contribuye

¡Te invito a contribuir a este proyecto y hacerlo aún mejor! 😊

Si te gusta este proyecto, no olvides darle una Star ⭐️ en GitHub.

Si deseas contribuir con código, sigue estos pasos:

Haz un fork de este repositorio.
Crea una rama con tu nueva funcionalidad: git checkout -b feature/nueva-funcionalidad.
Realiza tus cambios y realiza commits: git commit -m "Añade nueva funcionalidad".
Envía tus cambios a tu repositorio remoto: git push origin feature/nueva-funcionalidad.
Abre un Pull Request en este repositorio principal.
Si encuentras algún problema o tienes alguna sugerencia, abre un Issue en el repositorio. Estaré encantado de ayudarte.

Comparte este proyecto con tus amigos y colegas.

Agradecimientos
¡Gracias por tu interés en este proyecto! Esperamos que sea útil y te diviertas explorando y contribuyendo. Si tienes alguna pregunta, no dudes en contactarme.
