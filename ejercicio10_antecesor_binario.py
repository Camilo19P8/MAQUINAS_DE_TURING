"""Ejercicio 10: antecesor de un número binario."""

from turing_machine import TuringMachine


def antecesor_binario(bits: str) -> str:
    states = {"seek_blank", "subtract", "accept", "reject"}
    symbols = {"0", "1"}
    transitions = {
        "seek_blank": {
            "0": ("seek_blank", "0", "R"),
            "1": ("seek_blank", "1", "R"),
            "_": ("subtract", "_", "L"),
        },
        "subtract": {
            "1": ("accept", "0", "N"),
            "0": ("subtract", "1", "L"),
            "_": ("reject", "_", "N"),
        },
    }

    tm = TuringMachine(
        states=states,
        symbols=symbols,
        transitions=transitions,
        initial_state="seek_blank",
        blank_symbol="_",
        accept_states={"accept"},
        reject_states={"reject"},
    )
    resultado_final = tm.run(bits)
    if resultado_final.status != "accept":
        raise ValueError("No existe antecesor para el número binario dado")
    resultado = tm.tape_contents()
    return resultado.lstrip("0") or "0"


if __name__ == "__main__":
    ejemplo = "1100"
    print(f"Antecesor binario de {ejemplo}: {antecesor_binario(ejemplo)}")
