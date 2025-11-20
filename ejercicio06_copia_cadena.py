"""Ejercicio 6: copia de una cadena sobre {A, B, C} en la misma cinta."""

from turing_machine import TuringMachine


def copiar_cadena(cadena: str) -> str:
    symbols = {"A", "B", "C", "a", "b", "c", "X", "Y", "Z"}
    states = {
        "seek",
        "move_end_A",
        "move_end_B",
        "move_end_C",
        "skip_right_blank",
        "return_home",
        "restore",
        "accept",
    }

    transitions = {
        "seek": {
            "A": ("move_end_A", "a", "R"),
            "B": ("move_end_B", "b", "R"),
            "C": ("move_end_C", "c", "R"),
            "a": ("seek", "a", "R"),
            "b": ("seek", "b", "R"),
            "c": ("seek", "c", "R"),
            "X": ("seek", "X", "R"),
            "Y": ("seek", "Y", "R"),
            "Z": ("seek", "Z", "R"),
            "_": ("restore", "_", "L"),
        },
        "move_end_A": {},
        "move_end_B": {},
        "move_end_C": {},
        "skip_right_blank": {
            "_": ("return_home", "_", "L"),
        },
        "return_home": {},
        "restore": {},
    }

    # Populate move_end states (all behave the same except for the symbol written)
    for state_name, symbol_to_write in [
        ("move_end_A", "X"),
        ("move_end_B", "Y"),
        ("move_end_C", "Z"),
    ]:
        transitions[state_name] = {
            "A": (state_name, "A", "R"),
            "B": (state_name, "B", "R"),
            "C": (state_name, "C", "R"),
            "a": (state_name, "a", "R"),
            "b": (state_name, "b", "R"),
            "c": (state_name, "c", "R"),
            "X": (state_name, "X", "R"),
            "Y": (state_name, "Y", "R"),
            "Z": (state_name, "Z", "R"),
            "_": ("skip_right_blank", symbol_to_write, "R"),
        }

    transitions["return_home"] = {
        "A": ("return_home", "A", "L"),
        "B": ("return_home", "B", "L"),
        "C": ("return_home", "C", "L"),
        "a": ("return_home", "a", "L"),
        "b": ("return_home", "b", "L"),
        "c": ("return_home", "c", "L"),
        "X": ("return_home", "X", "L"),
        "Y": ("return_home", "Y", "L"),
        "Z": ("return_home", "Z", "L"),
        "_": ("seek", "_", "R"),
    }

    transitions["restore"] = {
        "a": ("restore", "A", "L"),
        "b": ("restore", "B", "L"),
        "c": ("restore", "C", "L"),
        "X": ("restore", "A", "L"),
        "Y": ("restore", "B", "L"),
        "Z": ("restore", "C", "L"),
        "A": ("restore", "A", "L"),
        "B": ("restore", "B", "L"),
        "C": ("restore", "C", "L"),
        "_": ("accept", "_", "R"),
    }

    tm = TuringMachine(
        states=states,
        symbols=symbols,
        transitions=transitions,
        initial_state="seek",
        blank_symbol="_",
        accept_states={"accept"},
    )
    tm.run(cadena)
    return tm.tape_contents()


if __name__ == "__main__":
    ejemplo = "AABC"
    print(f"Copia de {ejemplo}: {copiar_cadena(ejemplo)}")
