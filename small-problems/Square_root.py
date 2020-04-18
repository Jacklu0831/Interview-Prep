def sqrt(n):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    left = 0
    right = n

    while left <= right:
    	middle = (left + right) // 2
    	floor_pred = middle ** 2
    	ceiling_pred = (middle + 1) ** 2

    	if floor_pred <= n < ceiling_pred:
    		return int(middle)
    	elif n >= ceiling_pred:
    		left = middle + 1
    	else:
    		right = middle - 1
    
    return None

print ("Pass" if (3 == sqrt(9)) else "Fail")
print ("Pass" if (0 == sqrt(0)) else "Fail")
print ("Pass" if (4 == sqrt(16)) else "Fail")
print ("Pass" if (1 == sqrt(1)) else "Fail")