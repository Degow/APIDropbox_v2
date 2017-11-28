"""
	DESCRIPTION:	Subir archivos a Dropbox de una determinada carpeta
	EJERCICIOS:	
		TOKEN = Token de la aplicacion
		RUTA_DESTINO = ruta en donde grardar el archivo
				>> no es necesario especificar el nombre
"""

import dropbox, sys, os

dbx = dropbox.Dropbox('TOKEN')
rootdir = '<RUTA_DIRECTORIO>' 

print ("Attempting to upload...")

# Walk recorre una carpeta retornando los directorios, carpetas, archivos
for dir, dirs, files in os.walk(rootdir):
    for file in files:
        try:
            file_path = os.path.join(dir, file)
            dest_path = os.path.join('<RUTA_DESTINO>', file)
            print('Uploading {} to {}'.format(file_path, dest_path))
            with open(file_path, 'rb') as f:
                dbx.files_upload(f.read(), dest_path, mute=True)
        except Exception as err:
            print("Failed to upload {}\n{}".format(file, err))

print("Finished upload.")