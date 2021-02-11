def check_real(string):
    try:
        if float(string):
            return float(string)
    except:
        return False