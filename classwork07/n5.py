def filt(x):
        if 'sus' in x == 0:
            return True
        else:
            return False

    lis = filter(filt, generator)
    return lis