from tkinter import filedialog
import view


f1=filedialog.askopenfilename(defaultextension="*.*",title="file open")
view.views(files=f1)
