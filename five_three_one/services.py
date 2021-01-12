from collections import defaultdict
from dataclasses import dataclass
from functools import reduce
from typing import Dict, List

WEIGHTS: List[float] = [45, 25, 10, 5, 2.5, 1.25]


@dataclass
class Workout:
    percent: str
    reps: int
    weight: float
    breakdown: str


def format_breakdown(weights: Dict[float, int]) -> str:
    keys = reversed(sorted(weights.keys()))
    result = reduce(
        lambda accumulator, key: accumulator + f"{key}x{weights[key]}, ", keys, ""
    )
    return result[:-2]


def calculate_breakdown(total: float) -> str:
    current: float = 0
    needed: Dict[float, int] = defaultdict(int)
    while current < total:
        remaining = total - current
        for weight in WEIGHTS:
            if weight <= remaining:
                current += weight
                needed[weight] += 1
                break
    return format_breakdown(needed)


def round_to(value: float, increment: float) -> float:
    return round(increment * round(value / increment), 2)


def get_set(percentage: float, training_max: float) -> Workout:
    total_weight = round_to(percentage * training_max / 100, 2.5)
    bar_weight = 45
    weight_per_side = (total_weight - bar_weight) / 2
    breakdown = calculate_breakdown(weight_per_side)
    return Workout(
        percent=f"{percentage}%", reps=5, weight=total_weight, breakdown=breakdown
    )


def get_workout(training_max: float) -> List[Workout]:
    percentages = [40, 50, 60, 65, 75, 85, 65, 65, 65, 65, 65]
    return [get_set(percentage, training_max) for percentage in percentages]
