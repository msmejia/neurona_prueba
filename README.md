
# Estadistica Neuronal

Biblioteca de funciones estadísticas y herramientas
para evaluar modelos predictivos.

## Instalación

```bash
pip install estadistica_neuronal
```

## Ejemplo de uso

```python
from estadistica_neuronal import calcular_error_cuadratico_medio

real = [10, 15, 20, 25]
predicho = [11, 14, 19, 26]

mse = calcular_error_cuadratico_medio(real, predicho)

print("Error cuadrático medio:", mse)
```
