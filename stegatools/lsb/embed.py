from typing import Optional

def embed(carrier_path: str, payload: bytes, output_path: str,
          channel_mode: str = "rgb_all") -> None:
    """
    Incrusta datos usando LSB en imágenes PNG/BMP.
    
    Args:
        carrier_path: Ruta a la imagen portadora
        payload: Datos binarios a ocultar
        output_path: Ruta donde guardar la imagen modificada
        channel_mode: Modo de canal ('rgb_all', 'r_only', 'g_only', 'b_only')
    
    Importante: Guarda SIEMPRE en PNG o BMP. JPEG destruye los bits.
    """
    raise NotImplementedError("Módulo en desarrollo")
