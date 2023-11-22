# Challenge_removables
Challenge que genera una clave en función del número de dispositivos extraíbles conectados al ordenador. Permite ser utilizado para detectar cuando se conectan determinados medios extraíbles independientemente del usuario que utilice el equipo. 
Genera la clave mediante la concatenación de los nombres de los extraíbles.


## Prerrequisitos

Instalar la librería `win32file` con `pip install pywin32`


ejemplo de configuracion json
```json
{
	"FileName": "removables_challenge.dll",
	"Description": "Challenge that generates a key based on the number of removable devices connected to the computer..",
	"Props": {
		"validity_time": 3600,
		"refresh_time": 3000
	},
	"Requirements": "none"
}
```

## Funcionamiento

Todas las funciones y la lógica del challenge se encuentran en el fichero removable_challenge.py, el cual es un programa en python que contiene toda la lógica del challenge. La función principal dentro del fichero que gestiona toda la lógica del challenge es locate_usb(), la cual devuelve la lista de dispositivos extraíbles conectados.

Primero hay que llamar al método win32file.GetLogicalDrives() para obtener la lista de dispositivos lógicos. Después, mediante el método GetDriveType() se obtiene el tipo de dispositivo lógico y posteriormente win32file.DRIVE_REMOVABLE para comprobar que es un dispositivo extraíble. Con la lista definitiva, se almacena en un array y se genera una clave concatenando todos los dispositivos extraíbles conectados.

Aplicable fundamentalmente a PCs personales (aunque también podría ser a servidores). El contexto de seguridad requiere de la concurrencia de varios dispositivos extraíbles conectados para que se revele el contenido. Sería necesario disponer de una o varias “llaves”, entregadas físicamente en las circunstancias que la organización decida, a los usuarios de ese equipo para que pueda utilizarlo. Aunque sea un usuario con permisos, requiere que la organización le provea de la “llave USB” para que opere en la circunstancia correcta.

Pretende evitar situaciones como: 
- Que un usuario (cualquiera, no por parámetro) se lleve, por ejemplo, un PC corporativo a su casa y pueda operar con él.
- Que un usuario pueda realizar actividades sobre un PC en una ubicación concreta (ej. Mantenimiento de equipos de la red OT ).
