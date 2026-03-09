import os

def test_integration_example():
    assert os.path.exists("openhab_conf")

def test_dockerfile_exists():
    assert os.path.isfile("Dockerfile")