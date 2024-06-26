# CalcIp

![Licenza](https://img.shields.io/badge/license-GNU-blue.svg)
![Versione](https://img.shields.io/badge/version-1.0.0-green.svg)

## Index

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [License](#license)
- [Contact](#contact)


## Introduction

CalcIp is a software it's capable to study an IPv4 along with its subnet mask(CIDR) and it's can make subnetting or supernetting by a new subnet mask. CalcIp has born to automate the IPv4 plan on router. I've used The software engineering to develop this project.

## Features

- **Network Address**: CalcIp provides converted network address to decimal, binary.
- **Broadcast Address**: CalcIp provides converted broadcast address to decimal, binary.
- **Subnet Mask**: CalcIp provides converted subnet mask to decimal, binary, CIDR.
- **Wild Card**: CalcIp provides converted wild card to decimal, binary.
- **IPv4**: CalcIp gives converted input address to decimal, binary.
- **Max Hosts**: CalcIp provides the number of maximum hosts.
- **ClassFul**: If the incoming subnet mask is class, CalcIp provides the address class.


## Installation

### Steps

```bash
# Clone repository
git clone https://github.com/jim-bug/calcip.git
cd calcip
```
```bash
# SUPERNETTING
bash calcip.sh -S IP/SB NEW_SB
```
```bash
# subnetting
bash calcip.sh -s IP/SB NEW_SB
```
```bash
# Only IPv4 studing
bash calcip.sh IP/SB
```
```bash
# Help
bash calcip.sh -h
```

### Note:
In the SUPERNETTING case ```NEW_SB``` have to be less than ```SB```. The subnetting case ```NEW_SB``` have to be greater than ```NEW_SB```.

## License

[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)


## Contact
You can contact me using -> ignazioandsperandeo@gmail.com