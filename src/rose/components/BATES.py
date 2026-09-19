from ..core.component import Component

class BATES(Component):
# ------------------------- PRIVATE ATTRIBUTES -------------------------
    _initial_segment_length   = None  # m, Length of the grain segment
    _current_segment_length   = None 
    _initial_outside_diameter = None  # m, Outside diameter of grain segment
    _current_outside_diamter  = None
    _initial_port_diameter    = None  # m, Inside diameter of grain segment
    _current_port_diameter    = None
    _number_of_segments       = None  #     Number of grain segments
    _initial_segment_spacing  = 0     # m, Spacing inbetween grain segments, defaults to 0 mm
    _current_segment_spacing  = 0 

    _burn_distance = 0     # m,  Burn distance
    _burning_area  = None  # m2, Burning area

    _required_inputs = [""]

    def __init__(self,
            segment_length:     float, 
            outside_diamter:    float, 
            port_diameter:      float, 
            number_of_segments: int = 1, 
            segment_spacing:    float = 0
        ):
        """ Constructor
        """

        # TODO: Check inputs here

        self._initial_segment_length   = segment_length
        self._current_segment_length   = segment_length
        self._initial_outside_diameter = outside_diamter
        self._current_outside_diamter  = outside_diamter
        self._initial_port_diameter    = port_diameter
        self._current_port_diameter    = port_diameter
        self._number_of_segments       = number_of_segments
        self._initial_segment_spacing  = segment_spacing
        self._current_segment_spacing  = segment_spacing

        self._burn_distance = 0
        self._burning_area  = self._calculate_burning_area(self._burn_distance)

# ------------------------- PRIVATE METHODS -------------------------

    def _calculate_burning_area(self, burn_distance: float = 0):
        pass


# ------------------------- PUBLIC METHODS -------------------------
    def evaluate(self):
        pass

    def integrate(self):
        pass

    def define_connection(self, component, parameters):
        pass

# ------------------------- GETTERS AND SETTERS -------------------------
    @property
    def L(self):
        return (self._L - 2*self._x)

    @property
    def OD(self):
        return self._OD

    @property
    def ID(self):
        return (self._ID + 2*self._x)

    @property
    def N(self):
        return self._N

    @property
    def h(self):
        return self._h

    @property
    def Ab(self):
        return self._calculate_burning_area(self._burn_distance)