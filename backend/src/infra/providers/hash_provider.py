from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_hash(password: str) -> str:
    return password_context.hash(password)


def verify_hash(password: str, password_hash) -> bool:
    return password_context.verify(password, password_hash)
