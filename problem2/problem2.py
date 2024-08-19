def date_format(date_str: str) -> str:
    """
    Convert a date from MM/DD/YYYY format to YYYY-MM-DD format.

    Parameters:
    date_str (str): The date string in MM/DD/YYYY format

    Returns:
    str: The date string in YYYY-MM-DD format
    """
    # Split the input string into parts
    month, day, year = date_str.split('/')
    # Return the formatted date string
    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
