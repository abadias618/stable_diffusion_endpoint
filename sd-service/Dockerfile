FROM python:3.10.8-slim
LABEL description="Stable Difussion Pixel LoRA service"
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 6000
CMD ["python3","app.py"]