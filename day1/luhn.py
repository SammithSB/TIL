def luhn(number):
    sum = 0
    card_number = str(number)
    is__num_len_even = len(card_number)%2==0
    for i, digit in enumerate(card_number):
        digit = int(digit)
        # this is because we are enummerating from first digit from left
        # and if length is even then when we start from the rightmost digit
        # we end the first digit from left, if len is off we end up at the 
        # second digit from left.
        if(i%2==(0 if is__num_len_even else 1)):
            digit*=2
            if digit>9:
                digit-=9
        sum+=digit
    return sum%10==0
print(luhn(374245455400126))