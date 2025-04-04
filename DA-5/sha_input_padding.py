def sha_512_padding(message_size):
    padding = (896 - message_size % 1024) % 1024
    total_length = message_size + padding + 128
    blocks = total_length // 1024
    return padding, blocks

if __name__ == "__main__":
    p, q, k, h_val, private_key, h_M = 23, 11, 5, 7, 3, 4
    input_sequence = f"{p},{q},{k},{h_val},{private_key},{h_M}"
    message_size = len(input_sequence) * 8  # Convert to bits
    padding, blocks = sha_512_padding(message_size)
    print(f"Padding Bits: {padding}\nNo. of Blocks: {blocks}")
