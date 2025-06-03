import pytest
import yaml
from models.cats_analyzer import CatsAnalyzer


@pytest.fixture(scope='session')
def env_config():
    with open('env.yaml') as f:
        result = yaml.load(f, Loader=yaml.FullLoader)
        return result.get('base_url')


@pytest.fixture
def test_client(env_config) -> CatsAnalyzer:
    client = CatsAnalyzer(env_config)
    return client
