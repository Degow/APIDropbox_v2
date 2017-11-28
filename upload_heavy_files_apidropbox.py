"""
	Recomendacion:
		El archivo no debe pesar mas de 150 MB
	files_upload_session_start = Sesion de carga 
		Permite para cargar un solo archivo en una 
		o mas solucitudes
	files_upload_session_finish = Finaliza la sesion
		de carga y los guarda en la ruta de archivo dada
	files_upload_session_append = Agregar mas datos
		a una sesion de carga.
"""

import os
import dropbox

dbx = dropbox.Dropbox('<TOKEN>')

file_path = '<ARCHIVO_LOCAL>'
dest_path = '<RUTA_DESTINO>'

f = open(file_path, 'rb')
file_size = os.path.getsize(file_path)

CHUNK_SIZE = 4 * 1024 * 1024

if file_size == CHUNK_SIZE:
    print(dbx.files_upload(f.read(), dest_path))

else:
    upload_session_start_result = dbx.files_upload_session_start(f.read(CHUNK_SIZE))
    cursor = dropbox.files.UploadSessionCursor(session_id=upload_session_start_result.session_id,
                                               offset=f.tell())

    commit = dropbox.files.CommitInfo(path=dest_path)

    while f.tell() < file_size:
        if ((file_size - f.tell()) <= CHUNK_SIZE):
            print(dbx.files_upload_session_finish(f.read(CHUNK_SIZE),
                                            cursor,
                                            commit))
        else:
            dbx.files_upload_session_append(f.read(CHUNK_SIZE),
                                            cursor.session_id,
                                            cursor.offset)
            cursor.offset = f.tell()
f.close()