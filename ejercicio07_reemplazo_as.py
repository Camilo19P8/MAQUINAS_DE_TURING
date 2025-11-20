"""Ejercicio 7: reemplazo de las primeras M letras A por B."""

from turing_machine import TuringMachine


def reemplazar_primeras_as(cadena: str, m: int) -> str:
    if m < 0:
        raise ValueError("M debe ser no negativo")

    alphabet = set(cadena) | {"A", "B"}
    states = {f"q{i}" for i in range(m + 1)} | {"accept", "reject"}
    transitions = {}

    for i in range(m):
        state = f"q{i}"
        transitions[state] = {}
        transitions[state]["A"] = (f"q{i + 1}", "B", "R")
        for symbol in alphabet - {"A"}:
            transitions[state][symbol] = (state, symbol, "R")
        transitions[state]["_"] = ("reject", "_", "N")

    final_state = f"q{m}"
    transitions[final_state] = {}
    for symbol in alphabet:
        transitions[final_state][symbol] = (final_state, symbol, "R")
    transitions[final_state]["_"] = ("accept", "_", "N")

    tm = TuringMachine(
        states=states,
        symbols=alphabet,
        transitions=transitions,
        initial_state="q0",
        blank_symbol="_",
        accept_states={"accept"},
        reject_states={"reject"},
    )
    result = tm.run(cadena)
    if result.status != "accept":
        raise ValueError("La entrada no contiene suficientes letras A")
    return tm.tape_contents()


if __name__ == "__main__":
    ejemplo = "11AAAAB"
    print(f"Reemplazo con M=2: {reemplazar_primeras_as(ejemplo, 2)}")
