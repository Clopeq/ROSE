from ..core.component import Component
from scipy.constants import pi

class BATES(Component):
# ------------------------- PRIVATE ATTRIBUTES -------------------------
    _input_ports: tuple[str, ...] = ("regression_rate",)

    def __init__(self,
            segment_length:     float, 
            outside_diameter:    float, 
            port_diameter:      float, 
            number_of_segments: int = 1, 
            segment_spacing:    float = 0
        ):
        """ Constructor """

        if segment_length <= 0:
            raise ValueError(f"Segment length has to be positive number!")
        if outside_diameter <= 0:
            raise ValueError(f"Outside diameter has to be positive number!")
        if outside_diameter <= port_diameter:
            raise ValueError(f"Port diameter has to be smaller than the grain outside diameter!")
        if port_diameter <= 0:
            raise ValueError(f"Port diameter has to be positive number!")
        if number_of_segments <= 0:
            raise ValueError(f"Number of segments has to be a positive integer!")
        if segment_spacing < 0:
            raise ValueError(f"Segment spacing cannot be negative")

        self._initial_segment_length   = segment_length
        self._segment_length   = segment_length
        self._initial_outside_diameter = outside_diameter
        self._outside_diameter = outside_diameter
        self._initial_port_diameter    = port_diameter
        self._port_diameter    = port_diameter
        self._number_of_segments       = number_of_segments
        self._initial_segment_spacing  = segment_spacing
        self._segment_spacing  = segment_spacing

        self._burn_distance = 0
        self._burning_area  = self._calculate_burning_area()

        self._output_ports: dict = {
            "segment_length":     self._segment_length,
            "port_diameter":      self._port_diameter,
            "outside_diameter":   self._outside_diameter,
            "number_of_segments": self._number_of_segments,
            "segment_spacing":    self._segment_spacing,
            "burn_distance":      self._burn_distance,
            "burning_area":       self._burning_area
        }

# ------------------------- PRIVATE METHODS -------------------------

    def _calculate_burning_area(self, burn_distance: float = 0) -> float:
        a0 = -6 * burn_distance**2
        a1 = burn_distance * (2*self._segment_length - 4*self._port_diameter)
        a2 = self._port_diameter + self._segment_length
        a3 = (self._outside_diameter**2 - self._port_diameter**2)/2
        Ab = self._number_of_segments*pi * (a0 + a1 + a2 + a3)
        return Ab


# ------------------------- PUBLIC METHODS -------------------------
    def evaluate(self, time_step: float, inputs: dict = {}) -> dict:
        """ Evaluate the value of outputs but do not integrate (dont increase burn distance) """

        # Check inputs here
        # Initialize values of each input
        # Initialize to None if no reasonable initial value makes sense

        # Initialize to 0 in order to evaluate some outputs
        #  on the first pass of the main simulation loop
        if not "regression_rate" in inputs.keys():
            inputs["regression_rate"] = 0      
        elif not type(inputs["regression_rate"]) in [float, int]:
            raise TypeError(f"Regressiuon rate has to be an float. Regression rate: {inputs["regression_rate"]}")   
        elif inputs["regression_rate"] < 0:
            raise ValueError(f"Regression rate cannot be negative. Regression rate: {inputs["regression_rate"]}")

        burn_distance = self._burn_distance + inputs["regression_rate"]*time_step
        self._burning_area = self._calculate_burning_area(burn_distance)

        self._output_ports["segment_length"]     = self._segment_length
        self._output_ports["port_diameter"]      = self._port_diameter
        self._output_ports["outside_diameter"]   = self._outside_diameter
        self._output_ports["number_of_segments"] = self._number_of_segments
        self._output_ports["segment_spacing"]    = self._segment_spacing
        self._output_ports["burn_distance"]      = self._burn_distance
        self._output_ports["burning_area"]       = self._burning_area

        return self._output_ports

    def advance(self, time_step: float, inputs: dict = {}) -> dict:
        """ Evaluate the value of outputs and integrate (change burn distance) """

        # Initialize to 0 in order to evaluate some outputs
        #  on the first pass of the main simulation loop
        if not "regression_rate" in inputs.keys():
            inputs["regression_rate"] = 0   
        elif not type(inputs["regression_rate"]) in [float, int]:
            raise TypeError(f"Regressiuon rate has to be an float. Regression rate: {inputs["regression_rate"]}")   
        elif inputs["regression_rate"] < 0:
            raise ValueError(f"Regression rate cannot be negative. Regression rate: {inputs["regression_rate"]}")
        
        self._burn_distance += inputs["regression_rate"] * time_step

        # regression rate is set to zero to correctly evaluate burning area inside of evaluate(). 
        # The integrated burn distance is calculated above and should not be overwritten in evaluate()
        inputs["regression_rate"] = 0
        self.evaluate(time_step, inputs) 
         
        return self._output_ports

    def read_port(self, port: str):
        """ return the values of the component's ports """
        if not port in self._output_ports:
            raise ValueError(f"Cannot read from port: {port}. It is not a valid output port for this compoenent!")
        return self._output_ports[port]

# ------------------------- GETTERS AND SETTERS -------------------------