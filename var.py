import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    pass
else:
    pass
