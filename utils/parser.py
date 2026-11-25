import re
import math


_CALL_PATTERN = re.compile(
    r"CALL_FUNCTION:([A-Za-z_]\w*):"
    r"([A-Za-z_]\w*=[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
    r"(?:,[A-Za-z_]\w*=[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)*)"
)

def parse_function_call(text):
    """
    Parse function call from text in format: CALL_FUNCTION:function_name:param1=value1,param2=value2
    
    Args:
        text (str): Text that may contain a function call
        
    Returns:
        tuple: (function_name, parameters) or (None, None) if no function call found
    """
    if not isinstance(text, str):
        return None, None

    match = _CALL_PATTERN.fullmatch(text.strip())
    if match is None:
        return None, None

    function_name, parameter_text = match.groups()
    parameters = {}
    for parameter in parameter_text.split(","):
        name, value = parameter.split("=", 1)
        if name in parameters:
            return None, None
        number = float(value)
        if not math.isfinite(number):
            return None, None
        parameters[name] = number

    return function_name, parameters
