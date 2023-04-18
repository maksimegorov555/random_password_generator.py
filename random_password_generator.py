import random
import string

def generate_password(length):
    """Генерирует случайный пароль заданной длины."""
    # Символы, которые будут использоваться в пароле.
    chars = string.ascii_letters + string.digits

    # Генерируем пароль из случайных символов.
    password = ''.join(random.choice(chars) for _ in range(length))

    return password

length = int(input("Введите длину пароля: "))
password = generate_password(length)
print("Сгенерированный пароль:", password)
