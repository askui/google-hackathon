import pytest
from askui import VisionAgent
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

@pytest.fixture(scope="session")
def agent():
    with VisionAgent() as agent:
        yield agent
    
