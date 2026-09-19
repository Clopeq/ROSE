

class Component:
    inputs:  tuple [str, ...] = ()  # just names of the parameters, the objects connections are defined in graph class
    outputs: tuple [str, ...] = ()

    def __init__(self, name: str):
        self.name = name
        self.in_values: dict[str, float] = {}
        self.out_values: dict[str, float] = {}