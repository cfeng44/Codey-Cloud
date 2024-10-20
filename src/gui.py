import tkinter as tk

from VMwareManager import VMwareManager

def onStartClick():
    vm_name = vm_variable.get()
    VMwareManager.startVM(f"{vm_name}.vmwarevm")

def onStopClick():
    vm_name = vm_variable.get()
    VMwareManager.stopVM(f"{vm_name}.vmwarevm")

root = tk.Tk()
root.title("VM Manager")
root.geometry("500x160")
root.resizable(False, False)
root.grid_columnconfigure([0, 1, 2, 3], weight=1)

start_stop_frame = tk.Frame(root, width=480, height=140, highlightbackground="black", highlightthickness=2)
start_stop_frame.grid(row=0, column=0, columnspan=5, pady=(10, 5), padx=10)
# vm_info_frame = tk.Frame(root, width=435, height=140, highlightbackground="black", highlightthickness=2)
# vm_info_frame.grid(row=1, column=0, columnspan=4, pady=(5, 5), padx=10)
# vm_todo_frame = tk.Frame(root, width=435, height=140, highlightbackground="black", highlightthickness=2)
# vm_todo_frame.grid(row=2, column=0, columnspan=4, pady=(5, 5), padx=10)

vm_name_label = tk.Label(root, text="VM Name")
vm_name_label.grid(row=0, column=0, padx=10, pady=10)

vm_variable = tk.StringVar(root)
vm_variable.set(VMwareManager.VMs[0])
dropdown = tk.OptionMenu(root, vm_variable, *VMwareManager.VMs)
dropdown.grid(row=0, column=1, padx=10, pady=10)

start_button = tk.Button(root, text="Start", command=onStartClick)
start_button.grid(row=0, column=2, padx=(10, 2.5), pady=10)
stop_button = tk.Button(root, text="Stop", command=onStopClick)
stop_button.grid(row=0, column=3, padx=(2.5, 10), pady=10)


root.mainloop()