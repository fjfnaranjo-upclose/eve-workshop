#!/bin/bash

users="usuario00
usuario01
usuario02
usuario03
usuario04
usuario05
usuario06
usuario07
usuario08
usuario09
usuario10
usuario11
usuario12
usuario13
usuario14
usuario15
usuario16
usuario17
usuario18
usuario19"

for a in $users; do
	echo "Creating user $a..."
	adduser --disabled-password --gecos "" $a
	echo "$a:$a" | /usr/sbin/chpasswd
done

touch /var/log/auth.log
service ssh start
tail -f /var/log/auth.log

