# Aplicación Python conectada a una Base de Datos MySQL en Clever Cloud

Este repositorio contiene el código de una aplicación Python que se conecta a una base de datos MySQL alojada en Clever Cloud. La aplicación permite realizar consultas sobre las tablas de la base de datos.

## Instrucciones de Instalación

1. Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/ismael123439/tp8.git
```

2. Instala las dependencias necesarias. Recomiendo usar un entorno virtual:

```bash
cd nombre_repositorio
python3 -m venv venv
source venv/bin/activate      # En Linux/Mac
venv\Scripts\activate.bat     # En Windows
pip install -r requirements.txt
```

## Configuración de la Base de Datos

Antes de ejecutar la aplicación, asegúrate de configurar correctamente la conexión a la base de datos MySQL en Clever Cloud. Modifica el archivo `config.py` con los datos de tu base de datos:

```python
# config.py

DB_CONFIG = {
    'host': 'tu_host',
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'database': 'nombre_base_de_datos'
}
```

## Ejecución de la Aplicación

Una vez configurada la conexión a la base de datos, puedes ejecutar la aplicación:

```bash
python app.py
```

## Funcionalidad de la Aplicación

La aplicación permite realizar las siguientes operaciones:

1. **Consulta de Datos**: Permite realizar consultas SELECT a las tablas de la base de datos.
2. **Inserción de Datos**: Permite agregar nuevos registros a las tablas de la base de datos mediante consultas INSERT.
3. **Eliminación de Datos**: Permite eliminar registros de las tablas de la base de datos mediante consultas DELETE.