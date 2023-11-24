from jwt import encode, decode

def create_token(data: dict):
    token: str = encode(payload = data, key = "U+KTd4E6kUNZnpHrSwEFdKgZz5V0FLC3bHqPWLhlYjs", algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key="U+KTd4E6kUNZnpHrSwEFdKgZz5V0FLC3bHqPWLhlYjs", algorithms=['HS256'])
    return data