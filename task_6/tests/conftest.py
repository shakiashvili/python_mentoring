import pytest
import yaml
from models.cats_analyzer import CatsAnalyzer


@pytest.fixture(scope='session')
def env_config() -> dict:
    """This function returns dictionary ,key,value pair of the base_url"""
    with open('env.yaml') as f:
        return yaml.load(f, Loader=yaml.FullLoader)     


@pytest.fixture
def test_client(env_config: dict) -> CatsAnalyzer:
    '''This function returns an instance of CatsAnalyzer with url'''
    return CatsAnalyzer(env_config.get('base_url'))
