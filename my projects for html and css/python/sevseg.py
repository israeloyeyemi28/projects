def getSevSegStr(number, width):
    # Define the seven-segment display patterns for each digit (0-9).
    # Each pattern represents a row of segments: top, middle, bottom.
    segments = {
        '0': ['###', '# #', '# #', '# #', '###'],
        '1': ['  #', '  #', '  #', '  #', '  #'],
        '2': ['###', '  #', '###', '#  ', '###'],
        '3': ['###', '  #', '###', '  #', '###'],
        '4': ['# #', '# #', '###', '  #', '  #'],
        '5': ['###', '#  ', '###', '  #', '###'],
        '6': ['###', '#  ', '###', '# #', '###'],
        '7': ['###', '  #', '  #', '  #', '  #'],
        '8': ['###', '# #', '###', '# #', '###'],
        '9': ['###', '# #', '###', '  #', '###']
    }

    # Get the seven-segment representation for each digit.
    digit_lines = []
    for digit in number:
        if digit in segments:
            digit_lines.append(segments[digit])
        else:
            digit_lines.append([''] * 5)

    # Combine the lines for each digit horizontally.
    combined_lines = []
    for row in range(5):
        combined_line = ''
        for digit_line in digit_lines:
            combined_line += digit_line[row].ljust(width)
        combined_lines.append(combined_line)

    # Join the lines into a single string with newlines between them.
    return '\n'.join(combined_lines)