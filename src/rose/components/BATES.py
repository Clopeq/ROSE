

class BATES:
# ------------------------- PRIVATE ATTRIBUTES -------------------------
    _L  = None  # mm, Length of the grain segment
    _OD = None  # mm, Outside diameter of grain segment
    _ID = None  # mm, Inside diameter of grain segment
    _N  = None  #     Number of grain segments
    _h  = 0     # mm, Spacing inbetween grain segments, defaults to 0 mm

    def __init__(self,
            segment_length:     float, 
            outside_diamter:    float, 
            port_diameter:      float, 
            number_of_segments: float = 1, 
            segment_spacing:    float = 0
        ):
        """ Constructor
        """

        # TODO: Check inputs here

        self._L  = segment_length
        self._OD = outside_diamter
        self._ID = port_diameter
        self._N  = number_of_segments
        self._h  = segment_spacing


# ------------------------- PUBLIC METHODS -------------------------
    def evaluate(self):
        pass

    def integrate(self):
        pass


# ------------------------- GETTERS AND SETTERS -------------------------
    @property
    def L(self):
        return self._L

    @property
    def OD(self):
        return self._OD

    @property
    def ID(self):
        return self._ID

    @property
    def N(self):
        return self._N

    @property
    def h(self):
        return self._h