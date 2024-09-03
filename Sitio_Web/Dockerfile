FROM nginx:latest

#Path: /etc/nginx/nginx.conf
#Path: /usr/share/nginx/html

COPY /sitio /usr/share/nginx/html

# Se puede utilizar volumenes para proyectos más dinámicos, 
# Se puede ejecutar en comando "-v ...." como el siguiente:
# docker run -it --rm -d -p 8080:80 -v ./sitio:/usr/share/nginx/html/sitio --name web nginx
# O se puede declarar en el Dockerfile:
VOLUME [ "/sitio", "/usr/share/nginx/html" ] 
