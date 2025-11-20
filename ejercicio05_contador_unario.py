"""Ejercicio 5: contador unario para cadenas sobre {a, b, c}."""

from turing_machine import TuringMachine


def contar_caracteres(cadena: str) -> str:
    states = {"count", "accept"}
    symbols = {"a", "b", "c", "1"}
    transitions = {
        "count": {
            "a": ("count", "1", "R"),
            "b": ("count", "1", "R"),
            "c": ("count", "1", "R"),
            "1": ("count", "1", "R"),
            "_": ("accept", "_", "N"),
        }
    }

    tm = TuringMachine(
        states=states,
        symbols=symbols,
        transitions=transitions,
        initial_state="count",
        blank_symbol="_",
        accept_states={"accept"},
    )
    tm.run(cadena)
    return tm.tape_contents()


if __name__ == "__main__":
    ejemplo = "abca"
    print(f"Contador unario para {ejemplo}: {contar_caracteres(ejemplo)}")
