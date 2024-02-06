# miniGPT
def decode(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Dictionary to store number-word pairs
    number_word_dict = {}
    for line in lines:
        number, word = line.split()
        number_word_dict[int(number)] = word

    # Decode the message
    decoded_message = []
    row_end = 1
    row_length = 1
    while row_end in number_word_dict:
        decoded_message.append(number_word_dict[row_end])
        row_length += 1
        row_end += row_length

    return ' '.join(decoded_message)

# Example usage
message = decode('coding_qual_input.txt')
print(message)
