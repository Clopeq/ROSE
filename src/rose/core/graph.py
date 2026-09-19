from .component import Component
from dataclasses import dataclass
from ..exceptions import DuplicateComponentError, PortUnavailableError

@dataclass
class Connection:
    source: Component
    source_port: str
    destination: Component
    destination_port: str


class Graph:
    # graph should have all of the components and their connections inside

    _components: list[Component] = []
    _connections: list[Connection] = []
    _open_ports: dict = {}

    def __init__(self):
        pass

    def add_component(self, component: Component) -> None:
        """ Add new component (node) to the graph """
        if component in self._components:
            raise DuplicateComponentError(f"Duplicate components are not allowed! Create new instance first.")

        self._components.append(component)
        self._open_ports[component] = component.input_ports

    def add_connection(self, connection: Connection) -> None:
        """ Add new connection (edge) to the graph connecting two components (nodes) """

        if not connection.source_port in connection.source.output_ports:
            raise ValueError(f"The source does not have a valid port: {connection.source_port}")

        if not connection.destination_port in connection.destination.input_ports:
            raise ValueError(f"The destination does not have a valid port: {connection.destination_port}")

        if not connection.destination_port in self._open_ports[connection.destination]:
            raise PortUnavailableError(f"The destination port is already connected elswhere: {connection.destination_port}")

        self._open_ports[connection.destination].remove(connection.destination_port)
        self._connections.append(connection)


    def remove_component(self, component: Component) -> bool:
        """
        Returns:
            True - if the component has been deleted
            False - if the component has not been found
        """

        if component in self._components:
            self._components.remove(component)
            return True
        return False

    def remove_connection(self, connection: Connection) -> bool:

        if connection in self._connections:
            self._connections.remove(connection)
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

    @property
    def components(self):
        return self._components

    @property 
    def connections(self):
        return self._connections