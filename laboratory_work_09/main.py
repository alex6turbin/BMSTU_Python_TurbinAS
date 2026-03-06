"""
Главная программа с двумя режимами:
1. Ввод словами (два плюс три)
2. Ввод символами (2 + 3)
"""

import sys
from lexer import TextLexer, MathLexer
from parser import TextParser, MathParser
from ast import ASTVisualizer
from evaluator import ASTEvaluator
from dictionary import MathDictionary

def print_header():
    """Печатает заголовок"""
    print("="*70)
    print("ИНТЕРПРЕТАТОР С ДВУМЯ РЕЖИМАМИ")
    print("="*70)
    print("\nРЕЖИМ 1: ВВОД СЛОВАМИ")
    print("  Пример: 'два плюс три умножить четыре'")
    print("  Поддерживаются: плюс, минус, умножить, разделить, корень")
    print("  Числа словами: от 'ноль' до 'двадцать'")

    print("\nРЕЖИМ 2: ВВОД СИМВОЛАМИ")
    print("  Пример: '2 + 3 * 4' или 'sqrt(9) + 5'")
    print("  Поддерживаются: + - * / ** sqrt()")
    print("  Числа: любые (12, 3.14, -5)")
    print("="*70)

def process_text_input(text: str):
    """Обрабатывает ввод словами"""
    print(f"\nРЕЖИМ СЛОВ: '{text}'")
    print("="*70)

    try:
        # 1. Лексический анализ
        print("\nЛЕКСИЧЕСКИЙ АНАЛИЗ (слова → токены):")
        lexer = TextLexer(text)
        tokens = lexer.tokenize()
        lexer.pretty_print(tokens)

        # Проверяем на нераспознанные слова
        unknown_words = [t for t in tokens if t.type.name == 'WORD']
        if unknown_words:
            print(f"\nНе распознаны: {[t.value for t in unknown_words]}")

        # 2. Парсинг
        print("\nСИНТАКСИЧЕСКИЙ АНАЛИЗ (токены → AST):")
        parser = TextParser(tokens)
        ast = parser.parse()

        # 3. Визуализация AST
        visualizer = ASTVisualizer()
        visualizer.print_ast(ast, "AST ИЗ ТЕКСТА")

        # 4. Вычисление
        evaluator = ASTEvaluator()
        result = evaluator.evaluate_with_steps(ast)

        # 5. Показываем математическую форму
        print(f"\nМАТЕМАТИЧЕСКАЯ ФОРМА: {text_to_math(text)}")

        return result

    except Exception as e:
        print(f"\nОШИБКА: {e}")
        return {'success': False, 'error': str(e)}

def process_math_input(expression: str):
    """Обрабатывает ввод символами"""
    print(f"\nРЕЖИМ СИМВОЛОВ: '{expression}'")
    print("="*70)

    try:
        # 1. Лексический анализ
        print("\nЛЕКСИЧЕСКИЙ АНАЛИЗ (символы → токены):")
        lexer = MathLexer(expression)
        tokens = lexer.tokenize()
        lexer.pretty_print(tokens)

        # 2. Парсинг
        print("\nСИНТАКСИЧЕСКИЙ АНАЛИЗ (токены → AST):")
        parser = MathParser(tokens)
        ast = parser.parse()

        # 3. Визуализация AST
        visualizer = ASTVisualizer()
        visualizer.print_ast(ast, "AST ИЗ МАТЕМАТИКИ")

        # 4. Вычисление
        evaluator = ASTEvaluator()
        result = evaluator.evaluate_with_steps(ast)

        # 5. Показываем текстовую форму
        print(f"\nТЕКСТОВАЯ ФОРМА: {math_to_text(expression)}")

        return result

    except Exception as e:
        print(f"\nОШИБКА: {e}")
        return {'success': False, 'error': str(e)}

def text_to_math(text: str) -> str:
    """Преобразует текст в математическую форму"""
    from dictionary import MathDictionary
    dict = MathDictionary

    normalized = dict.normalize_text(text)
    words = normalized.split()

    symbols = []
    for word in words:
        symbol = dict.word_to_symbol(word)
        symbols.append(symbol)

    # Собираем выражение
    result = ' '.join(symbols)

    # Улучшаем форматирование
    result = result.replace('** 2', '^')  # Для красоты
    result = result.replace('sqrt', '√')

    return result

def math_to_text(expression: str) -> str:
    """Преобразует математику в текстовую форму (упрощенно)"""
    # Простые замены
    result = expression

    replacements = {
        '+': ' плюс ',
        '-': ' минус ',
        '*': ' умножить ',
        '/': ' разделить ',
        '^': ' в степени ',
        'sqrt': 'корень из ',
        '(': '',
        ')': '',
    }

    for old, new in replacements.items():
        result = result.replace(old, new)

    # Убираем лишние пробелы
    result = ' '.join(result.split())

    return result

    print("\nРЕЖИМ СЛОВ (ввод → математика → результат):")
    for text, math, result in examples:
        print(f"  '{text}' → '{text_to_math(text)}' = {result}")

    print("\nРЕЖИМ СИМВОЛОВ (ввод → текст → результат):")
    for text, math, result in examples:
        print(f"  '{math}' → '{math_to_text(math)}' = {result}")

    print("\n" + "="*70)

def interactive_text_mode():
    """Интерактивный режим для ввода словами"""
    print("\n" + "="*70)
    print("💬 ИНТЕРАКТИВНЫЙ РЕЖИМ: ВВОД СЛОВАМИ")
    print("="*70)
    print("Вводите выражения словами, 'выход' для выхода")
    print("Пример: 'два плюс три умножить корень четыре'")
    print("="*70)

    while True:
        try:
            text = input("\nВведите словами: ").strip()

            if text.lower() in ['выход', 'exit', 'quit', 'q']:
                print("Выход из режима слов")
                break

            if not text:
                continue

            result = process_text_input(text)

            if result['success']:
                print(f"\nИтог: {result['result']}")
            else:
                print(f"\nНе удалось вычислить")

        except KeyboardInterrupt:
            print("\n\n👋 Выход из программы")
            sys.exit(0)
        except Exception as e:
            print(f"\n⚠️  Ошибка: {e}")

def interactive_math_mode():
    """Интерактивный режим для ввода символами"""
    print("\n" + "="*70)
    print("ИНТЕРАКТИВНЫЙ РЕЖИМ: ВВОД СИМВОЛАМИ")
    print("="*70)
    print("Вводите математические выражения, 'выход' для выхода")
    print("Пример: '2 + 3 * sqrt(4)' или '(1+2)*3'")
    print("="*70)

    while True:
        try:
            expression = input("\nВведите символами: ").strip()

            if expression.lower() in ['выход', 'exit', 'quit', 'q']:
                print("👋 Выход из режима символов")
                break

            if not expression:
                continue

            result = process_math_input(expression)

            if result['success']:
                print(f"\nИтог: {result['result']}")
            else:
                print(f"\nНе удалось вычислить")

        except KeyboardInterrupt:
            print("\n\nВыход из программы")
            sys.exit(0)
        except Exception as e:
            print(f"\nОшибка: {e}")

def main():
    """Главная функция"""
    print_header()

    while True:
        print("\n" + "="*70)
        print("ГЛАВНОЕ МЕНЮ")
        print("="*70)
        print("1. Режим слов (ввод словами)")
        print("2. Режим символов (ввод математикой)")
        print("0. Выход")
        print("="*70)

        choice = input("\nВыберите режим (0-2): ").strip()

        if choice == '0':
            print("\nДо свидания!")
            break

        elif choice == '1':
            interactive_text_mode()

        elif choice == '2':
            interactive_math_mode()

        else:
            print("Неверный выбор")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nПрограмма завершена")
    except Exception as e:
        print(f"\nКритическая ошибка: {e}")