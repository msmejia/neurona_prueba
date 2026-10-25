def calcular_error_cuadratico_medio(real, predicho):
    """
    Calcula el error cuadrático medio (MSE).

    Parámetros
    ----------
    real : lista de números
        Valores observados.
    predicho : lista de números
        Valores estimados por el modelo.

    Retorna
    -------
    float
        Error cuadrático medio.
    """
    if len(real) == 0:
        raise ValueError("Los datos no pueden estar vacíos.")

    if len(real) != len(predicho):
        raise ValueError(
            "Las listas deben tener igual longitud."
        )

    errores = [(r - p) ** 2 for r, p in zip(real, predicho)]
    return sum(errores) / len(errores)
