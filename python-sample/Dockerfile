FROM python:3.13

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt 

EXPOSE 8000

CMD [ "gunicorn", "app:app", "-b", ":8000"]
