from src.operacoes.add import AddOperation
from faker import Faker

fake = Faker()

def test_some():
    addOperation = AddOperation()
    number1 = fake.random_number()
    number2 = fake.random_number()
    
    expect = number1 + number2

    test_some()

    result = addOperation.soma(number1, number2)


    assert result == number1 + number2
