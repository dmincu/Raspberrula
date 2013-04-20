#! /bin/bash

ADDR=$1
MAC=$2
if (( $# == 0));
then
	echo "use ./network ip [mac]"
else
	if (($# == 1));
	then
		sudo su
		ip address add $ADDR dev eth0
		exit
	else
		sudo su
		/etc/init.d/networking stop
		ip address add $ADDR dev eth0
		ip link set eth0 address 02:01:02:03:04:08	
		/etc/init.d/networking start
		exit
	fi
fi

