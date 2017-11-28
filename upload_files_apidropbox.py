"""
EJEMPLOS:
	TOKEN = Token de la aplicación
	RUTA_ARCHIVO_LOCAL = Ruta donde se encuentra
			a subir. 
	RUTA_REMOTA = Ruta Dropbox para guardar archivo
"""

import dropbox

dbx = dropbox.Dropbox("TOKEN")

with open("<RUTA_ARCHIVO_LOCAL>", "rb") as f:
	dbx.files_upload(f.read(), "/<RUTA_REMOTA>", mute=True)
