import logging
import sys
from colorama import Fore, Style, init

# Inicializa colorama para colores en consola Windows/Linux/Mac
init(autoreset=True)

# Crea logger
logger = logging.getLogger("logger_coloreado")
logger.setLevel(logging.DEBUG)

# Crea handler para consola (stdout)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)

# Formato base con fecha, nivel, archivo y línea
log_format = "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"

# Clase para formatear con colores según nivel
class ColorFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.MAGENTA + Style.BRIGHT
    }

    def format(self, record):
        msg = super().format(record)
        color = self.COLORS.get(record.levelno, Fore.WHITE)
        return f"{color}{msg}{Style.RESET_ALL}"

# Asignar formatter al handler
formatter = ColorFormatter(log_format, datefmt="%Y-%m-%d %H:%M:%S")
console_handler.setFormatter(formatter)

# Agregar handler al logger
logger.addHandler(console_handler)

# Ejemplos de logs
logger.debug("Mensaje DEBUG")
logger.info("Mensaje INFO")
logger.warning("Mensaje WARNING")
logger.error("Mensaje ERROR")
logger.critical("Mensaje CRITICAL")
