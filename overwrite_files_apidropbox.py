""" 
	Existen diferentes variables para el metodo 
	dropbox.files.WriteMode.<VARIABLES>
	VARIABLES:
		- overwrite
		- add
		- update
"""

import dropbox

dbx = dropbox.Dropbox('<TOKEN>')

with open('<RUTA_ARCHIVO>', 'rb') as f:
    dbx.files_upload(f.read(), '/<RUTA_REMOTA>', mode=dropbox.files.WriteMode.overwrite)
