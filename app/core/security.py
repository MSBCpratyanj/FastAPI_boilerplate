# app/core/security.py

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ───── Password Hashing ─────
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed one."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a password for storing."""
    return pwd_context.hash(password)

