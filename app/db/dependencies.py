from database import SessionLocal


def get_db():
    """
    Locally initialising database
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
