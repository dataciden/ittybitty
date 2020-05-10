#!/bin/bash

if [ $(id -u) -eq 0 ]; then
	read -p "Enter username : " username
	read -s -p "Enter password : " password
	egrep "^$username" /etc/passwd >/dev/null
	if [ $? -eq 0 ]; then
		echo "$username exists!"
		exit 1
	else
		pass=$(perl -e 'print crypt($ARGV[0], "password")' $password)
        useradd -m -p "$pass" "$username"
		[ $? -eq 0 ] && echo "User has been added to system!" || echo "Failed to add a user!"
	fi
    read -p "Enter a description for $username user: " desc
    usermod -c $desc &username
    read -p "Enter a group name to add $username into: " group
    if [group] then
        grep $group /etc/group
        if [ $? -gt 0] then 
            groupadd $group
            echo " $username is added to the $group group"
        fi
else
	echo "Only root may add a user to the system."
	exit 2

fi