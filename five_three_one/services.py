from collections import defaultdict
from dataclasses import dataclass
from functools import reduce
from typing import Dict, List

WEIGHTS: List[float] = [45, 25, 10, 5, 2.5, 1.25]
BAR_WEIGHT = 45
SET_PERCENTAGES = [40, 50, 60, 65, 75, 85, 65, 65, 65, 65, 65]


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
    weights_needed_per_side: Dict[float, int] = defaultdict(int)
    while current < total:
        current += add_largest_valid_weight(weights_needed_per_side, current, total)
    return format_breakdown(weights_needed_per_side)


def add_largest_valid_weight(
    weights_per_side: Dict[float, int], current: float, total: float
) -> float:
    remaining = total - current
    weight_to_add = next((weight for weight in WEIGHTS if weight <= remaining), 0)
    weights_per_side[weight_to_add] += 1
    return weight_to_add


def round_to(value: float, increment: float) -> float:
    return round(increment * round(value / increment), 2)


def get_set(percentage: float, training_max: float) -> Workout:
    total_weight = round_to(percentage * training_max / 100, 2.5)
    weight_per_side = (total_weight - BAR_WEIGHT) / 2
    breakdown = calculate_breakdown(weight_per_side)
    return Workout(
        percent=f"{percentage}%", reps=5, weight=total_weight, breakdown=breakdown
    )


def get_workout(training_max: float) -> List[Workout]:
    return [get_set(percentage, training_max) for percentage in SET_PERCENTAGES]
