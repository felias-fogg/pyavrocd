# pyavrocd Installation

If you want to use pyavrocd as part of Arduino IDE 2, you do not need to install it explicitly. It is sufficient [to add an "additional boards manager URL" and install the respective core](https://github.com/felias-fogg/pyavrocd/blob/main/docs/debugging-software.md). As a Linux user, you may also need to set some permissions and provide udev rules.

If you want to use pyavrocd stand-alone or as part of another IDE, you need to install the pyavrocd package explicitly.

## Installation by downloading binaries

Go to the GitHub page (if you are not already there), select the latest release (located on the right-hand side of the page), download the archive containing the binary for your architecture, and then untar the archive. It includes the executable pyavrocd, a folder pyavrocd-util, and additionally avr-gdb, the GDB debugger for AVR chips. Store pyavrocd and pyavrocd-util somewhere in the same folder and include this folder in your `PATH` variable. The avr-gdb debugger has version 16.3, which is relatively recent, and has been compiled for your architecture with only a minimal amount of references to dynamic libraries. It is up to you to decide whether you want to use this version or the one that is already installed on your system.

Since the binaries were generated on very recent versions of the respective operating systems (Windows 11, macOS 15.4, Ubuntu 24.04), it can happen that the binary is not compatible with your operating system. In this case, use one of the methods below.

## PyPI installation

I assume you already installed a recent Python version (>=3.9).

It will be necessary to install [pipx](https://pipx.pypa.io/) first. If you haven't done so already, follow the instructions on the [pipx website](https://pipx.pypa.io/stable/installation/). Then proceed as follows.

### On Linux

```
> pipx install pyavrocd
> pipx ensurepath
> sudo ~/.local/bin/pyavrocd --install-udev-rules
```

The last command will install the necessary udev rules. This can also be done manually by following the instructions in the [pyedbglib README](https://github.com/microchip-pic-avr-tools/pyedbglib/blob/main/README.md).

After unplugging and replugging the debugger and restarting your shell, you can invoke the GDB server by simply typing `pyavrocd` into a shell. The binary is stored under `~/.local/bin/`

### Windows and macOS

```
> pipx install pyavrocd
> pipx ensurepath
```

After restarting the shell, you should be able to start the GDB server. The binary is stored under `~/.local/bin/`

## GitHub installation

Alternatively, you can download or clone the GitHub repository. Additionally, you need to install the Python package management [poetry](https://python-poetry.org):

```
> pipx install poetry
```

With that, you can start executing the script inside the downloaded folder as follows:

```
> poetry install
> poetry run pyavrocd ...
```

Furthermore, you can create a binary standalone package as follows (after having installed the [pyinstaller package](https://pyinstaller.org/en/stable/)):

```
> poetry run pyinstaller pyavrocd.spec
```

After that, you find an executable `pyavrocd` (or `pyavrocd.exe`) in the directory `dist/pyavrocd/` together with the folder `pyavrocd-util`. You can copy those to a place in your `PATH`. If you want to generate a binary on a Mac that can be shipped to other Macs, you should use `arm64-apple-pyavrocd.spec` or `intel-apple-pyavrocd.spec` in order to include the right `libusb` for the host architecture. Note that fat binaries cannot be generated.

------

[<small><i>Back to pyavrocd README</i></small>](https://github.com/felias-fogg/pyavrocd/blob/main/README.md)
