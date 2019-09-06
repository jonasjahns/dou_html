from dataclasses import dataclass, field
from typing import List
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class DouLicitacao:
    headers: List[str] = field(default_factory=list)
    titulos: List[str] = field(default_factory=list)
    corpo: List[str] = field(default_factory=list)
    publicador: List[str] = field(default_factory=list)
