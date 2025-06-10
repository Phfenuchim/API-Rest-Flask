# API-Rest-Flask
APi Rest em python em padrão MVC, com regras de usuários e politicas e envio de e-mails.
# Deploy - cloud
Configuração em nuvem, automação em bash, criação de service para iniciaclizar jutnamente a instância, caso necessario envie o arquivo .env via scp para a instancia.
## 1. Crie um systemctl
no "/etc/systemd/system/" crie um arquivo gunicorn.service
```bash
[Unit]
Description=Gunicorn instance to serve flask app
After=network.target

[Service]
User=ec2-user
Group=ec2-user
WorkingDirectory=/home/ec2-user/API-Rest-Flask/src/main
ExecStart=/home/ec2-user/.local/bin/gunicorn -w 4 -b 127.0.0.1:8000 app:app

[Install]
WantedBy=multi-user.target
```
## 2. ativando service automatico
```bash
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn
```

## 3. .bash
Automação para atualizar a branch

```bash
#!/bin/bash

set -e  # Encerra o script ao primeiro erro

# Diretórios
PROJ_DIR="paySmart-contaPagamento"
REPO_URL="git@github.com:Phfenuchim/API-Rest-Flask.git"
SRC_ENV="environment/.env"
DEST_ENV="$PROJ_DIR/.env"

# Parar o serviço antes de atualizar (opcional)
sudo systemctl stop gunicorn || true

# Remover projeto antigo
if [ -d "$PROJ_DIR" ]; then
    echo "Removendo diretório antigo: $PROJ_DIR"
    rm -rf "$PROJ_DIR"
fi

# Clonar projeto
echo "Clonando repositório..."
git clone "$REPO_URL"

# Copiar arquivos sensíveis
echo "Copiando arquivos env..."
cp "$SRC_ENV" "$DEST_ENV"

# Instalar dependências (user-level para evitar problemas de permissão)
echo "Instalando dependências Python..."
pip install --user -r "$PROJ_DIR/requirements.txt"

# Migrar banco, coletar estáticos etc. (adicione seus comandos extras aqui)

# Subir serviço novamente
echo "Reiniciando serviço Gunicorn..."
sudo systemctl restart gunicorn
echo "Deploy concluído com sucesso!"

```
## 4. Configure o proxy reverso com nginx
na pasta do nginx "/etc/nginx/conf.d/" adicone o arquivo .conf

```bash
server {
    listen 80;
    server_name SEU_DOMINIO.com.br;  # Substitua pelo seu domínio

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
## 5. Subdominio/dominio
Crie um direcionamento do dns para o ip utilizado, no caso criei um registro simples do tipo A.

## 6. Abrir porta para comunicação
Garanta que as porta 443 e 80 estejam abertas

## 7. Gere um certificado ssl
```bash
sudo dnf install certbot python3-certbot-nginx -y
sudo certbot --nginx

```
## Analisar LOGs
```bash
sudo tail -f var/log/nginx/access.log
```
## Teste o banco de dados localmente

```bash
db:Add commentMore actions
    image: postgres:latest
    container_name: postgres-container
    restart: always
    environment:
      - FLASK_ENV=development
      - FLASK_APP=app.py
      POSTGRES_DB: paysmart-db
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: "Postgres2022!"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./src/main/resources/db/migrations/init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```