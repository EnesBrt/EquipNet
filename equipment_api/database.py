from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Configuration de la connexion à la base de données
# Format: postgresql://utilisateur:motdepasse@hote:port/nom_base
DATABASE_URL = "postgresql://admin:123456@localhost:5432/cmdb"

# Création du moteur de base de données
engine = create_engine(DATABASE_URL)

# Création d'une factory de sessions
# autocommit=False : les changements ne sont pas automatiquement sauvegardés
# autoflush=False : les requêtes ne sont pas automatiquement synchronisées
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Création de la classe de base pour les modèles
Base = declarative_base()

# Fonction pour obtenir une session de base de données


def get_db():
    db = SessionLocal()
    try:
        yield db  # Fournit la session
    finally:
        db.close()  # Ferme la session après utilisation
