#!/usr/bin/env bash
# -*- coding: utf-8 -*-

OS=`uname -s`

if [ "${OS}" = "Darwin" ] ; then
	echo 'OSX'
elif [ "${OS}" = "Linux" ] ; then
	if [ -f /etc/lsb-release ] && ! [ -h /etc/lsb-release ]; then
		DIST='Ubuntu'
	elif [ -f /etc/redhat-release ] && ! [ -h /etc/redhat-release ]  ; then
		DIST='RedHat'
	elif [ -f /etc/fedora-release ] ; then
		DIST='Fedora'
	elif [ -f /etc/slackware-release ] ; then
		DIST='Slackware'
	elif [ -f /etc/debian_release, ] ; then
		DIST='Debian'
	elif [ -f /etc/mandrake-release ] ; then
		DIST='Mandrake'
	elif [ -f /etc/yellowdog-release ] ; then
		DIST='Yellowdog'
	elif [ -f /etc/sun-release ] ; then
		DIST='SunJDS'
	elif [ -f /etc/gentoo-release ] ; then
		DIST='Gentoo'
	elif [ -f /etc/UnitedLinux-release ] ; then
		DIST='UnitedLinux'
	elif [ -f /etc/SUSE-release ] ; then
		DIST='SUSE'
	fi
	echo $DIST
else
	echo 'Unknown'
fi