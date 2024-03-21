def convert_seconds_to_days(seconds: int) -> int:
    """converts seconds to days
    
    :param seconds: total seconds
    :type seconds: int
    :return: days
    """
    return seconds // 60 // 60 // 24