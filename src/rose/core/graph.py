from .component import Component
from dataclasses import dataclass

@dataclass
class Connection:
    origin: Component
    origin_port: str
    destination: Component
    destination_port: str


class Graph:
    # graph should have all of the components and their connections inside

    components: dict[str, Component]
    connections: list[Connection]

    def __init__(self):
        pass

    def add_component(self, component: Component):
        self.components[component.name] = Component

    def add_connection(self, origin: Component, origin_port: str, destination: Component, destination_port: str) -> Connection:
        """
        Returns:
            Connection dataclass created by this method
        """
        # TODO check if origin port is valid
        # TODO check if destination port is valid

        connection = Connection(origin, origin_port, destination, destination_port)
        self.connections.append(connection)
        return connection

    def remove_component(self, component: Component) -> bool:
        """
        Returns:
            True - if the component has been deleted
            False - if the component has not been found
        """

        if component.name in self.components.keys:
            del self.components[component.name]
            return True
        return False

    def evaluate(self) -> None:
        """ Evaluate (calculate) each node of the graph, do not advance the timestap, no integration will happen """
        pass

    def advance(self) -> None:
        """ Advance the time in the simulation, .advance() component, this should move forward the simulation, the fuel should regress, the liquids should get depleted, etc. """
        pass

    def run(self) -> None:
        """ run the entire simulation """
        pass