from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Tuple

Direction = str  # Valores esperados: "L", "R" o "N"
Transition = Tuple[str, str, Direction]
TransitionTable = Dict[str, Dict[str, Transition]]


@dataclass
class HaltResult:
    """Pequeña ayuda para describir cómo/cuándo se detuvo la máquina."""

    status: str  # "accept", "reject" or "halt"
    steps: int
    reason: str


class TuringMachine:
    """
    Simulador sencillo de una Máquina de Turing determinista de una sola cinta.

    La tabla de transición es un diccionario de dos niveles:
    transitions[estado_actual][símbolo_leído] = (siguiente_estado, símbolo_a_escribir, dirección)
    donde la dirección es una de L, R o N.
    """

    def __init__(
        self,
        states: Iterable[str],
        symbols: Iterable[str],
        transitions: TransitionTable,
        initial_state: str,
        blank_symbol: str = "_",
        accept_states: Optional[Iterable[str]] = None,
        reject_states: Optional[Iterable[str]] = None,
    ) -> None:
        if len(blank_symbol) != 1:
            raise ValueError("Blank symbol must be a single character")
        self.states = set(states)
        self.symbols = set(symbols) | {blank_symbol}
        self.transitions = transitions
        self.initial_state = initial_state
        self.blank_symbol = blank_symbol
        self.accept_states = set(accept_states or [])
        self.reject_states = set(reject_states or [])

        self.tape: List[str] = []
        self.head: int = 0
        self.state: str = initial_state
        self.steps: int = 0
        self.halted: bool = False
        self.halt_reason: Optional[str] = None
        self.reset("")

    def reset(self, tape_input: str) -> None:
        """Reinicia la máquina a la configuración inicial con una nueva entrada."""
        if any(len(ch) != 1 for ch in tape_input):
            raise ValueError("Only single-character symbols are supported on the tape")
        self.tape = list(tape_input) if tape_input else [self.blank_symbol]
        self.head = 0
        self.state = self.initial_state
        self.steps = 0
        self.halted = False
        self.halt_reason = None

    def _read_symbol(self) -> str:
        if self.head < 0:
            self.tape.insert(0, self.blank_symbol)
            self.head = 0
        elif self.head >= len(self.tape):
            self.tape.append(self.blank_symbol)
        return self.tape[self.head]

    def _write_symbol(self, symbol: str) -> None:
        if len(symbol) != 1:
            raise ValueError("Only single-character symbols are supported on the tape")
        self.tape[self.head] = symbol

    def step(self) -> Optional[HaltResult]:
        """
        Ejecuta una transición. Devuelve un HaltResult cuando la máquina se detiene; de lo contrario None.
        """
        if self.halted:
            return HaltResult(self.halt_reason or "halt", self.steps, "already halted")

        symbol = self._read_symbol()
        state_transitions = self.transitions.get(self.state, {})
        transition = state_transitions.get(symbol)
        if not transition:
            self.halted = True
            self.halt_reason = "halt"
            return HaltResult("halt", self.steps, f"No transition for ({self.state}, {symbol})")

        next_state, write_symbol, direction = transition
        self._write_symbol(write_symbol)

        if direction == "R":
            self.head += 1
        elif direction == "L":
            self.head -= 1
        elif direction != "N":
            raise ValueError(f"Unknown direction: {direction}")

        self.state = next_state
        self.steps += 1

        if self.state in self.accept_states:
            self.halted = True
            self.halt_reason = "accept"
            return HaltResult("accept", self.steps, "Reached accept state")

        if self.state in self.reject_states:
            self.halted = True
            self.halt_reason = "reject"
            return HaltResult("reject", self.steps, "Reached reject state")

        return None

    def run(self, tape_input: Optional[str] = None, max_steps: int = 10_000) -> HaltResult:
        """
        Ejecuta la máquina hasta que se detenga o se exceda max_steps.

        Si `tape_input` no es None, la máquina se reinicia con esa entrada antes de correr.
        """
        if tape_input is not None:
            self.reset(tape_input)

        for _ in range(max_steps):
            result = self.step()
            if result:
                return result

        self.halted = True
        self.halt_reason = "halt"
        return HaltResult("halt", self.steps, f"Exceeded max steps ({max_steps})")

    def tape_contents(self, trim: bool = True) -> str:
        """Devuelve el contenido actual de la cinta."""
        contents = "".join(self.tape)
        if trim:
            return contents.strip(self.blank_symbol)
        return contents

    def snapshot(self) -> str:
        """Devuelve una descripción legible de la configuración actual."""
        tape = self.tape.copy()
        if 0 <= self.head < len(tape):
            tape[self.head] = f"[{tape[self.head]}]"
        else:
            tape.append(f"[{self.blank_symbol}]")
        return f"state={self.state}, head={self.head}, tape={''.join(tape)}"
