#!/bin/sh
printf "Content-type: text/plain\n\n"

{
 date
} >> "`dirname "$0"`"/cron.log.txt 2>&1
