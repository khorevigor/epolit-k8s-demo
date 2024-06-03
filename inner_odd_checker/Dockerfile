FROM python:3.11.8-bookworm
LABEL authors="zihakho"

EXPOSE 7788

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "inner_odd_checker.py"]
