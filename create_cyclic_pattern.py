import argparse
import string

def create_cyclic_pattern(input_charset: str, num_patterns: int, pattern_length: int) -> list[str]:
    """
    creates a series of cyclic patterns based on an input character set.

    This function creates patterns by treating the characters in `input_charset`
    as digits in a custom base system. It starts with the first character
    repeated `pattern_length` times and increments from there, cycling through
    the characters.

    Args:
        input_charset: A string containing the unique characters to use for
                       generating patterns (e.g., "ABC", "01").
        num_patterns: The total number of patterns to create.
        pattern_length: The fixed length of each created pattern.

    Returns:
        A list of strings, where each string is a created pattern.
        Returns an empty list if input validation fails.
    """
    # --- Input Validation ---
    if not input_charset:
        print("Error: Character set cannot be empty.")
        return []
    if num_patterns <= 0:
        print("Error: Number of patterns must be a positive integer.")
        return []
    if pattern_length <= 0:
        print("Error: Pattern length must be a positive integer.")
        return []

    # --- Initialization ---
    base = len(input_charset)
    # This list holds the indices for the characters in the current pattern.
    # We start at all zeros (e.g., [0, 0, 0, 0] for 'AAAA').
    indices = [0] * pattern_length
    created_patterns = []

    # --- Pattern Generation Loop ---
    for _ in range(num_patterns):
        # 1. Build the current pattern string from the indices.
        current_pattern = "".join([input_charset[i] for i in indices])
        created_patterns.append(current_pattern)

        # 2. Increment the indices for the next pattern (like base-26 counting).
        # Start from the rightmost "digit".
        for i in range(pattern_length - 1, -1, -1):
            indices[i] += 1
            # If the index is still within the bounds of our charset,
            # we're done incrementing for this pattern.
            if indices[i] < base:
                break
            # Otherwise, reset this index to 0 and carry over to the left.
            else:
                indices[i] = 0

    return created_patterns

# --- Command-Line Interface ---
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="create a sequence of cyclic patterns using the alphabet.\n"
                    "Example usage: python your_script_name.py 3 4"
    )
    parser.add_argument(
        "num_patterns",
        type=int,
        help="The total number of patterns to create."
    )
    parser.add_argument(
        "pattern_length",
        type=int,
        help="The fixed length of each pattern."
    )

    args = parser.parse_args()

    # The character set is now fixed to the uppercase alphabet.
    alphabet_charset = string.ascii_uppercase

    # create the requested number of patterns.
    patterns = create_cyclic_pattern(
        input_charset=alphabet_charset,
        num_patterns=args.num_patterns,
        pattern_length=args.pattern_length
    )

    # Print the resulting patterns on a single line, separated by spaces.
    if patterns:
        print(" ".join(patterns))
