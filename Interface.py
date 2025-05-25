from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def get_salario(self):
        pass

class FuncionarioCLT(Funcionario):
    @abstractmethod
    def get_fgts(self):
        pass

class FuncionarioPublico(Funcionario):
    @abstractmethod
    def get_siape(self):
        pass

class FuncionarioIncorreto(ABC):
    @abstractmethod
    def get_salario(self):
        pass

    @abstractmethod
    def get_fgts(self):
        pass

    @abstractmethod
    def get_siape(self):
        pass