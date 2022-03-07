
def add(arg1, arg2):
    """
    Parameters
    ----------
    arg1 : TYPE
        DESCRIPTION.
    arg2 : TYPE
        DESCRIPTION.

    Returns
    -------
    temp : TYPE
        DESCRIPTION.
    """
    if isinstance(arg1, (int, float)) and isinstance(arg1, (int, float)):
        temp=arg1+arg2
        return temp
    else:
        return None
    
if __name__ == "__main__":

    result=add(23,56)
    print(result)
    
    result=add("abc","def")
    print(result)




