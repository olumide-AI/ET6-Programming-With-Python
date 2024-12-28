def mystery_6(a, b):
    """ The behaviour of the function. 
     Takes a as the new list(c) length, 
      while b is the initial length for the new list(c)
        """
    if a == 0:
        return []

    c = []
    while len(c) < a:
        c.append(b)
        b = b + 1

    return c
