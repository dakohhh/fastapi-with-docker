FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/application

COPY pyproject.toml ./

COPY poetry.lock ./

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000" ]