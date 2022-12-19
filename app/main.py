from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> None:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> None:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> None:
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        return Distance(km=self.km + other)

    def __iadd__(self, other: Distance | int | float) -> None:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int | float) -> None:
        if isinstance(other, int | float):
            return Distance(km=self.km * other)
        raise TypeError

    def __truediv__(self, other: int | float) -> None:
        if isinstance(other, int | float):
            return Distance(km=round(self.km / other, 2))
        raise TypeError

    def __lt__(self, other: Distance | int | float) -> None:
        return self.km < other

    def __gt__(self, other: Distance | int | float) -> None:
        return self.km > other

    def __eq__(self, other: Distance | int | float) -> None:
        return self.km == other

    def __le__(self, other: Distance | int | float) -> None:
        return self.km <= other

    def __ge__(self, other: Distance | int | float) -> None:
        return self.km >= other
