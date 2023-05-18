from sqlalchemy import MetaData, Table, Column
from sqlalchemy import Integer, String, Date, DateTime
from sqlalchemy.sql import func


metadata = MetaData()

person_table = Table(
    "person",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("first_name", String, nullable=False),
    Column("last_name", String, nullable=False),
    Column("date_of_birth", Date, nullable=False),
    Column("created_at", DateTime(timezone=False), default=func.now())
)