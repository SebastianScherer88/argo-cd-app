from pydantic import BaseModel, validator
from enum import Enum

class ValidUser(str, Enum):
    nutch = 'Nutch'
    seb = 'Sebastian'
    syed = 'Syed'
    vincent = 'Vincent'
    vishal = 'Vishal'


def create_message(name: str = 'Sebastian'):

    return f'Hello!!! And welcome to the sample app, {name}!'