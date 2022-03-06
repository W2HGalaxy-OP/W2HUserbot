import os

ENV = bool(os.environ.get("ENV", False))
from sample_config import Var

if ENV:
    pass
else:
    if os.path.exists("config.py"):
        pass
