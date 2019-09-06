from dataclasses import dataclass

from dataclasses_json import dataclass_json

from DOU_HTML.DOU_HTML.model import dou_licitacao


@dataclass
@dataclass_json
class LicitacaoComTags:
    data: dou_licitacao
    tag_pregao: str  # presencial eletronico
    tag_tipo: str  # produto servico ambos
