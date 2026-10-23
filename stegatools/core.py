"""
Interface común abstracta para todos los portadores.
Cada módulo (meta, lsb, unicode) debe implementar estas 4 funciones.
"""
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Protocol

class Portador(Protocol):
    """Protocolo que define la interfaz mínima de cualquier portador."""
    
    @staticmethod
    def get_capacity(carrier_path: str) -> int:
        """Devuelve la capacidad máxima en bytes que este portador puede contener."""
        ...
    
    @staticmethod
    def embed(carrier_path: str, payload: bytes, output_path: str) -> None:
        """Incrusta el payload en el portador y guarda el resultado."""
        ...
    
    @staticmethod
    def extract(carrier_path: str) -> bytes:
        """Extrae el payload oculto del portador."""
        ...
    
    @staticmethod
    def detect(carrier_path: str) -> bool:
        """Esteganálisis básico: devuelve True si sospecha que hay algo oculto."""
        ...
