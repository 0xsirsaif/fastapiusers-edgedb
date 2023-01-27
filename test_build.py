# flake8: noqa
import sys

try:
    from fastapiusers_edgedb import EdgeDBUserDatabase
except:
    sys.exit(1)

sys.exit(0)
