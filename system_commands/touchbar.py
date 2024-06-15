#!/usr/bin/env python3
import subprocess
import logging
from typing import List


def run_command(command: List[str]) -> None:
    """
    Executes a shell command and captures the output.

    Parameters:
        command (List[str]): A list containing command and its arguments to be run.

    Returns:
        None
    """
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        logging.info(f"Command: {' '.join(command)}; Result: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running {' '.join(command)}: {e.stderr}")


def restart_touch_bar() -> None:
    """
    Restarts the touch bar by terminating the TouchBarServer and ControlStrip processes.

    Returns:
        None
    """
    commands = [
        ['sudo', 'pkill', 'TouchBarServer'],
        ['sudo', 'killall', 'ControlStrip']
    ]

    for command in commands:
        run_command(command)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
    # Calls the touch bar restarting function
    restart_touch_bar()