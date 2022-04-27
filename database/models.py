from datetime import datetime
from sqlalchemy import Table, Column, MetaData, Integer, String, TIMESTAMP, Boolean, DECIMAL, create_engine
from sqlalchemy.orm import  registry, sessionmaker
from app.account.domain.model.User import User
from app.catalog.domain.model.Product import Product
from database import DATABASE_URL

metadata = MetaData()
mapper_registry = registry(metadata=metadata)

users = Table(
    "users",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255),  nullable=False),
    Column("email", String(255), nullable=False, unique=True),
    Column("password", String(255), nullable=False),
    Column("admin", Boolean,  default=True),
    Column("created_at", TIMESTAMP,  default=datetime.utcnow(), nullable=False),
    Column("updated_at", TIMESTAMP,  default=datetime.utcnow(), nullable=False),
)

products = Table(
    "products",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255),  nullable=False),
    Column("sku", String(255), nullable=False, unique=True),
    Column("price", DECIMAL, nullable=False, default=0.0),
    Column("brand", String(255), nullable=False, default=0.0),
    Column("created_at", TIMESTAMP,  default=datetime.utcnow(), nullable=False),
    Column("updated_at", TIMESTAMP,  default=datetime.utcnow(), nullable=False),
)


def start_mappers():
    mapper_registry.map_imperatively(User, users)
    mapper_registry.map_imperatively(Product, products)

def get_session():
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal

def get_db():
    session = get_session()
    db = session()
    try:
        yield db
    finally:
        db.close()