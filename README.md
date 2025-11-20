# Taller de Máquinas de Turing

Este proyecto implementa una clase `TuringMachine` reutilizable y diez ejercicios clásicos de simulación. Cada ejercicio define su propia tabla de transición y reutiliza la clase base para ejecutar la lógica solicitada en el taller.

## Requisitos

- Python 3.10 o superior.
- No se necesitan dependencias externas; todo se apoya en la biblioteca estándar.

## Instalación rápida

1. (Opcional) Crear y activar un entorno virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Clonar o descargar el directorio `taller_maquinas_turing` en tu máquina local.

## Estructura principal

- `turing_machine.py`: implementación completa de la clase `TuringMachine` y el contenedor `HaltResult`.
- `ejercicio01_complemento.py` … `ejercicio10_antecesor_binario.py`: scripts independientes para cada ejercicio solicitado.
- `__init__.py`: facilita el uso como paquete, reexportando todas las funciones.

## Funcionamiento de `TuringMachine`

1. **Definición**: cada ejercicio especifica el conjunto de estados, alfabeto, tabla de transición (diccionario de dos niveles), estado inicial, símbolo blanco y estados de aceptación/rechazo.
2. **Ejecución**:
   - `step()` simula una transición: lee el símbolo bajo el cabezal, consulta la tabla, escribe el nuevo símbolo y mueve el cabezal.
   - `run()` repite pasos hasta detenerse (aceptar, rechazar o no encontrar transición). Se puede reiniciar con una nueva entrada mediante el parámetro `tape_input`.
3. **Inspección**: `tape_contents()` devuelve el contenido actual de la cinta y `snapshot()` ofrece un resumen legible del estado.

## Cómo ejecutar los ejercicios

Cada módulo es ejecutable directamente. Por ejemplo, para el complemento binario:

```bash
python ejercicio01_complemento.py
```

Todos los archivos incluyen un bloque `if __name__ == "__main__":` con un ejemplo, por lo que basta ejecutar el script correspondiente (`ejercicio0X_*.py`). Las funciones también pueden importarse desde otros programas:

```python
from ejercicio09_sucesor_binario import sucesor_binario
print(sucesor_binario("1011"))  # -> 1100
```

## Validación rápida

Puedes verificar los diez ejercicios de una sola vez con un pequeño script:

```bash
python - <<'PY'
from ejercicio01_complemento import complemento_binario
from ejercicio02_sucesor_unario import sucesor_unario
from ejercicio03_predecesor_unario import predecesor_unario
from ejercicio04_paridad_binaria import paridad_binaria
from ejercicio05_contador_unario import contar_caracteres
from ejercicio06_copia_cadena import copiar_cadena
from ejercicio07_reemplazo_as import reemplazar_primeras_as
from ejercicio08_comparacion_palabras import comparar_palabras
from ejercicio09_sucesor_binario import sucesor_binario
from ejercicio10_antecesor_binario import antecesor_binario

print("1", complemento_binario("10101"))
print("2", sucesor_unario("111"))
print("3", predecesor_unario("1111"))
print("4", paridad_binaria("1011"))
print("5", contar_caracteres("abca"))
print("6", copiar_cadena("AABC"))
print("7", reemplazar_primeras_as("11AAAAB", 2))
print("8a", comparar_palabras("101#101"))
print("8b", comparar_palabras("110#101"))
print("9", sucesor_binario("1011"))
print("10", antecesor_binario("1100"))
PY
```

Cada línea muestra el resultado esperado de acuerdo con el enunciado del taller. Ajusta las entradas según las pruebas que quieras realizar.E***
