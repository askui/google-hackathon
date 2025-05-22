import pytest
from askui import VisionAgent
from dotenv import load_dotenv
from askui.reporting import SimpleHtmlReporter

load_dotenv()  # take environment variables from .env.

@pytest.fixture(scope="session")
def agent():
    with VisionAgent(reporters=[SimpleHtmlReporter()]) as agent:
        yield agent
    
