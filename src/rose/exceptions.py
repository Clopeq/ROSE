

class DuplicateComponentError(Exception):
    """ Exception raised when trying to add a component that already exists """

class PortUnavailableError(Exception):
    """ Exception raised when the port is already occupied by another connection """