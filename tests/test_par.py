from funciones.funcion_par import funcion_par

def test_par():
    assert funcion_par(4) == True


def test_impar():
    assert funcion_par(5) == False