#!/usr/bin/python3

import subprocess
import sys
import time

ADAPTER_PROPS = {
    "Powered": ("power on", "power off"),
    "Discovering": (lambda: launch_scan(), lambda: None),
    "Pairable": ("pairable on", "pairable off"),
    "Discoverable": ("discoverable on", "discoverable off"),
}

DEVICE_PROPS = {
    "Connected": ("connect", "disconnect"),
    "Paired": ("pair", "remove"),
    "Trusted": ("trust", "untrust"),
}

SEPARATOR = "----------"


def bluetoothctl(instruction, device=None):
    call = ["bluetoothctl"] + instruction.split(" ")
    if device:
        call.append(get_devices()[device])
    return subprocess.run(call, capture_output=True)


def launch_scan():
    call = "coproc (timeout 30s bluetoothctl scan on > /dev/null 2>&1)"
    subprocess.Popen(call, executable="/bin/bash", shell=True)
    time.sleep(0.3)


def get_state(prop, device=None):
    result = bluetoothctl("info", device) if device else bluetoothctl("show")
    return prop + ": yes" in result.stdout.decode('utf-8')


def toggle_state(prop, device=None):
    props = DEVICE_PROPS if device else ADAPTER_PROPS
    instruction = props[prop][get_state(prop, device)]
    if type(instruction) is str:
        bluetoothctl(instruction, device)
    elif callable(instruction):
        instruction()


def get_devices():
    result = bluetoothctl("devices").stdout.decode('utf-8').rstrip()
    devices = {}
    if len(result) > 0:
        for line in result.split('\n'):
            _, address, name = line.split(" ", maxsplit=2)
            devices[name] = address
    return devices


def main_menu():
    for device in get_devices():
        print(device)
    print(SEPARATOR)
    for prop in ADAPTER_PROPS:
        print(prop + ": " + ("yes" if get_state(prop) else "no"))
    print("Refresh")
    exit(0)


def device_menu(device):
    for prop in DEVICE_PROPS:
        state_str = "yes" if get_state(prop, device) else "no"
        print(device + " | " + prop + ": " + state_str)
    print(SEPARATOR)
    print("Back")
    exit(0)


if len(sys.argv) == 1 or sys.argv[1] == 'Back':
    main_menu()

for prop in DEVICE_PROPS:
    if prop in sys.argv[1]:
        device = sys.argv[1].split(" | ")[0]
        toggle_state(prop, device)
        device_menu(device)

for device in get_devices():
    if device in sys.argv[1]:
        device_menu(device)

for prop in ADAPTER_PROPS:
    if prop in sys.argv[1]:
        toggle_state(prop)

main_menu()
