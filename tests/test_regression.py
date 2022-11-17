import os

import pytest
import requests

from app.utils import create_message

port=int(os.environ.get('PORT', 8080))

url_template = 'http://127.0.0.1:{port}/{user_name}'

def test_root():
    
    response = requests.get(url_template.format(port=port,user_name=''))
    assert response.status_code == 200
    assert response.json() == {"message": create_message()}

@pytest.mark.parametrize('user_name',('Sebastian','Nutch','Vincent','Vishal'))
def test_custom_message_valid_username(user_name):

    response = requests.get(url_template.format(port=port,user_name=user_name))
    assert response.status_code == 200
    assert response.json() == {"message": create_message(user_name)}

@pytest.mark.parametrize('user_name',('Bob',' '))
def test_custom_message_invalid_username(user_name):

    response = requests.get(url_template.format(port=port,user_name=user_name))
    assert response.status_code == 422