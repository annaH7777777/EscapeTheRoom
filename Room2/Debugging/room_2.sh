#Fix the script so the file is readable and writable only by the user running the script.

#!/bin/bash

touch "$1"
chmod 600 "$1"
chown root:root "$1"