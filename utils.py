import datetime


def time_to_datetime(time):
    """ Converts a string into a date time object.

    :param time: The time as a string to be converted into the date time object.
    :raises ValueError: If time cant be converted into a date time object due to the format not being YYYY/MM/DD HH:MM.
    :return: the date time object.
    """
    date_format = "%Y/%m/%d %H:%M"
    try:
        date_obj = datetime.datetime.strptime(time, date_format)
    except ValueError:
        raise ValueError("The time must have the format YYYY/MM/DD HH:MM")
    return date_obj


def load_prev_plan_spec(path):
    """ Loads the details of a planned journey from a file.

    :param path: the filepath of the file containing the details of the journey.
    :return: a tuple of three strings containing start location, end location and arrival time.
    """
    from_ = None
    to = None
    arrive_at = None
    try:
        f = open(path, "r")
        from_ = f.readline().rstrip('\n')
        to = f.readline().rstrip('\n')
        try:
            arrive_at = f.readline().rstrip('\n')
            date_obj = datetime.datetime.strptime(arrive_at, "%Y/%m/%d %H:%M")
        except ValueError:
            from_ = None
            to = None
            arrive_at = None
        if from_ == "" or to == "" or arrive_at == "":
            from_ = None
            to = None
            arrive_at = None
    except FileNotFoundError:
        pass
    return from_, to, arrive_at

