import random
import textwrap
import argentina


def create_even_sections(cur_list, sections):
    total_words = len(cur_list)
    # Convert list to a NumPy array for easy manipulation
    idxs = [round(i * total_words / sections) for i in range(sections)]
    idxs += [total_words]  # Ensure the last section goes to the end of the list
    # Use the indices to split the list into sections
    sections_list = [cur_list[idxs[i]:idxs[i + 1]] for i in range(sections)]
    return sections_list

# Function to generate a bingo chart
def generate_bingo_chart(word_list, center_word, width=5):

    # Remove the center word from the list for now as it will be placed in the center
    if center_word:
        word_list.remove(center_word)

    sections = create_even_sections(word_list, width)
    # Create the bingo board
    bingo_board = []
    for section in sections:
        selected_words = random.sample(section, width)  # Pick 5 words from each section
        bingo_board.extend(selected_words)

    # Randomize the final board order, except the center slot for "Wowisimo"
    random.shuffle(bingo_board)
    center_index = 12  # Center of a 5x5 bingo board
    if center_word:
        bingo_board.insert(center_index, center_word)  # Insert "Wowisimo" at the center

    # Convert list to 5x5 format
    bingo_board_formatted = [bingo_board[i:i + width] for i in range(0, width ** 2, width)]

    return bingo_board_formatted


# Function to convert the bingo chart into a tab-separated list for Excel
def bingo_chart_to_tsv(bingo_chart):
    return '\n'.join(['\t'.join(row) for row in bingo_chart])


# New function to create a sublist from the original list while respecting constraints
def create_sublist_from_constraints(original_list, constraint_sets):
    # Select one word from each constraint set
    selected_words = set()
    for constraint_set in constraint_sets:
        selected_word = random.choice(list(constraint_set))
        selected_words.add(selected_word)

    # Create the new sublist by including only the selected words from each set and all other words
    new_sublist = []
    for word in original_list:
        # Add the word if it's selected or not in any constraint set
        if word in selected_words or not any(word in constraint_set for constraint_set in constraint_sets):
            new_sublist.append(word)

    return new_sublist


def center_ascii_art(ascii_art, total_width):
    # First, find the maximum length of any line in the ASCII art.
    max_line_length = max(len(line) for line in ascii_art.split('\n'))

    # How many spaces to add to the left of the art to center it
    left_padding = (total_width - max_line_length) // 2

    # Add the left padding to each line of the ASCII art.
    # Also add the vertical borders directly to each line.
    centered_lines = ['|' + ' ' * left_padding + line + ' ' * (total_width - left_padding - len(line) - 2) + '|' for
                      line in ascii_art.split('\n')]

    # Construct the full centered ASCII art with borders.
    top_bottom_border = '+' + '-' * (total_width - 2) + '+'

    # Combine all parts.
    return top_bottom_border + '\n' + '\n'.join(centered_lines)


def format_word_for_cell(word, width=15, height=3):
    """Format a word to fit into a bingo card cell, spread over three lines."""
    # Wrap the word into lines of the given width.
    wrapped_lines = textwrap.wrap(word, width)
    # Ensure the word takes up exactly 'height' lines.
    wrapped_lines += [''] * (height - len(wrapped_lines))
    # Center each line within the cell.
    return [line.center(width) for line in wrapped_lines[:height]]


def generate_ascii_bingo_chart_text(bingo_chart, ascii_art_header, width=15, height=3):
    # ascii_bingo_chart = ascii_art_header
    bingo_width = len(bingo_chart)

    ascii_bingo_chart = center_ascii_art(ascii_art_header, (width + 1) * bingo_width + 1) + '\n'  # Center the header
    card_str = ascii_bingo_chart  # Start with the ASCII art header
    # Process each row in the bingo chart.
    for row in bingo_chart:
        # Process each word in the row for the cell.
        cell_lines_list = [format_word_for_cell(word, width, height) for word in row]
        # Top border of the row.
        card_str += '+' + ('-' * width + '+') * len(row) + '\n'
        # Content of the row.
        for line_index in range(height):
            row_str = '|'.join(cell_lines[line_index] for cell_lines in cell_lines_list)
            card_str += f"|{row_str}|\n"
    # Bottom border of the last row.
    card_str += '+' + ('-' * width + '+') * len(row) + '\n'
    return card_str


def generate_one_bingo(theme=argentina, width=5):
    # Convert the example bingo chart to a tab-separated format
    cur_list = create_sublist_from_constraints(theme.sorted_list, theme.constraints).copy()
    bingo_chart_example = generate_bingo_chart(cur_list, theme.center_word, width)

    # bingo_chart_example
    ascii_bingo_chart_text = generate_ascii_bingo_chart_text(bingo_chart_example, theme.ascii_art_header)
    return ascii_bingo_chart_text

def generate_sheets(n, theme=argentina):
    bingo_boards_output = "\n\n".join([generate_one_bingo(theme) for _ in range(n)])
    return bingo_boards_output


def print_bingo_sheets(n, output_file_path, theme=argentina):
    bingo_boards_output = generate_sheets(n, theme)
    # Write the generated bingo boards to a text file
    with open(output_file_path, 'w') as file:
        file.write(bingo_boards_output)

