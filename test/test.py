import sys
sys.path.insert(1, '/home/borja/Desktop/tfg/pruebas/8.UnitTesting')
from src.complejo import Complejo


C1 = Complejo(3, 2); C2 = Complejo(5, 6)


def testGetParteEntera():

    assert C1.getParteEntera() == 3


def testGetParteImaginaria():

    assert C1.getParteImaginaria() == 2


def testSum():

    suma = C1 + C2
    assert suma.getParteEntera() == 8 and suma.getParteImaginaria() == 8


def testMul():

    multiplicacion = C1 * C2
    assert multiplicacion.getParteEntera() == 3 and multiplicacion.getParteImaginaria() == 28