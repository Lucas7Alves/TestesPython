from src.calculadora import Calculadora
from src.operacoes.add import AddOperation
from src.operacoes.sub import SubOperation

calc = Calculadora(AddOperation(), SubOperation())

op1 = calc.add(2, 5, True)
op2 = calc.sub(5, 3, True)

print(op1)
print(op2)