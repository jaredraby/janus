# Janus
# Jared Raby 09/2016
# 
# type.py
# Description:
# Type is the base level class that serves as the program object that will manipulated for the 
# conversion system. The base level calls contains the current and output file formats as well
# as the location of the file for conversion.


class convType():
    
    def __init__(self, current, output):
        self.current = current
        self.output = output

    def toolCall(self, convType):
        """ Calls the given tool for the next 

        Args:
            -Input Format
            -Output Format
            -File - whether location, byte array, or remote location

        Returns:
            -Type of new version

        """
        

