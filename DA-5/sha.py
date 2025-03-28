import binascii
import struct

# Initial hash values
initial_hash = (
    0x6A09E667F3BCC908,
    0xBB67AE8584CAA73B,
    0x3C6EF372FE94F82B,
    0xA54FF53A5F1D36F1,
    0x510E527FADE682D1,
    0x9B05688C2B3E6C1F,
    0x1F83D9ABFB41BD6B,
    0x5BE0CD19137E2179,
)

# Round constants
round_constants = (
    0x428A2F98D728AE22,
    0x7137449123EF65CD,
    0xB5C0FBCFEC4D3B2F,
    0xE9B5DBA58189DBBC,
    0x3956C25BF348B538,
    0x59F111F1B605D019,
    0x923F82A4AF194F9B,
    0xAB1C5ED5DA6D8118,
    0xD807AA98A3030242,
    0x12835B0145706FBE,
    0x243185BE4EE4B28C,
    0x550C7DC3D5FFB4E2,
    0x72BE5D74F27B896F,
    0x80DEB1FE3B1696B1,
    0x9BDC06A725C71235,
    0xC19BF174CF692694,
    0xE49B69C19EF14AD2,
    0xEFBE4786384F25E3,
    0x0FC19DC68B8CD5B5,
    0x240CA1CC77AC9C65,
    0x2DE92C6F592B0275,
    0x4A7484AA6EA6E483,
    0x5CB0A9DCBD41FBD4,
    0x76F988DA831153B5,
    0x983E5152EE66DFAB,
    0xA831C66D2DB43210,
    0xB00327C898FB213F,
    0xBF597FC7BEEF0EE4,
    0xC6E00BF33DA88FC2,
    0xD5A79147930AA725,
    0x06CA6351E003826F,
    0x142929670A0E6E70,
    0x27B70A8546D22FFC,
    0x2E1B21385C26C926,
    0x4D2C6DFC5AC42AED,
    0x53380D139D95B3DF,
    0x650A73548BAF63DE,
    0x766A0ABB3C77B2A8,
    0x81C2C92E47EDAEE6,
    0x92722C851482353B,
    0xA2BFE8A14CF10364,
    0xA81A664BBC423001,
    0xC24B8B70D0F89791,
    0xC76C51A30654BE30,
    0xD192E819D6EF5218,
    0xD69906245565A910,
    0xF40E35855771202A,
    0x106AA07032BBD1B8,
    0x19A4C116B8D2D0C8,
    0x1E376C085141AB53,
    0x2748774CDF8EEB99,
    0x34B0BCB5E19B48A8,
    0x391C0CB3C5C95A63,
    0x4ED8AA4AE3418ACB,
    0x5B9CCA4F7763E373,
    0x682E6FF3D6B2B8A3,
    0x748F82EE5DEFB2FC,
    0x78A5636F43172F60,
    0x84C87814A1F0AB72,
    0x8CC702081A6439EC,
    0x90BEFFFA23631E28,
    0xA4506CEBDE82BDE9,
    0xBEF9A3F7B2C67915,
    0xC67178F2E372532B,
    0xCA273ECEEA26619C,
    0xD186B8C721C0C207,
    0xEADA7DD6CDE0EB1E,
    0xF57D4F7FEE6ED178,
    0x06F067AA72176FBA,
    0x0A637DC5A2C898A6,
    0x113F9804BEF90DAE,
    0x1B710B35131C471B,
    0x28DB77F523047D84,
    0x32CAAB7B40C72493,
    0x3C9EBE0A15C9BEBC,
    0x431D67C49C100D4C,
    0x4CC5D4BECB3E42B6,
    0x597F299CFC657E2A,
    0x5FCB6FAB3AD6FAEC,
    0x6C44198C4A475817,
)


def _right_rotate(n: int, bits: int) -> int:
    """Perform right rotation on 64-bit integer."""
    return (n >> bits) | (n << (64 - bits)) & 0xFFFFFFFFFFFFFFFF


def sha512(message: str) -> str:
    """Compute SHA-512 hash of the input message."""
    if not isinstance(message, str):
        raise TypeError("Given message should be a string.")

    # Convert message to bytes
    message_array = bytearray(message, encoding="utf-8")

    # Padding
    mdi = len(message_array) % 128
    padding_len = 119 - mdi if mdi < 112 else 247 - mdi
    ending = struct.pack("!Q", len(message_array) << 3)
    message_array.append(0x80)
    message_array.extend([0] * padding_len)
    message_array.extend(bytearray(ending))

    # Initialize hash values
    sha512_hash = list(initial_hash)

    # Process message in 128-byte chunks
    for chunk_start in range(0, len(message_array), 128):
        chunk = message_array[chunk_start : chunk_start + 128]

        # Prepare message schedule
        w = [0] * 80
        w[0:16] = struct.unpack("!16Q", chunk)

        # Extend message schedule
        for i in range(16, 80):
            s0 = (
                _right_rotate(w[i - 15], 1)
                ^ _right_rotate(w[i - 15], 8)
                ^ (w[i - 15] >> 7)
            )
            s1 = (
                _right_rotate(w[i - 2], 19)
                ^ _right_rotate(w[i - 2], 61)
                ^ (w[i - 2] >> 6)
            )
            w[i] = (w[i - 16] + s0 + w[i - 7] + s1) & 0xFFFFFFFFFFFFFFFF

        # Initialize working variables
        a, b, c, d, e, f, g, h = sha512_hash

        # Main compression loop
        for i in range(80):
            # Sigma functions
            sum1 = _right_rotate(e, 14) ^ _right_rotate(e, 18) ^ _right_rotate(e, 41)

            # Channel function
            ch = (e & f) ^ (~e & g)

            # Temporary values
            temp1 = h + sum1 + ch + round_constants[i] + w[i]

            sum0 = _right_rotate(a, 28) ^ _right_rotate(a, 34) ^ _right_rotate(a, 39)

            # Majority function
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = sum0 + maj

            # Update working variables
            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFFFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFFFFFFFFFF

        # Update hash values
        sha512_hash = [
            (x + y) & 0xFFFFFFFFFFFFFFFF
            for x, y in zip(sha512_hash, (a, b, c, d, e, f, g, h))
        ]

    # Convert final hash to hexadecimal
    return binascii.hexlify(
        b"".join(struct.pack("!Q", element) for element in sha512_hash),
    ).decode("utf-8")


def main():
    # Test cases
    test_messages = ["Hello, world!", "Tanishq Anand", "22BCE0508"]

    # Compute and print hashes
    for msg in test_messages:
        hash_result = sha512(msg)
        print(f"SHA-512 hash of '{msg}':")
        print(hash_result)
        print()


if __name__ == "__main__":
    main()