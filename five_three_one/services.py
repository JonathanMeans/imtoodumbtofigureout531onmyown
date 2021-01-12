from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Workout:
    percent: str
    reps: int
    weight: float
    breakdown: str


def format_breakdown(weights: Dict[float, int]) -> str:
    keys = reversed(sorted(weights.keys()))
    result = ""
    for key in keys:
        result += f"{key}x{weights[key]}, "
    return result[:-2]


def calculate_breakdown(total: float) -> str:
    WEIGHTS: List[float] = [45, 25, 10, 5, 2.5, 1.5]
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


def get_workout(training_max: int) -> Workout:
    total_weight = 0.4 * training_max
    bar_weight = 45
    weight_per_side = (total_weight - bar_weight) / 2
    breakdown = calculate_breakdown(weight_per_side)
    return Workout(percent="40%", reps=5, weight=total_weight, breakdown=breakdown)
