def create_cyclic_pattern(input_charset: str, num_patterns: int, pattern_length: int) -> list[str]:
    """
    Generates a series of cyclic patterns based on an input character set.

    This function creates patterns by treating the characters in `input_charset`
    as digits in a custom base system. It starts with the first character
    repeated `pattern_length` times and increments from there, cycling through
    the characters.

    Args:
        input_charset: A string containing the unique characters to use for
                       generating patterns (e.g., "ABC", "01").
        num_patterns: The total number of patterns to generate.
        pattern_length: The fixed length of each generated pattern.

    Returns:
        A list of strings, where each string is a generated pattern.
        Returns an empty list if the input_charset is empty.

    Example:
        >>> generate_cyclic_pattern("AB", 5, 4)
        ['AAAA', 'AAAB', 'AABA', 'AABB', 'ABAA']
        >>> generate_cyclic_pattern("012", 4, 2)
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
    generated_patterns = []

    # --- Pattern Generation Loop ---
    for _ in range(num_patterns):
        # 1. Build the current pattern string from the indices.
        # We use a list comprehension and join for efficiency.
        current_pattern = "".join([input_charset[i] for i in indices])
        generated_patterns.append(current_pattern)

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
                # If we've carried over from the very first digit (i == 0),
                # it means we have wrapped around the maximum possible pattern.
                # We can handle this case if needed, but for now, it just wraps.

    return generated_patterns

# --- Example Usage ---
if __name__ == '__main__':
    # Recreate the example from the prompt.
    # We'll assume the input character set is the uppercase alphabet.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    example_patterns = create_cyclic_pattern(alphabet, 2, 4)
    print(f"Example from prompt ('{alphabet}', 2, 4):")
    print(example_patterns)
    print("-" * 20)

    # Another example with a smaller character set.
    binary_charset = "01"
    binary_patterns = generate_cyclic_pattern(binary_charset, 8, 4)
    print(f"Binary example ('{binary_charset}', 8, 4):")
    print(binary_patterns)
    print("-" * 20)
    
    # An example with more "digits".
    hex_charset = "0123456789ABCDEF"
    hex_patterns = generate_cyclic_pattern(hex_charset, 20, 2)
    print(f"Hexadecimal example ('{hex_charset}', 20, 2):")
    print(hex_patterns)
    print("-" * 20)

