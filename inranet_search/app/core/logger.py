import logging

# Initialize logger
logger = logging.getLogger('silva.ocr')
# Set the default level
logger.setLevel(logging.INFO)

# Create the handler (console output)
handler = logging.StreamHandler()
# Create the formatter (to display relevant information)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(filename)s:%(lineno)d - %(levelname)s - [%(funcName)s] %(message)s')

# Link the formatter to the handler
handler.setFormatter(formatter)
# Ling the handler to the logger
logger.addHandler(handler)
