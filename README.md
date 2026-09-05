# Dagon Scanner · [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/lofiwkz/dagon-recon/blob/main/LICENSE)

A Python CLI tool for network scanning and reconnaissance.

## Summary

* [About](#about)
* [Features](#features)
* [Technologies](#technologies)
* [Requirements](#requirements)
* [Installation](#installation)
* [How to Use](#how-to-use-the-dagon-scanner)
  * [Help](#help)
  * [Running Dagon](#running-dagon)
  * [General Options](#general-options)
  * [Port Scan Options](#port-scan-options-pscan)
  * [Examples](#examples)
* [Project Structure](#project-structure)
* [Roadmap](#roadmap)
* [Limitations](#limitations)
* [Contribution](#contribution)
* [License](#license)
* [Disclaimer](#disclaimer)

## About

Dagon Scanner is a simple CLI tool developed in **Python** for **educational purposes**. Its goal is to perform different types of scans on hosts within a network.

The project is currently focused on network scanning and reconnaissance, with additional features planned for future versions.

## Features

* **Port Scanner**
  * Scans the 1000 most common ports
  * Scans all ports (1-65535)
  * Scans specific ports
  * Identifies the common service associated with a port
* **Multithreading**
  * Uses multiple threads to improve scanning performance
* **CLI**
  * Command-line interface with configurable options

## Technologies

Dagon is developed using the **Python** programming language. The main libraries used in the project are:

* **Argparse**: Handles user interaction through command-line arguments.
* **Socket**: Used for network communication, connection handling, and packet transmission.
* **ThreadPoolExecutor**: Controls the number and usage of threads during scanning.

## Requirements

* **Python 3**
    * Python **3.13.5** was used during the latest tests.

More information about Python can be found at [python.org/downloads](https://www.python.org/downloads/).

## Installation

In a **terminal**, use the following commands:

```bash
# Clone this repository
git clone https://github.com/lofiwkz/dagon-recon.git

# Access the project directory
cd dagon-recon/

# Run the software
python3 dagon.py --help
```

## How to Use the Dagon Scanner

### Help

When using Dagon for the first time, you can view **all available options through the terminal** using the following command:

```bash
python3 dagon.py --help
```

### Running Dagon

Dagon uses the following command-line usage pattern:

```bash
dagon.py [scantype] [target] [options ...]
```

* **scantype**: Defines the type of scan to be performed. By default, the scantype is set to **pscan**.

  * **pscan**: Port scan.
* **target**: Target **IPv4** address or domain.
* **options**: Defines which options will be used for the selected scan type.

---

### General Options

Some arguments can be used regardless of the scan type:

* `-v, --verbose`: Enables verbose output.
* `-t, --threads [threads]`: Specifies the maximum number of threads used by Dagon.

---

### Port Scan Options (pscan)

The following options can be used to perform a port scan:

* `-p, --ports [port, ...]`: Specifies which ports should be scanned.
* `-P, --all-ports`: Scans all **65535** ports.

By default, if none of these arguments are provided, Dagon scans the **1000 most common ports**.

### Examples

```bash
# Scan the 1000 most common ports on "localhost"
python3 dagon.py localhost

# Scan ports 22 and 80 on "127.0.0.1"
python3 dagon.py 127.0.0.1 -p 22 80

# Scan all ports on "127.0.0.1"
python3 dagon.py 127.0.0.1 -P
```

## Project Structure

Overview of the project's directories and files:

```bash
dagon-recon/
|---src/
|-----scanners/
|-------portscan.py
|-----wordlists/
|---dagon.py
```

## Roadmap

### Scanning

* [x] TCP port scanner
* [x] Multithreading
* [ ] SYN scan
* [ ] UDP scan
* [ ] Custom port ranges

### Reconnaissance

* [ ] DNS enumeration
* [ ] Directory enumeration
* [ ] Banner grabbing
* [ ] Service detection

### Output

* [ ] JSON output
* [ ] CSV output
* [ ] Save scan results

## Limitations

Dagon is currently a simple port scanning and reconnaissance tool.

At the moment, it does not provide advanced features such as SYN scanning, UDP scanning, service version detection, or operating system detection.

## Contribution

Contributions are welcome!

If you find a bug, have a suggestion, or want to add a feature, open an **Issue** or submit a **Pull Request**.

When contributing, please keep the code organized and follow the **standards** already used in the project.

## License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

## Disclaimer

Dagon was developed for **educational purposes and authorized security testing only**.

Do not use this tool against systems or networks without explicit permission from the owner.

❤ Thank you for reading ❤
