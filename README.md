## Description

[Rofi](https://github.com/davatorium/) is extensible via [scripts](https://github.com/davatorium/rofi/blob/next/doc/rofi-script.5.markdown). `rofi-bluetooth-script` is such a script and allows you to manage your bluetooth connections with rofi.

## Requirements

This project is a thin python wrapper around `bluetoothctl` from the [Bluez](http://www.bluez.org/) project and those two are the only requirements:

* python3
* bluetoothctl

### Void Linux

```bash
xi python bluez
```

## Installation

1. Place script in `~/.config/rofi/scripts`
2. Add `rofi-bluetooth` to `modes` variable in rofi config
3. Optionally, add something like `display-rofi-bluetooth: "  ";` to rofi config if you use a nerd font

## Implementation Details

Rofi stays responsive after putting the bluetooth adapter into the "Discovering" state to scan for new devices. This is achieved by forking off a `timeout 30s bluetoothctl scan on` using python's `Popen(..., shell=True)` and bash's `coproc()`.

## Credit

Inspired by [nickclyde's](https://github.com/nickclyde/) [rofi-bluetooth](https://github.com/nickclyde/rofi-bluetooth), which is a standalone script that calls rofi in dmenu-mode. It gets the job done at least as well as this script, but I couldn't find a way to combine it with other modes in one rofi window.
