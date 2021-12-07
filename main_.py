from pdf2image import convert_from_path
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
# from tkinter import filedialog as fd
from tkinter.filedialog import askopenfilename
from PIL import Image

master = Tk()

def open_file_schenker():
   filename = askopenfilename(filetypes=(("pdf file", "*.pdf"), ("All files", "*.*"),))
   e1.insert(END, filename) # add this

def open_file_asn():
   filename = askopenfilename(filetypes=(("pdf file", "*.pdf"), ("All files", "*.*"),))
   e2.insert(END, filename) # add this

# def open_file_schenker():
#     # file type
#     filetypes = (
#         ('text files', '*.pdf'),
#         ('All files', '*.*')
#     )
#     # show the open file dialog
#     f = fd.askopenfilename(filetypes=(("pdf files","*.pdf"),("All files","*.*")))
#     # read the text file and show its content on the Text


# def open_file_asn():
#     # file type
#     filetypes = (
#         ('text files', '*.pdf'),
#         ('All files', '*.*')
#     )
#     # show the open file dialog
#     f = fd.askopenfile(filetypes=filetypes)
#     # read the text file and show its content on the Text
#     e2.insert("1.0", f.readlines())


def pdf2img():

	try:
		images = convert_from_path(str(e1.get()))

		images2 = convert_from_path('pdf/1.PDF')
		for img in images2:
			img.save('jpg/asn.png', 'PNG')

		for i, image in enumerate(images):
			fname = 'jpg/' + str(i) + '.png'
			image.save(fname, "PNG")

	except :
		Result = "No PDF files."
		messagebox.showinfo("Wynik", Result)

	else:
		Result = "JPG files are ready."
		messagebox.showinfo("Wynik", Result)


def cut():
	# Opens a image in RGB mode
	im = Image.open(r"jpg/asn.png")

	# Setting the points for cropped image
	left = 190
	top = 480
	right = 600
	bottom = 650

	left2 = 140
	top2 = 720
	right2 = 670
	bottom2 = 920

	# Cropped image of above dimension
	# (It will not change original image)
	im1 = im.crop((left, top, right, bottom))

	im2 = im.crop((left2, top2, right2, bottom2))

	# Shows the image in image viewer
	im1.save('jpg/asn_nr.png', 'PNG')
	im1 = Image.open('jpg/asn_nr.png')
	im1 = im1.rotate(-90, expand=True)
	im1.save('jpg/asn_nr.png', 'PNG')
	im1 = im1.resize((70, 169), Image.ANTIALIAS)
	im1.save('jpg/asn_nr.png', 'PNG')

	im2.save('jpg/asn_ean.png', 'PNG')


def merge():
	img = Image.open('jpg/asn_ean.png').convert("RGBA")
	img2 = Image.open('jpg/asn_nr.png').convert("RGBA")

	background1 = Image.open('jpg/0.png').convert("RGBA")
	background2 = Image.open('jpg/1.png').convert("RGBA")
	background3 = Image.open('jpg/2.png').convert("RGBA")
	background4 = Image.open('jpg/3.png').convert("RGBA")

	background1.paste(img, (180, 1020), img)
	background2.paste(img, (180, 1020), img)
	background3.paste(img, (180, 1020), img)
	background4.paste(img, (180, 1020), img)

	background1.paste(img2, (720, 1040), img2)
	background2.paste(img2, (720, 1040), img2)
	background3.paste(img2, (720, 1040), img2)
	background4.paste(img2, (720, 1040), img2)

	background1.save('jpg/generated_files/strona_1.png', 'PNG')
	background2.save('jpg/generated_files/strona_2.png', 'PNG')
	background3.save('jpg/generated_files/strona_3.png', 'PNG')
	background4.save('jpg/generated_files/strona_4.png', 'PNG')


master.title('Schenker ASN Merger')
master.geometry('400x140')

Label(master, text="Schenker").grid(row=0, sticky=W)
Label(master, text="AMAZON").grid(row=1, sticky=W)

e1 = Entry(master, font=40)
e2 = Entry(master, font=40)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# # Text editor
# text = tk.Text(master, height=1)
# text.grid(column=0, row=0, sticky='nsew')

open_button_schenker = ttk.Button(master, text='Open PDF', command=open_file_schenker)

open_button_asn = ttk.Button(master, text='Open PDF', command=open_file_asn)

open_button_schenker.grid(column=2, row=0, sticky='w', padx=10, pady=10)
open_button_asn.grid(column=2, row=1, sticky='w', padx=10, pady=10)


b = Button(master, text="Convert", command=(pdf2img))
b.grid(row=4, column=0, columnspan=1, rowspan=4, padx=10, pady=10)

c = Button(master, text="Cut ASN number", command=(cut))
c.grid(row=4, column=1, columnspan=1, rowspan=4, padx=10, pady=10)

d = Button(master, text="Merge", command=(merge))
d.grid(row=4, column=2, columnspan=1, rowspan=4, padx=10, pady=10)

master.mainloop()
