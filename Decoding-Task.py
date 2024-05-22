def decode(message_file):
    with open(message_file, 'r') as file:
        num_wrd = {}
        for line in file:
            num, word = line.split()
            num_wrd[int(num)] = word
    msg = ''
    l_end = 1
    total_num = max(num_wrd.keys())
    while l_end <= total_num:
        msg += num_wrd[l_end] + ' '
        l_end += int((1 + (1 + 8 * l_end)**0.5) / 2)
    return msg.strip()
print(decode('coding_qual_input.txt'))
