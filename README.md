## Description

Rofi is extensible via [scripts](https://github.com/davatorium/rofi/blob/next/doc/rofi-script.5.markdown). This project is such a script and allows you to manage your bluetooth connections with rofi. It wraps bluetoothctl from the [Bluez](http://www.bluez.org/) project.

## Requirements

* python3
* bluetoothctl

## Installation

Place script in `~/.config/rofi/scripts` and add `:rofi-bluetooth` to `modes` variable in rofi config.

## Credit

Inspired by nickclyde's [rofi-bluetooth](https://github.com/nickclyde/rofi-bluetooth).
