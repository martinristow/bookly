from passlib.context import CryptContext

passwd_context = CryptContext(
    schemes=["bcrypt"]
)


def generate_passwd_hash(password: str) -> str:
    password_hash = passwd_context.hash(password)

    return password_hash


def verify_password(password_plain: str, hash_pass: str) -> bool:
    return passwd_context.verify(password_plain, hash_pass)
