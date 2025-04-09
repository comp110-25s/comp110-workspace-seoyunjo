"""running dictionary.py"""

__author__: str = "730760820"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert keys and values of dictionary and raise KeyError if duplicate"""
    output = {}
    for key in input:
        value = input[key]
        if value in output:
            raise KeyError
        output[value] = key
    return output


def count(values: list[str]) -> dict[str, int]:
    """Count string in the list"""
    result = {}

    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(colors: dict[str, str]) -> str:
    """What is the favorite color in dictionary?"""
    color_counts = {}

    for person in colors:
        color = colors[person]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    most_common_color = ""
    max_count = 0

    for color in colors.values():
        if color_counts[color] > max_count:
            most_common_color = color
            max_count = color_counts[color]
    return most_common_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    result = {}
    for word in words:
        word_length = len(word)
        if word_length not in result:
            result[word_length] = set()
        result[word_length].add(word)
    return result
