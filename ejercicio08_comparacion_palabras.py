"""Ejercicio 8: comparación de dos palabras separadas por #."""

from turing_machine import TuringMachine


def comparar_palabras(entrada: str) -> bool:
    symbols = {"0", "1", "#", "x", "y"}
    states = {
        "scan_left",
        "seek_right_0",
        "seek_right_1",
        "match_right_0",
        "match_right_1",
        "return_left",
        "check_right_done",
        "accept",
        "reject",
    }

    transitions = {
        "scan_left": {
            "0": ("seek_right_0", "x", "R"),
            "1": ("seek_right_1", "y", "R"),
            "x": ("scan_left", "x", "R"),
            "y": ("scan_left", "y", "R"),
            "#": ("check_right_done", "#", "R"),
            "_": ("reject", "_", "N"),
        },
        "seek_right_0": {
            "0": ("seek_right_0", "0", "R"),
            "1": ("seek_right_0", "1", "R"),
            "x": ("seek_right_0", "x", "R"),
            "y": ("seek_right_0", "y", "R"),
            "#": ("match_right_0", "#", "R"),
            "_": ("reject", "_", "N"),
        },
        "seek_right_1": {
            "0": ("seek_right_1", "0", "R"),
            "1": ("seek_right_1", "1", "R"),
            "x": ("seek_right_1", "x", "R"),
            "y": ("seek_right_1", "y", "R"),
            "#": ("match_right_1", "#", "R"),
            "_": ("reject", "_", "N"),
        },
        "match_right_0": {
            "x": ("match_right_0", "x", "R"),
            "y": ("match_right_0", "y", "R"),
            "0": ("return_left", "x", "L"),
            "1": ("reject", "1", "N"),
            "_": ("reject", "_", "N"),
        },
        "match_right_1": {
            "x": ("match_right_1", "x", "R"),
            "y": ("match_right_1", "y", "R"),
            "1": ("return_left", "y", "L"),
            "0": ("reject", "0", "N"),
            "_": ("reject", "_", "N"),
        },
        "return_left": {
            "0": ("return_left", "0", "L"),
            "1": ("return_left", "1", "L"),
            "x": ("return_left", "x", "L"),
            "y": ("return_left", "y", "L"),
            "#": ("return_left", "#", "L"),
            "_": ("scan_left", "_", "R"),
        },
        "check_right_done": {
            "x": ("check_right_done", "x", "R"),
            "y": ("check_right_done", "y", "R"),
            "_": ("accept", "_", "N"),
            "0": ("reject", "0", "N"),
            "1": ("reject", "1", "N"),
        },
    }

    tm = TuringMachine(
        states=states,
        symbols=symbols,
        transitions=transitions,
        initial_state="scan_left",
        blank_symbol="_",
        accept_states={"accept"},
        reject_states={"reject"},
    )
    result = tm.run(entrada)
    return result.status == "accept"


if __name__ == "__main__":
    ejemplos = ["101#101", "110#101"]
    for palabra in ejemplos:
        print(f"{palabra} -> {'Iguales' if comparar_palabras(palabra) else 'Distintas'}")
