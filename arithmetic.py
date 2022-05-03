import re
import math
def arithmetic_operations(user_input):
    try:
        return str(eval(user_input))
    except:
        return None
