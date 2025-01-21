import subprocess as sp
import os

VMWARE_CMD_PATH = "/Applications/VMware Fusion.app/Contents/Public/vmrun"
VM_DIR_PATH = "/Users/codey/Virtual Machines.localized/"
VMWARE_TYPE = "fusion"

class VMwareManager:
    VMs = [os.path.splitext(f)[0] for f in os.listdir(VM_DIR_PATH) if not f.startswith(".")]

    def __init__(self):
        pass

    @staticmethod
    def startVM(vm_path, gui=False):
        """Starts a VM from the local library."""
        vm_path = VM_DIR_PATH + vm_path

        if not gui:
            sp.run([VMWARE_CMD_PATH, "-T", VMWARE_TYPE, "start", vm_path, "nogui"])
        else:
            sp.run([VMWARE_CMD_PATH, "-T", VMWARE_CMD_PATH, "start", vm_path])

    @staticmethod
    def stopVM(vm_path):
        """Stops a running VM from the local library."""
        vm_path = VM_DIR_PATH + vm_path

        sp.run([VMWARE_CMD_PATH, "stop", vm_path])
