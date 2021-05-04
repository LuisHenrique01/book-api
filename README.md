# Requisitos
python>=3.8
# Instalação
### Configurando o seu ambiente
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Criando um SECRET_KEY
**Para não expor minha SECRET_KEY eu usei o python-decouple**

A um script criado para gerar uma nova para você sem muitas preocupações.
```bash
python generate_secret_key.py
```