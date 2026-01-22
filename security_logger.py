import logging

security_logger = logging.getLogger("AI_SECURITY")
security_logger.setLevel(logging.WARNING)
security_logger.propagate = False

handler = logging.FileHandler("security.log")
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)

if not security_logger.handlers:
    security_logger.addHandler(handler)

def log_security_event(message):
    security_logger.warning(message)
