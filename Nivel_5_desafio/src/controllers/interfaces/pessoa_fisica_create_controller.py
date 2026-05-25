from typing import Dict
from abc import ABC, abstractmethod

class PessoaFisicaCreateControllerInterface(ABC):

    @abstractmethod
    def create(self, pessoa_fisica_info: Dict) -> Dict:
        pass