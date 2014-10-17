#!/usr/bin/env python
# -*- coding: utf-8 -*-

# script iterates over the disks of all available VMs and compares them
# to the existing images in the VM directory.
# NOTE: the /var/lib/libvirt/boot image is not included

import libvirt
import glob
from xml.etree import ElementTree

used_files = []

conn = libvirt.open("qemu:///system")
for vmname in conn.listDefinedDomains():
    vm = conn.lookupByName(vmname)
    xmlroot = ElementTree.fromstring(vm.XMLDesc(0)) # get root of XML description
    for source in xmlroot.findall('./devices/disk/source'):
        used_files.append(source.get('file'))

print "vm files not used in libvirt configuration:"
for file in glob.glob('/var/lib/libvirt/images/*'):
    if file not in used_files:
        print file



