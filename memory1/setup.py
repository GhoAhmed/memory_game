#setup
import cx_Frezze

executables = [cx_Frezze.Executable("demo.py")]

cx_Frezze.setup(
	name = "Memory"
	options = {"build_exe": {"packages":["pygame","tkinter"], "includes_files":["images","cover.png"]}}
	)