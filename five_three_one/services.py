from collections import Counter
from dataclasses import dataclass
from functools import reduce
from typing import List, Generator

WEIGHTS: List[float] = [45, 25, 10, 5, 2.5, 1.25]
BAR_WEIGHT = 45
SET_PERCENTAGES = {
    1: [40, 50, 60, 65, 75, 85, 65, 65, 65, 65, 65],
    2: [40, 50, 60, 70, 80, 90, 70, 70, 70, 70, 70],
    3: [40, 50, 60, 75, 85, 95, 75, 75, 75, 75, 75],
}


@dataclass
class Workout:
    percent: str
    reps: int
    weight: float
    breakdown: str


def format_breakdown(weights: List[float]) -> str:
    weights_in_order = reversed(sorted(set(weights)))
    weight_counts = Counter(weights)
    result = reduce(
        lambda accumulator, key: accumulator + f"{key}x{weight_counts[key]}, ",
        weights_in_order,
        "",
    )
    return result[:-2]


def next_weight_needed(final_value: float) -> Generator[float, None, None]:
    current_value = 0.0
    while current_value < final_value:
        remaining = final_value - current_value
        value_to_add = next((weight for weight in WEIGHTS if weight <= remaining), 0)
        current_value += value_to_add
        yield value_to_add


def calculate_breakdown(total: float) -> str:
    weights_needed_per_side = list(next_weight_needed(total))
    return format_breakdown(weights_needed_per_side)


def round_to(value: float, increment: float) -> float:
    return round(increment * round(value / increment), 2)


def get_set(percentage: float, training_max: float) -> Workout:
    total_weight = round_to(percentage * training_max / 100, 2.5)
    weight_per_side = (total_weight - BAR_WEIGHT) / 2
    breakdown = calculate_breakdown(weight_per_side)
    return Workout(
        percent=f"{percentage}%",
        reps=5,
        weight=total_weight,
        breakdown=breakdown,
    )


def get_workout(training_max: float, week_number: int) -> List[Workout]:
    return [
        get_set(percentage, training_max) for percentage in SET_PERCENTAGES[week_number]
    ]
