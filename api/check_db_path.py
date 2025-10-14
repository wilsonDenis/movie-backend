"""Script pour vérifier le chemin de la base de données"""
import os
from pathlib import Path

# Chemin actuel
print(f"Répertoire de travail actuel: {os.getcwd()}")

# Chemin relatif utilisé dans database.py
db_path = "./movies.db"
absolute_path = Path(db_path).resolve()
print(f"Chemin absolu de './movies.db': {absolute_path}")
print(f"Le fichier existe? {absolute_path.exists()}")

# Vérifier aussi dans le dossier api
api_db = Path("api/movies.db").resolve()
print(f"\nChemin de 'api/movies.db': {api_db}")
print(f"Le fichier existe? {api_db.exists()}")

# Vérifier les tables si le fichier existe
if absolute_path.exists():
    import sqlite3
    conn = sqlite3.connect(str(absolute_path))
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"\nTables dans {absolute_path}: {tables}")
    conn.close()
