from dataclasses import dataclass


@dataclass
class LicitacaoOut:
    titulo: str
    dados: str
    pregao: str
    tipo: str


@dataclass
class LicitacaoOut2:
    titulo: str
    dados: str
    pregao: str
    tipo: str
    empresa: str
