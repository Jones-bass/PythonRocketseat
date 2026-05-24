from typing import Dict
from abc import ABC, abstractmethod

class PessoaFisicaListerControllerInterface(ABC):

    @abstractmethod
    def list(self) -> Dict:
        pass
