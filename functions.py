import error

def errorcount(original, user_data):
    """Returns the count of error occured while typing"""
    err_no = 0
    for i in range(len(original)):
        try:
            if original[i] != user_data[i]:
                raise error.NotSameError
        except:
            err_no += 1
    return err_no

def typing_time(start_t, end_t):
    """Returns the time to type in secinds"""
    taken_t = end_t - start_t
    return taken_t

def speed(start_t, end_t, user_data):
    """Returns the speed of typing in form of word per second"""
    Time = typing_time(start_t, end_t)
    spd = len(user_data)/Time
    return spd

def select(level):
    """Returns the target statement to be printed"""
    import data
    import random
    target = random.choice(level)
    return target
