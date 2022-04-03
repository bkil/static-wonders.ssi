#!/bin/sh
echo "Content-type: text/plain"
echo

mkdir -p var/ok 2>/dev/null
if [ -d var/ok ]; then
  rmdir var/ok 2>/dev/null
  echo ok
else
  echo bad
fi
