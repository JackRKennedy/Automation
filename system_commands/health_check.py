#!/usr/bin/env python3
import os
import shutil
import psutil
import tempfile
from typing import Union


def check_disk_usage(disk: str) -> bool:
    """Calculate the free disk space percentage.

    Parameters:
        - disk (str): path to the disk volume to check

    Returns:
        - bool: True if free disk space is more than 20%, else False.
    """
    du = shutil.disk_usage(disk)
    free_percentage = du.free / du.total * 100
    return free_percentage > 20


def check_cpu_usage(duration: Union[int, float]) -> bool:
    """Calculate CPU utilization percentage over a period of time.

    Parameters:
        - duration (Union[int, float]): duration in seconds to measure cpu usage

    Returns:
        - bool: True if CPU usage is less than 75%, else False.
    """
    usage = psutil.cpu_percent(duration)
    return usage < 75


def purge_memory() -> None:
    """Execute the system's memory purge command."""
    os.system('sudo purge')


def check_temp() -> None:
    """Check system temperature."""
    temp = psutil.sensors_temperatures(fahrenheit=False)
    for component in temp:
        for element in temp[component]:
            print(f"{component}\t\t{element.current}°C")


def check_memory_usage() -> None:
    """Print the current memory usage of the system."""
    memory = psutil.virtual_memory()
    print(f'Your memory usage is at {memory.percent}%.')


def clean_temp_files() -> None:
    """Remove all temporary files from the temp folder."""
    temp_folder = tempfile.gettempdir()
    for temp_file in os.listdir(temp_folder):
        if temp_file.endswith(".tmp"):
            os.remove(os.path.join(temp_folder, temp_file))


def kill_zombie_processes() -> None:
    """Identify and kill all the zombie processes running in the system."""
    zombies = []
    for process in psutil.process_iter(['pid', 'name', 'status']):
        if process.info['status'] == psutil.STATUS_ZOMBIE:
            zombies.append(process.info['pid'])
    if zombies:
        for pid in zombies:
            os.system(f'kill -9 {pid}')


if __name__ == "__main__":
    if not check_cpu_usage(1) or not check_disk_usage("/"):
        print("ERROR!")
    else:
        print("Everything seems to be working fine!")
    purge_memory()
    check_temp()
    check_memory_usage()
    clean_temp_files()
    kill_zombie_processes()