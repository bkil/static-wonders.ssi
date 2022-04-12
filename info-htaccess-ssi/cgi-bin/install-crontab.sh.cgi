#!/bin/sh
printf "Content-type: text/plain\n\n"
CRONCGI="`dirname $(readlink -f "$0")`/cron.sh.cgi"

crontab -r

echo "37 13 * * * $CRONCGI >/dev/null 2>/dev/null" |
crontab -
