"""
Utilidades compartidas entre todos los portadores.
"""
def bytes_to_bits(data: bytes) -> list[int]:
    """Convierte bytes a lista de bits (MSB-first)."""
    bits = []
    for byte in data:
        for i in range(7, -1, -1):
            bits.append((byte >> i) & 1)
    return bits

def bits_to_bytes(bits: list[int]) -> bytes:
    """Convierte lista de bits a bytes (MSB-first)."""
    # Agrupa en grupos de 8 y convierte cada grupo a byte
    result = []
    for i in range(0, len(bits), 8):
        chunk = bits[i:i+8]
        if len(chunk) == 8:
            byte_val = 0
            for j, bit in enumerate(chunk):
                byte_val |= (bit << (7 - j))
            result.append(byte_val)
    return bytes(result)

def calculate_crc32(data: bytes) -> int:
    """Calcula CRC-32 para integridad básica."""
    import zlib
    return zlib.crc32(data) & 0xffffffff

def make_magic_bytes(magic_str: str = "STGT") -> bytes:
    """Genera bytes mágicos para identificar un payload de StegaTools."""
    return magic_str.encode('utf-8')[:4]
