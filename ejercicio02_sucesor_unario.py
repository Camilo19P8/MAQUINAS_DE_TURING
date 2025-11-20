"""Ejercicio 2: sucesor en codificación unaria."""

from turing_machine import TuringMachine


def sucesor_unario(entrada: str) -> str:
    states = {"scan", "accept"}
    symbols = {"1"}
    transitions = {
        "scan": {
            "1": ("scan", "1", "R"),
            "_": ("accept", "1", "N"),
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
    tm.run(entrada or "_")
    return tm.tape_contents()


if __name__ == "__main__":
    ejemplo = "111"
    print(f"Sucesor unario de {ejemplo}: {sucesor_unario(ejemplo)}")
