from prometheus_client import start_http_server
from src.app import app

if __name__ == "__main__":
    start_http_server(8000)
    api_service = app
