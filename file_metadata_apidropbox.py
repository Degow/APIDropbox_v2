"""
	RUTA_REMOTA = ruta donde se encuentra el archivo
			especifica el nombre
"""

import dropbox

dbx = dropbox.Dropbox('<TOKEN>')
md = dbx.files_get_metadata('/<RUTA_REMOTA>')

nombre = md.name
fecha = md.client_modified
ubicacion = md.path_display

print("Nombre del Archivo:\t", nombre)
print("Fecha de registro:\t", fecha)
print("Ubicacion del archivo:\t", ubicacion)
