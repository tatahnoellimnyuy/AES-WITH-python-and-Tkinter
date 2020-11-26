from Crypto import Random
from Crypto.Cipher import AES
from tkinter import *
import random 
import tkFileDialog
import sys
import tkinter.messagebox

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)
#encrypting a file section
 ## defining the function to generate a random key
#key = ""#.join(chr(random.randint(0, 0xFF)) for i in range(16))
# print ('key', [x for x in key])
 
 # adding the padding to make the string an eligeble block size
def pad(s):
 return s+b"\0"*(AES.block_size-len(s)%AES.block_size)


#function to encyrpt 
def encrypt(message,key_size=256):
 message=pad(message)
#generating a value
 key = "".join(chr(random.randint(0, 0xFF)) for i in range(16))
 print ('the encyption key is in quotes', key)
 string=""
 string=string+key
 # popupmsg()
 tkinter.messagebox.showinfo('encryption key','file has been encrypted with key ') 
 iv=Random.new().read(AES.block_size)
 cipher=AES.new(key,AES.MODE_CBC,iv)
# encrypted character
 return iv+cipher.encrypt(message)

# decryption function 
def decrypt(ciphertext,key):
	iv=ciphertext[:AES.block_size]
	cipher=AES.new(key,AES.MODE_CBC,iv)
	plaintext=cipher.decrypt(ciphertext[AES.block_size:])
	return plaintext.rstrip(b"\0")


# encypting a file
file_name=None
def encrypt_file(file_name):
	with open(file_name,'rb')as f:
		plaintext=f.read()# store the text from the file
	enc=encrypt(plaintext)
	with open(file_name+".toxic",'wb') as f:
		f.write(enc)# writing the encrypted text into the file



#decrypting a file
def decrypt_file(file_name,key):
	with open(file_name,'rb') as f:
		ciphertext=f.read()
	dec=decrypt(ciphertext,key)
	with open(file_name[:-4],'wb') as f:
		f.write(dec) #writing the decrypted text into the file
		
#loading the file
def load_file():
	global key,file_name
	text_file=tkFileDialog.askopenfile(filetypes=[('Text Files','txt')]) #setting the file type and the the extention
	if text_file.name !=None:
			file_name=text_file.name#gettin the file name

def encrypt_the_file():
	global file_name
	if file_name != None:
		fname=file_name
		encrypt_file(fname)
	else:
		messagebox.showerror(title="you foo error",message="there was no file loadedto encrypt")

  
  
def decrypt_the_file():
 key=retrieve_input()
 print(key)
 global file_name
 if file_name !=None:
		fname=file_name+ ".toxic"
  # key=retrieve_input()
		decrypt_file(fname,key)
 else:
		messagebox.showerror(title="you foo error",message="there was no file loadedto decrypt")
	

root = Tk()
labelfont = ('times', 20, 'bold')
widget = Label(root, text='AES Encryption, Work 3 . level4 gtel ')
widget.config(bg='grey', fg='blue')
widget.config(font=labelfont)
widget.config(height=6, width=30)
widget.pack(expand=YES, fill=BOTH)



widget = Button(text='laod file', padx=10, pady=10)
widget.pack(padx=20, pady=20)
widget.config(cursor='gumby')
widget.config(bd=8, relief=RAISED)
widget.config(bg='dark blue', fg='white')
widget.config(font=('helvetica', 20, 'underline italic'))
widget.config(command=load_file)


widget = Button(text='Encrypt file', padx=10, pady=10)
widget.pack(padx=20, pady=20)
widget.config(cursor='gumby')
widget.config(bd=8, relief=RAISED)
widget.config(bg='dark blue', fg='white')
widget.config(font=('helvetica', 20, 'underline italic'))
widget.config(command=encrypt_the_file)
	
def retrieve_input():
    inputValue= ("%s" % textBox.get('1.0', END+'-1c'))
    print(inputValue)
    return(inputValue)

textBox=Text(root, height=2, width=80)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Commit", 
                    command=lambda: retrieve_input())
textBox.insert('1.0', 'delete this then paste the decryption key')

widget= Button(text='dEcrypt file', padx=10, pady=10)
widget.pack(padx=20, pady=20)
widget.config(cursor='gumby')
widget.config(bd=8, relief=RAISED)
widget.config(bg='dark blue', fg='white')
widget.config(font=('helvetica', 20, 'underline italic'))
widget.config(command=decrypt_the_file)


class StdoutRedirector(object):

    def __init__(self, text_area):
        self.text_area = text_area

    def write(self, str):
        self.text_area.insert(END, str)
        self.text_area.see(END)



text = Text()
text.config(font=('courier', 15, 'normal'))
text.config(width=20, height=10)
text.pack(expand=YES, fill=BOTH)
text.insert('1.0', 'Highlight and Ctrl+C To Copy\n\n')


sys.stdout = StdoutRedirector(text)

def create_widgets(self):
 self.hi_there = tk.Button(self)
 self.hi_there["text"] = "Hello World\n(click me)"
 self.hi_there["command"] = self.say_hi
 self.hi_there.pack(side="top")

 self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
 self.quit.pack(side="bottom")


root.mainloop()