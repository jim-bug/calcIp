#!/bin/bash
# Author: Ignazio Leonardo Calogero Sperandeo
# Date: 27/06/2024
# Project: CalcIp

echo "


 _____       _     ____
/  __ \     | |   |_   _|
| /  \/ __ _| | ___ | | _ _
| |    / _\` | |/ __|| || '_ \\
| \__/\ (_| | | (___| || |_) |
 \____/\__,_|_|\___\___/ .__/
                       | |
                       |_|


"

if [[ "${1:0:1}" == "-" ]]; then	# check first char
    python3 Main.py "$2" "$3" "$1"
else
    python3 Main.py "$1"
fi

# :)
