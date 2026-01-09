from sqlalchemy import create_engine

engine = create_engine("sqlite:///./bank_transactions.db", echo=True)
