import pytest
from models.cats_analyzer import CatsAnalyzer


@pytest.fixture
def test_client():
    client = CatsAnalyzer('https://http.cat/status/')
    yield client
