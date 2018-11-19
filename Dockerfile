FROM python:3
MAINTAINER Sergio Cruz Pérez <sergiocruz@correo.ugr.es>
WORKDIR InfraestructuraVirtual/
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD gunicorn APLICACION_WEB:app --log-file=- --bind 0.0.0.0:80
