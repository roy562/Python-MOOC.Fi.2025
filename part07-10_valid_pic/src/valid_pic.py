# Write your solution here
from datetime import datetime


def is_it_valid(pic: str):
    valid_markers = {'+':'18',
                 '-':'19',
                 'A':'20'}
    remainder_codes = '0123456789ABCDEFHJKLMNPRSTUVWXY'

    if len(pic) != 11:
        return False
    
    century_marker = pic[6]
    if century_marker not in valid_markers:
        return False
    
    day = pic[0:2]
    month = pic[2:4]
    year = valid_markers[century_marker]+pic[4:6]
    
    try:
        given_date = datetime(int(year), int(month), int(day))
        #print(given_date)
    except ValueError:
        return False

    control_index = int(pic[0:6]+pic[7:10])%31
    expected_control_char = remainder_codes[control_index]
    #print(expected_control_char)
    if expected_control_char != pic[-1]:
        return False


    return True

#print(is_it_valid("230827-906F"))