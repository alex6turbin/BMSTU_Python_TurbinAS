"""
Вычислитель AST
"""

import math
from ast import ASTNode, NumberNode, BinaryOpNode, UnaryOpNode, FunctionCallNode

class ASTEvaluator:
    """Вычисляет значения AST"""

    def __init__(self):
        self.operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else self._zero_division_error(),
            '^': lambda x, y: x ** y,
        }

        self.functions = {
            'sqrt': lambda x: math.sqrt(x) if x >= 0 else self._negative_sqrt_error(),
        }

    def evaluate(self, node: ASTNode) -> float:
        """Рекурсивно вычисляет значение AST"""
        return node.accept(self)

    def visit_NumberNode(self, node: NumberNode) -> float:
        return node.value

    def visit_BinaryOpNode(self, node: BinaryOpNode) -> float:
        left_val = self.evaluate(node.left)
        right_val = self.evaluate(node.right)

        if node.operator in self.operations:
            return self.operations[node.operator](left_val, right_val)
        else:
            raise ValueError(f"Неизвестный оператор: {node.operator}")

    def visit_UnaryOpNode(self, node: UnaryOpNode) -> float:
        operand_val = self.evaluate(node.operand)

        if node.operator == '-':
            return -operand_val
        else:
            raise ValueError(f"Неизвестный унарный оператор: {node.operator}")

    def visit_FunctionCallNode(self, node: FunctionCallNode) -> float:
        arg_val = self.evaluate(node.argument)

        if node.function_name in self.functions:
            return self.functions[node.function_name](arg_val)
        else:
            raise ValueError(f"Неизвестная функция: {node.function_name}")

    def generic_visit(self, node):
        raise TypeError(f"Неизвестный тип узла: {type(node).__name__}")

    def _zero_division_error(self):
        raise ValueError("Деление на ноль!")

    def _negative_sqrt_error(self):
        raise ValueError("Квадратный корень из отрицательного числа!")

    def evaluate_with_steps(self, node: ASTNode) -> dict:
        """Вычисляет с пошаговым выводом"""
        print("\n🧮 ВЫЧИСЛЕНИЕ:")
        print("-" * 40)

        steps = []

        try:
            result = self.evaluate(node)
            steps.append(f"Результат: {result}")
            print(f"  {steps[-1]}")

            return {
                'success': True,
                'result': result,
                'steps': steps
            }

        except Exception as e:
            steps.append(f"Ошибка: {e}")
            print(f"  {steps[-1]}")

            return {
                'success': False,
                'error': str(e),
                'steps': steps
            }