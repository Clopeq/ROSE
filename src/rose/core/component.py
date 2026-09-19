

class Component:
    _input_ports:  tuple [str, ...] = ()  # just names of the parameters, the objects connections are defined in graph class
    _output_ports: tuple [str, ...] = ()

    def __init__(self, name: str):
        self.name = name
        self.in_values: dict[str, float] = {}
        self.out_values: dict[str, float] = {}

    @property
    def input_ports(self):
        return self._input_ports

    @property
    def output_ports(self):
        return self._output_ports