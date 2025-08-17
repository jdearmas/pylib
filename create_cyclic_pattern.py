import argparse

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
        Returns an empty list if the input_charset is empty.

    Example:
        >>> create_cyclic_pattern("AB", 5, 4)
        ['AAAA', 'AAAB', 'AABA', 'AABB', 'ABAA']
        >>> create_cyclic_pattern("012", 4, 2)
        ['00', '01', '02', '10']
    """
    # --- Input Validation ---
    if not input_charset:
        print("Warning: input_charset cannot be empty.")
        return []
    if num_patterns <= 0:
        print("Warning: num_patterns must be a positive integer.")
        return []
    if pattern_length <= 0:
        print("Warning: pattern_length must be a positive integer.")
        return []

    # --- Initialization ---
    base = len(input_charset)
    # This list holds the indices for the characters in the current pattern.
    # It's like the digits of a number. We start at all zeros (e.g., [0, 0, 0, 0]).
    indices = [0] * pattern_length
    created_patterns = []

    # --- Pattern Generation Loop ---
    for _ in range(num_patterns):
        # 1. Build the current pattern string from the indices.
        # We use a list comprehension and join for efficiency.
        current_pattern = "".join([input_charset[i] for i in indices])
        created_patterns.append(current_pattern)

        # 2. Increment the indices for the next pattern (like counting).
        # We start from the rightmost "digit" (the end of the list).
        for i in range(pattern_length - 1, -1, -1):
            # Increment the current index
            indices[i] += 1

            # Check if we need to "carry over" to the next digit.
            if indices[i] < base:
                # If the index is still within the bounds of our charset,
                # we're done incrementing for this pattern.
                break
            else:
                # If we've exceeded the base, reset this index to 0
                # and the loop will continue to the next digit to the left.
                indices[i] = 0

    return created_patterns

# --- Command-Line Interface ---
if __name__ == '__main__':
    # Set up the argument parser to handle command-line inputs.
    parser = argparse.ArgumentParser(
        description="create the first pattern of a cyclic sequence. \n"
                    "Example usage: python your_script_name.py ABC 4"
    )
    parser.add_argument(
        "input_charset",
        type=str,
        help="A string of unique characters to use for the pattern (e.g., 'ABC')."
    )
    parser.add_argument(
        "pattern_length",
        type=int,
        help="The fixed length of the pattern."
    )

    args = parser.parse_args()

    # To output only the 'AAAA' style pattern, we call the main function
    # asking for just one pattern.
    first_pattern_list = create_cyclic_pattern(
        input_charset=args.input_charset,
        num_patterns=1,
        pattern_length=args.pattern_length
    )

    # The function returns a list; we print the first (and only) element.
    if first_pattern_list:
        print(first_pattern_list[0])
