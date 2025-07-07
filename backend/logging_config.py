import logging
from logging.handlers import RotatingFileHandler
from rich.logging import RichHandler

def setup_logging():
    # Console handler with Rich for colorful output
    console_handler = RichHandler(rich_tracebacks=True)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(message)s')  # Rich handles formatting
    console_handler.setFormatter(console_formatter)

    # File handler for debug+ logs, rotating files
    file_handler = RotatingFileHandler(
        'app_debug.log', maxBytes=5*1024*1024, backupCount=3, encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s][%(name)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(file_formatter)

    # Root logger setup: logs INFO+ to console only
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)  # Capture all levels; handlers filter
    root_logger.handlers = []  # Remove any default handlers
    root_logger.addHandler(console_handler)

    # File logger: dedicated logger for file output (debug+)
    file_logger = logging.getLogger('file_logger')
    file_logger.setLevel(logging.DEBUG)
    if not any(isinstance(h, RotatingFileHandler) for h in file_logger.handlers):
        file_logger.addHandler(file_handler)

    # Create your app loggers here with no extra handlers (inherit root handlers)
    for name in [
        'numifocus.main',
        'numifocus.utils',
        'numifocus.services',
        'numifocus.db',
        'numifocus.external'
    ]:
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)  # Fine-grained control per module

        # Avoid duplicate handlers if this runs multiple times
        if logger.hasHandlers():
            continue
        # No handlers added: inherits console output from root