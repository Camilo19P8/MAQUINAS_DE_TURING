"""Ejercicio 4: paridad de un número binario."""

from turing_machine import TuringMachine


def paridad_binaria(bits: str) -> str:
    states = {"even", "odd", "accept"}
    symbols = {"0", "1"}
    transitions = {
        "even": {
            "0": ("even", "0", "R"),
            "1": ("odd", "1", "R"),
            "_": ("accept", "0", "N"),
        },
        "odd": {
            "0": ("odd", "0", "R"),
            "1": ("even", "1", "R"),
            "_": ("accept", "1", "N"),
        },
    }

    tm = TuringMachine(
        states=states,
        symbols=symbols,
        transitions=transitions,
        initial_state="even",
        blank_symbol="_",
        accept_states={"accept"},
    )
    tm.run(bits)
    return tm.tape_contents()


if __name__ == "__main__":
    ejemplo = "1011"
    print(f"Paridad de {ejemplo}: {paridad_binaria(ejemplo)}")
