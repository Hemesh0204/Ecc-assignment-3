
FROM python:3.8-slim
WORKDIR /app
COPY server.py /app/
RUN apt-get update && apt-get install -y nano
EXPOSE 8000
CMD ["python3", "server.py"]