import re
from datetime import datetime

def generate_id(prefix: str, counter=[0]) -> str:
    """ Genereer unieke ID met prefix (bijv. 'M001', 'B001') """
    counter[0] += 1
    return f"{prefix}{counter[0]:03d}"
  
def validate_email(email: str) -> bool:
    """ Valideer email formaat (verbeterde versie) """
    pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
    return bool(pattern.match(email.strip()))
  
def format_date(date_string: str) -> str | None:
    """ Format datum naar ISO YYYY-MM-DD """
    if not date_string or not isinstance(date_string, str):
        return None
    s = date_string.strip()
    common_formats = [
        "%Y-%m-%d", "%d-%m-%Y", "%m-%d-%Y",
        "%Y/%m/%d", "%d/%m/%Y", "%m/%d/%Y",
        "%d.%m.%Y", "%Y.%m.%d", "%m.%d.%Y"
        ]
    for fmt in common_formats:
        try:
            dt = datetime.strptime(s, fmt)
            return dt
        except:
            continue
    return None
  
def calculate_days_between(date1: str, date2: str) -> int:
    """Bereken dagen tussen twee datums (strings in YYYY-MM-DD)"""
    d_one = format_date(date1)
    d_two = format_date(date2)
    if d_one >= d_two:
        return (d_one - d_two).days
    else:
        return (d_two - d_one).days
  
def validate_isbn(isbn: str) -> bool:
    """Check of ISBN geldig formaat heeft"""
    pattern = re.compile(r"^(?=(?:[^0-9]*[0-9]){10}(?:(?:[^0-9]*[0-9]){3})?$)[\d-]+$")
    return bool(pattern.match(isbn.strip()))

if __name__ == "__main__":
    print(f"Generated ID: {generate_id('M')}")
    print(f"Generated ID: {generate_id('M')}")
    print(f"Generated ID: {generate_id('B')}")
    print(f"Valid email: {validate_email('test@email.com')}")
    print(f"Invalid email: {validate_email('invalid-email')}")
    print(f"Days between: {calculate_days_between('2025-01-01', '2025-01-15')}")
    print(f"Valid ISBN: {validate_isbn('978-1234567890')}")