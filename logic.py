# Konstantes
KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172

def convert(value, conversion_type):
    """Veic aprēķinu balstoties uz izvēlēto tipu"""
    if conversion_type == "km → mi":
        return value * KM_TO_MI
    elif conversion_type == "mi → km":
        return value / KM_TO_MI
    elif conversion_type == "kg → lb":
        return value * KG_TO_LB
    elif conversion_type == "lb → kg":
        return value / KG_TO_LB
    elif conversion_type == "L → gal":
        return value * L_TO_GAL
    elif conversion_type == "gal → L":
        return value / L_TO_GAL
    return 0.0