"""Ejercicio 3: predecesor en codificación unaria."""

from turing_machine import TuringMachine


def predecesor_unario(entrada: str) -> str:
    states = {"scan", "back", "accept", "reject"}
    symbols = {"1"}
    transitions = {
        "scan": {
            "1": ("scan", "1", "R"),
            "_": ("back", "_", "L"),
        },
        "back": {
            "1": ("accept", "_", "N"),
            "_": ("reject", "_", "N"),
        },
    }

    tm = TuringMachine(
        states=states,
        symbols=symbols,
        transitions=transitions,
        initial_state="scan",
        blank_symbol="_",
        accept_states={"accept"},
        reject_states={"reject"},
    )
    result = tm.run(entrada or "_")
    if result.status != "accept":
        raise ValueError("No existe predecesor para la entrada proporcionada")
    return tm.tape_contents()


if __name__ == "__main__":
    ejemplo = "1111"
    print(f"Predecesor unario de {ejemplo}: {predecesor_unario(ejemplo)}")
