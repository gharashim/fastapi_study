from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# docker의 mysql 과 연결
engine = create_engine("mysql+pymysql://admin:1234@127.0.0.1:3306/dev")
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()