__all__ = ['format_bold']

def format_bold(text):
    return f"**{text.upper()}**"

if __name__ == "__main__":
    print(f"Модуль {__name__} запущен напрямую.")
    print("Тест форматирования:", format_bold("hello"))
else:
    print(f"Модуль {__name__} импортирован.")