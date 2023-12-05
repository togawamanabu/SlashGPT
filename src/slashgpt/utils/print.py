# from termcolor import colored

from slashgpt.utils.utils import COLOR_DEBUG, COLOR_ERROR, COLOR_INFO, COLOR_WARNING
import logging

logger = logging.getLogger('slashgpt')

def print_debug(text: str):
    logger.debug(text)
    # print(colored(text, COLOR_DEBUG))


def print_error(text: str):
    logger.error(text)
    # print(colored(text, COLOR_ERROR))


def print_info(text: str):
    logger.info(text)
    # print(colored(text, COLOR_INFO))


def print_warning(text: str):
    logger.warning(text)
    # print(colored(text, COLOR_WARNING))


def print_bot(botName: str, message: str):
    print(f"\033[92m\033[1m{botName}\033[95m\033[0m: {message}")


def print_function(function_name: str, message: str):
    print(f"\033[94m\033[1mfunction({function_name}): \033[95m\033[0m{message}")
