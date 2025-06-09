# Use uma imagem compativel com o serviço utilizadp
FROM registry.access.redhat.com/ubi8/python-39

# 1. Diretório de trabalho
WORKDIR /app

# 2. Instale dependências
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# 3. Copie o código-fonte
COPY . .

# 4. Exponha a porta do Flask
EXPOSE 5000

# 5. (Opcional, apenas para debug) - se quiser garantir PYTHONPATH
ENV PYTHONPATH=/app/src/main

# 6. Comando default: Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "src.main.app:app"]