
# REST API Gestione Utenti - Flask

API REST sviluppata in Python con Flask per la gestione utenti.

## Funzionalità
- CRUD utenti
- Gestione dati JSON
- Password hashing
- Login autenticato
- Architettura backend modulare

## Installazione

### 1. Creare ambiente virtuale
```bash
python -m venv venv
```

### 2. Attivare ambiente virtuale
Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

### 3. Installare dipendenze
```bash
pip install -r requirements.txt
```

### 4. Avviare il server
```bash
python app.py
```

Server disponibile su:
http://127.0.0.1:5000

## Endpoint API

### Creazione utente
POST /api/users/

### Lista utenti
GET /api/users/

### Singolo utente
GET /api/users/<id>

### Aggiornamento utente
PUT /api/users/<id>

### Eliminazione utente
DELETE /api/users/<id>

### Login
POST /api/users/login
