FROM python:3.11.8-bookworm
LABEL authors="zihakho"

EXPOSE 8899

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "outer_odd_checker.py"]
