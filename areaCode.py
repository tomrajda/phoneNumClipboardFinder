def areaCode(code=48):
    """
    Returns user's country area code
    """
    
    areaCode = code
    
    message = "Please, enter your country area code (default = 48)"
    message += "\nIf you dont want to change country area code, type ENTER: "
    try: 
        userCode = int(input(message))
        if userCode != 48:
            areaCode = userCode
    except ValueError:
        print("\nThanks, it seems you're from Poland.\n")

    return f'+{areaCode}'
