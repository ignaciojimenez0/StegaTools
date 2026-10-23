from typing import Optional

def embed(carrier_path: str, payload: bytes, output_path: str, 
          metadata_type: str = "exif") -> None:
    """
    Incrusta datos en metadatos de archivos.
    
    Args:
        carrier_path: Ruta al archivo portador (imagen, MP3, etc.)
        payload: Datos binarios a ocultar
        output_path: Ruta donde guardar el archivo modificado
        metadata_type: Tipo de metadato ('exif', 'id3', 'png_chunk')
    
    Nota: Los metadatos son detectables. No usar para ocultación seria.
    """
    raise NotImplementedError("Módulo en desarrollo")
