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
    def __init__(self):
        self._components: list[Component] = []
        self._connections: list[Connection] = []
        self._open_ports: dict = {}

    def add_component(self, component: Component) -> None:
        """ Add new component (node) to the graph """
        if component in self._components:
            raise DuplicateComponentError(f"Duplicate components are not allowed! Create new instance first.")

        self._components.append(component)
        self._open_ports[component] = list(component.input_ports)

    def add_connection(self, connection: Connection) -> None:
        """ Add new connection (edge) to the graph connecting two components (nodes) """

        if connection.source not in self._components:
            raise ValueError(f"The source does not exist: {type(connection.source).__name__}")
        if connection.destination not in self._components:
            raise ValueError(f"The destination does not exist: {type(connection.destination).__name__}")
        if connection.source_port not in connection.source.output_ports:
            raise ValueError(f"{connection.source_port} is not an output port of {type(connection.source).__name__}")
        if connection.destination_port not in connection.destination.input_ports:
            raise ValueError(f"The destination does not have a valid port: {connection.destination_port}")
        if connection.destination_port not in self._open_ports[connection.destination]:
            raise PortUnavailableError(f"The destination port is already connected elswhere: {connection.destination_port}")

        self._open_ports[connection.destination].remove(connection.destination_port)
        self._connections.append(connection)


    def remove_component(self, component: Component) -> bool:
        """
        Returns:
            True - if the component has been deleted
            False - if the component has not been found
        """

        if component not in self._components:
            return False
        
        # remove any connection to the component being removed
        for connection in self._connections:
            if connection.destination == component or connection.source == component:
                self._connections.remove(connection)

        # removes any tracked open ports associated with the component being removed
        self._open_ports.pop(component, None)   

        self._components.remove(component)
        return True

    def remove_connection(self, connection: Connection) -> bool:
        if connection not in self._connections:
            return False

        # free up the destination port first before removing the connection
        self._open_ports[connection.destination].append(connection.destination_port)
        self._connections.remove(connection)
        return True

    def validate(self) -> bool:
        """ Validate if all of the input ports are fed.
            Returns:
            True - if all of the input ports are fed
            False - if at least one input port is open 
        """

        for component in self._components:
            for port in component.input_ports:
                c = [con.destination_port for con in self._connections if con.destination == component]
                if port not in c:
                    return False
        return True

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