from logging import FileHandler
from tools.loggar import get_loggar

Log = get_loggar("rhunes-engine", handler=FileHandler("rhunes-loggar.log", mode="w"))