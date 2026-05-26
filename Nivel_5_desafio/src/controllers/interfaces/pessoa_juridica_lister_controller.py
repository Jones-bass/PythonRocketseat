from typing import Dict
from abc import ABC, abstractmethod

class PessoaJuridicaListerControllerInterface(ABC):

    @abstractmethod
    def list(self) -> Dict:
        pass
