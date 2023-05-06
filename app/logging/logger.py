import logging

from rich.logging import RichHandler

from app.configuration import get_settings

SETTINGS = get_settings()

log = logging.getLogger(__name__)
log.propagate = False

shell_handler = RichHandler()

log.setLevel(SETTINGS.logging_top_level)
shell_handler.setLevel(SETTINGS.logging_top_level)

fmt_shell = "%(message)s"

fmt_file = (
    "%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s"
)

shell_formatter = logging.Formatter(fmt_shell, "[%H:%M:%S]")

shell_handler.setFormatter(shell_formatter)

log.addHandler(shell_handler)
