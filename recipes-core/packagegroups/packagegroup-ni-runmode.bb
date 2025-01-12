# (C) Copyright 2013,
#  National Instruments Corporation.
#  All rights reserved.

SUMMARY = "Runmode specific packages for NI Linux Realtime distribution"
LICENSE = "MIT"

PACKAGE_ARCH = "${MACHINE_ARCH}"

inherit packagegroup

RDEPENDS_${PN} = "\
	dosfstools \
	e2fsprogs \
	e2fsprogs-e2fsck \
	e2fsprogs-mke2fs \
	e2fsprogs-tune2fs \
	gdbserver \
	glibc-gconv-cp932 \
	glibc-gconv-cp936 \
	glibc-gconv-iso8859-1 \
	iproute2-tc \
	libfmi-dev \
	librtpi \
	lldpd \
	niwatchdogpet \
	opkg-utils-shell-tools \
	parted \
	rtctl \
	systemimageupdateinfo \
	util-linux-sfdisk \
	vlan \
	zip \
"
