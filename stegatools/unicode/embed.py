def embed(carrier_text: str, payload: bytes) -> str:
    """
    Incrusta datos en texto usando caracteres Unicode de ancho cero.
    
    Mapeo sugerido:
    - U+200B (Zero Width Space) = 0
    - U+200C (Zero Width Non-Joiner) = 1
    - U+200D (Zero Width Joiner) = Separador de bytes
    
    Args:
        carrier_text: Texto visible que acompañará al payload
        payload: Datos binarios a ocultar
    
    Returns:
        Texto con caracteres invisibles intercalados.
    
    Advertencia: Detectable trivialmente buscando estos códigos Unicode.
    """
    raise NotImplementedError("Módulo en desarrollo")
