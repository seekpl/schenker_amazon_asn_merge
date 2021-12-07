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
	path_schenker = e1.insert(END, filename) # add this
	return (path_schenker)


def open_file_asn():
	filename = askopenfilename(filetypes=(("pdf file", "*.pdf"), ("All files", "*.*"),))
	path_asn = e2.insert(END, filename) # add this
	return(path_asn)


def pdf2img():
	try:
		images = convert_from_path(str(e1.get()))
		images2 = convert_from_path(str(e2.get()))

		for i, image in enumerate(images):
			fname = 'converted/' + str(i) + '.png'
			image.save(fname, "PNG")

		for img in images2:
			img.save('converted/asn.png', 'PNG')

	except:
		Result = "No PDF files."
		messagebox.showinfo("Message", Result)

	else:
		Result = "JPG files are ready."
		messagebox.showinfo("Message", Result)


def cut():
	# Opens a image in RGB mode
	im = Image.open(r"converted/asn.png")

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
	im1 = im.crop((left, top, right, bottom))
	im2 = im.crop((left2, top2, right2, bottom2))

	# Shows the image in image viewer
	im1.save('converted/asn_nr.png', 'PNG')
	im1 = Image.open('converted/asn_nr.png')
	im1 = im1.rotate(-90, expand=True)
	im1.save('converted/asn_nr.png', 'PNG')
	im1 = im1.resize((70, 169), Image.ANTIALIAS)
	im1.save('converted/asn_nr.png', 'PNG')

	im2.save('converted/asn_ean.png', 'PNG')


def merge():
	img = Image.open('converted/asn_ean.png').convert("RGBA")
	img2 = Image.open('converted/asn_nr.png').convert("RGBA")

	background1 = Image.open('converted/0.png').convert("RGBA")
	background2 = Image.open('converted/1.png').convert("RGBA")
	background3 = Image.open('converted/2.png').convert("RGBA")
	background4 = Image.open('converted/3.png').convert("RGBA")

	background1.paste(img, (180, 1020), img)
	background2.paste(img, (180, 1020), img)
	background3.paste(img, (180, 1020), img)
	background4.paste(img, (180, 1020), img)

	background1.paste(img2, (720, 1040), img2)
	background2.paste(img2, (720, 1040), img2)
	background3.paste(img2, (720, 1040), img2)
	background4.paste(img2, (720, 1040), img2)

	background1.save('converted/generated_files/strona_1.png', 'PNG')
	background2.save('converted/generated_files/strona_2.png', 'PNG')
	background3.save('converted/generated_files/strona_3.png', 'PNG')
	background4.save('converted/generated_files/strona_4.png', 'PNG')


master.title('Schenker ASN Merger')
master.geometry('420x140')

Label(master, text="Schenker").grid(row=0)
Label(master, text="AMAZON").grid(row=1)

e1 = Entry(master, font=40)
e2 = Entry(master, font=40)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

open_button_schenker = ttk.Button(master, text='Open PDF', command=open_file_schenker)
open_button_asn = ttk.Button(master, text='Open PDF', command=open_file_asn)

open_button_schenker.grid(column=2, row=0, padx=10, pady=10)
open_button_asn.grid(column=2, row=1, padx=10, pady=10)

convert_button = Button(master, text="Convert", command=(pdf2img))
convert_button.grid(row=4, column=0, columnspan=1, rowspan=4, padx=10, pady=10)

cut_button = Button(master, text="Cut ASN number", command=(cut))
cut_button.grid(row=4, column=1, columnspan=1, rowspan=4, padx=10, pady=10)

merger_button = Button(master, text="Merge", command=(merge))
merger_button.grid(row=4, column=2, columnspan=1, rowspan=4, padx=10, pady=10)

master.mainloop()
