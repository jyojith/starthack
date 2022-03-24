FROM python:3.6.9-alpine
WORKDIR /code

RUN apk --update --upgrade add --no-cache  gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev

RUN python3 -m pip3 install --upgrade pip3
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8050
COPY . .
CMD [ "python", "app.py" ]
