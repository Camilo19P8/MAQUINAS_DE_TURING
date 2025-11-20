"""Ejercicio 9: sucesor de un número binario."""

from turing_machine import TuringMachine


def sucesor_binario(bits: str) -> str:
    states = {"seek_blank", "add_carry", "accept"}
    symbols = {"0", "1"}
    transitions = {
        "seek_blank": {
            "0": ("seek_blank", "0", "R"),
            "1": ("seek_blank", "1", "R"),
            "_": ("add_carry", "_", "L"),
        },
        "add_carry": {
            "0": ("accept", "1", "N"),
            "1": ("add_carry", "0", "L"),
            "_": ("accept", "1", "N"),
        },
    }

    tm = TuringMachine(
        states=states,
        symbols=symbols,
        transitions=transitions,
        initial_state="seek_blank",
        blank_symbol="_",
        accept_states={"accept"},
    )
    tm.run(bits)
    return tm.tape_contents()


if __name__ == "__main__":
    ejemplo = "1011"
    print(f"Sucesor binario de {ejemplo}: {sucesor_binario(ejemplo)}")
