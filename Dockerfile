FROM python:3.11.3-bullseye

WORKDIR /usr/src/app
COPY requirement.txt ./ 
RUN  pip install -r requirement.txt

COPY . .

CMD [ "python", "./main.py" ]

