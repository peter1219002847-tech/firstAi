from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DaTABASE_URL = "mysql+pymysql://root:123456@localhost:3306/fastapi_db"

engine = create_engine(
    DaTABASE_URL,
    echo=True,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    bind=engine
)