from tkinter import *
import onetimepad
root = Tk()
root.title("Encryption Decryption GUI")
root.geometry("1600x1200")

# function for encryption
def encryptMessage():
    pt = en1.get()
    ctee = onetimepad.encrypt(pt, 'random')
    message = ctee
    cipher = ''
    i = len(message) - 1

    while i >= 0:
        cipher = cipher + message[i]
        i = i - 1
    en2.insert(0, ctee)
    en3.insert(0, cipher)
    en4.insert(0, cipher)

# function for decryption
def decryptMessage():
    ct1 = en4.get()
    message = ct1
    tra = ''
    i = len(message) - 1

    while i >= 0:
        tra = tra + message[i]
        i = i - 1
    en5.insert(0, tra)
    pt1 = onetimepad.decrypt(tra, 'random')
    en6.insert(0, pt1)

# function for refresh
def refreshMessage():
    en1.delete(0,'end')
    en2.delete(0, 'end')
    en5.delete(0, 'end')
    en3.delete(0, 'end')
    en6.delete(0, 'end')
    en4.delete(0, 'end')

# creating labels and positioning them on the grid
label1 = Label(root, text='User input', fg='blue', font=('Helvetica', 28))
label1.grid(row=10, column=1)
label2 = Label(root, text='Encrypted text', fg='gray', font=('Helvetica', 20))
label2.grid(row=11, column=1)
label3 = Label(root, text='Revers text', fg='green', font=('Helvetica', 20))
label3.grid(row=12, column=1)
lable4 = Label(root, text="Received revers text", fg='green', font=('Helvetica', 20))
lable4.grid(row=14, column=1)
label5 = Label(root, text="Cipher text", fg='gray', font=('Helvetica', 20))
label5.grid(row=15, column=1)
label6 = Label(root, text="Receiver text", fg='blue', font=('Helvetica', 28))
label6.grid(row=16, column=1)
label7 = Label(root, text='Please press the "Refresh" button !!!', fg='red', font=('Helvetica', 15))
label7.grid(row=19, column=1)
label8 = Label(root, text='To send a new message.', fg='red', font=('Helvetica', 15))
label8.grid(row=20, column=1)
# creating entries and positioning them on the grid
en1 = Entry(root, width=80, fg='blue', font=('Helvetica', 20))
en1.grid(row=10, column=2)
en2 = Entry(root, width=80, fg='red', font=('Helvetica', 10))
en2.grid(row=11, column=2)
en3 = Entry(root, width=80, font=('Helvetica', 10))
en3.grid(row=12, column=2)
en4 = Entry(root, width=80, font=('Helvetica', 10))
en4.grid(row=14, column=2)
en5 = Entry(root, width=80, fg='red', font=('Helvetica', 10))
en5.grid(row=15, column=2)
en6 = Entry(root, width=80, fg='green', font=('Helvetica', 20))
en6.grid(row=16, column=2)


send = Button(root, text="Send", bg="red", fg="blue", command=encryptMessage)
send.grid(row=13, column=2)
receive = Button(root, text="Receive", bg="green", fg="green", command=decryptMessage)
receive.grid(row=17, column=2)
refresh = Button(root, text="Refresh", bg="green", fg="red", command=refreshMessage)
refresh.grid(row=22, column=2)

root.mainloop()