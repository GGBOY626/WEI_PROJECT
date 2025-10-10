"""OOP Tic-Tac-Toe: readability, maintainability, refactoring friendly."""

from __future__ import annotations
from typing import List, Optional, Tuple


class Board:
    """3x3 tic-tac-toe board with winner detection."""

    def __init__(self) -> None:
        self._grid: List[List[str]] = [[" " for _ in range(3)] for _ in range(3)]

    def display(self) -> None:
        """Print the board."""
        for r in range(3):
            print(" | ".join(self._grid[r]))
            if r < 2:
                print("--+---+--")

    def place(self, row: int, col: int, mark: str) -> bool:
        """Place a mark if the cell is empty. Return True if placed."""
        if 0 <= row < 3 and 0 <= col < 3 and self._grid[row][col] == " ":
            self._grid[row][col] = mark
            return True
        return False

    def winner(self) -> Optional[str]:
        """Return 'X' or 'O' if someone wins, else None."""
        lines = []
        # rows and cols
        lines.extend(self._grid)
        lines.extend([[self._grid[r][c] for r in range(3)] for c in range(3)])
        # diagonals
        lines.append([self._grid[i][i] for i in range(3)])
        lines.append([self._grid[i][2 - i] for i in range(3)])
        for line in lines:
            if line[0] != " " and line.count(line[0]) == 3:
                return line[0]
        return None

    def full(self) -> bool:
        """Return True if the board has no empty cells."""
        return all(cell != " " for row in self._grid for cell in row)


class Player:
    """Represents a player with a name and mark."""

    def __init__(self, name: str, mark: str) -> None:
        self.name = name
        self.mark = mark  # 'X' or 'O'


class Game:
    """Handles turns, input validation, and game loop."""

    def __init__(self, p1: Player, p2: Player) -> None:
        self.board = Board()
        self.players = (p1, p2)
        self.current = 0  # index of current player

    def _parse_move(self, raw: str) -> Optional[Tuple[int, int]]:
        """Parse move 'row col' -> (row, col); return None if invalid."""
        parts = raw.strip().split()
        if len(parts) != 2 or not all(p.isdigit() for p in parts):
            return None
        row, col = (int(parts[0]), int(parts[1]))
        if not (0 <= row < 3 and 0 <= col < 3):
            return None
        return row, col

    def play(self) -> None:
        """Main loop: alternate moves until win or draw."""
        print("Tic-Tac-Toe: rows/cols are 0..2. Enter like: 0 2")
        self.board.display()
        while True:
            player = self.players[self.current]
            raw = input(f"{player.name} ({player.mark}) move: ")
            move = self._parse_move(raw)
            if move is None:
                print("Invalid input. Use two numbers 0..2, e.g. '1 2'.")
                continue
            if not self.board.place(*move, player.mark):
                print("Cell occupied or out of range. Try again.")
                continue

            self.board.display()
            win = self.board.winner()
            if win:
                print(f"🎉 {player.name} wins!")
                return
            if self.board.full():
                print("It's a draw.")
                return
            self.current = 1 - self.current


if __name__ == "__main__":
    Game(Player("Player 1", "X"), Player("Player 2", "O")).play()
