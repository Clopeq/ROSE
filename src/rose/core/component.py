from abc import ABC, abstractmethod

class Component(ABC):
    _input_ports:  tuple [str, ...] = ()  # just names of the parameters, the objects connections are defined in graph class
    _output_ports: tuple [str, ...] = ()

    def __init__(self):
        pass

    @abstractmethod
    def evaluate(self):
        """ Evry child class must implement this """

    @abstractmethod
    def advance(self):
        """ Evry child class must implement this """

    @abstractmethod
    def read_port(self, port: str):
        """ Evry child class must implement this """

    @property
    def input_ports(self):
        return self._input_ports

    @property
    def output_ports(self):
        return self._output_ports