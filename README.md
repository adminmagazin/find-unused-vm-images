find-unused-vm-images
=====================

Find unused VM images with Libvirt-Python. This script iterates over the disks of all available VMs and compares them to the existing images in the VM directory. The files in the '/var/lib/libvirt/boot' directory are not used for comparison, as they may contain DVD images that are mounted during runtime.

##Requires
* Libvirt, Libvirt-Python, Python-Elementtree
    
##License 

This script is licensed under the BSD License
