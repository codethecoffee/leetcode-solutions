def plusOne(digits):
    num_digits = len(digits)
    ans = [0]*num_digits
    i = num_digits -1
    
    while i >= 0:
        curr_digit = digits[i]
        if curr_digit < 9:
            ans[i] = curr_digit + 1
            break
        else: # curr_digit == 9
            # "Carry the 1"
            ans[i] = 0
            i -= 1
    
    # EDGE CASE: All of the digits are 9s
    if i < 0:
        return [1] + ans
    
    # If necessary, populate the rest of the numbers
    while i > 0:
        i -= 1
        ans[i] = digits[i]
    
    return ans