from pydantic import BaseModel, validator
from enum import Enum

class ValidUser(str, Enum):
    nutch: str = 'Nutch'
    seb: str = 'Sebastian'
    vincent: str = 'Vincent'
    vishal: str = 'Vishal'


def create_message(name: str = 'Sebastian'):

    return f'Hello and welcome to the sample app, {name}!'