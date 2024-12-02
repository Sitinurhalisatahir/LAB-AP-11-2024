def akronim():
	teks = input("Masukkan Teks: ")

	kalimat = teks.split()
	acronym = ''
	for kata in kalimat:
		acronym += kata[0].upper()

	print(acronym)

akronim()