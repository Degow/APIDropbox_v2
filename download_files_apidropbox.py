"""
EJEMPLOS:
	TOKEN = Token de tu aplicación
	ARCHIVO_LOCAL = Poner la ruta del archivo 
			en el que se va almacenar.
	RUTA_REMOTA = LA ruta donde se encuentra 
			tu archivo en Dropbox.
"""

import dropbox

dbx = dropbox.Dropbox("TOKEN")

with open("<ARCHIVO_LOCAL>", "wb") as f:
    md, res = dbx.files_download(path="/<RUTA_REMOTA>")
    f.write(res.content)