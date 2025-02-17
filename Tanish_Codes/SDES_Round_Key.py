def permute(original, permutation):
    return [original[i - 1] for i in permutation]  # Adjust index to be 0-based


def left_shift(bits, shift_count):
    return bits[shift_count:] + bits[:shift_count]


def generate_round_keys(key, P10, P8):
    LS1, LS2 = 1, 2
    
    permuted_key = permute(key, P10)
    
    left_half, right_half = permuted_key[:5], permuted_key[5:]
    left_half, right_half = left_shift(left_half, LS1), left_shift(right_half, LS1)
    
    round_key1 = permute(left_half + right_half, P8)
    
    left_half, right_half = left_shift(left_half, LS2), left_shift(right_half, LS2)
    round_key2 = permute(left_half + right_half, P8)
    
    return round_key1, round_key2


key_input = input("10-bit key: ")
key = [int(bit) for bit in key_input]

P10_input = input("P10 (10 nums): ")
P10 = [int(x) for x in P10_input.split()]

P8_input = input("P8 (8 nums): ")
P8 = [int(x) for x in P8_input.split()]

round_key1, round_key2 = generate_round_keys(key, P10, P8)

print("Key 1:", round_key1)
print("Key 2:", round_key2)