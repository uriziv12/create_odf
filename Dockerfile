# ~/repos/create_pdf> docker build -t create_pdf:v1.0 .
FROM python:3
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y wkhtmltopdf && rm -rf /var/lib/apt/lists/*
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["app/from_html_file.py"]
