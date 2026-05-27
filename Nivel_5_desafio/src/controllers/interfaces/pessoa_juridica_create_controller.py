from typing import Dict
from abc import ABC, abstractmethod

class PessoaJuridicaCreateControllerInterface(ABC):

    @abstractmethod
    def create(self, pessoa_juridica_info: Dict) -> Dict:
        pass