from datetime import date

from pydantic import BaseModel


class Person(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date


