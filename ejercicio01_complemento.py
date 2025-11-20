"""Ejercicio 1: complemento de un número binario."""

from turing_machine import TuringMachine


def complemento_binario(bits: str) -> str:
    states = {"scan", "accept"}
    symbols = {"0", "1"}
    transitions = {
        "scan": {
            "0": ("scan", "1", "R"),
            "1": ("scan", "0", "R"),
            "_": ("accept", "_", "N"),
        }
    }

    tm = TuringMachine(
        states=states,
        symbols=symbols,
        transitions=transitions,
        initial_state="scan",
        blank_symbol="_",
        accept_states={"accept"},
    )
    tm.run(bits)
    return tm.tape_contents()


if __name__ == "__main__":
    ejemplo = "10101"
    print(f"Complemento de {ejemplo}: {complemento_binario(ejemplo)}")
