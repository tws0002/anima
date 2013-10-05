# -*- coding: utf-8 -*-
# Copyright (c) 2012-2013, Anima Istanbul
# 
# This module is part of anima-tools and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause

import struct


LUTS = {
    'standard': {
        'byte_order': '!',
        'char_to_int': {
            '!': 0, '#': 2, '"': 1, '%': 4, '$': 3, "'": 6, '&': 5, ')': 8,
            '(': 7, '+': 10, '*': 9, '-': 12, ',': 11, '/': 14, '.': 13,
            '1': 16, '0': 15, '3': 18, '2': 17, '5': 20, '4': 19, '7': 22,
            '6': 21, '9': 24, '8': 23, ';': 26, ':': 25, '=': 28, '<': 27,
            '?': 30, '>': 29, 'A': 32, '@': 31, 'C': 34, 'B': 33, 'E': 36,
            'D': 35, 'G': 38, 'F': 37, 'I': 40, 'H': 39, 'K': 42, 'J': 41,
            'M': 44, 'L': 43, 'O': 46, 'N': 45, 'Q': 48, 'P': 47, 'S': 50,
            'R': 49, 'U': 52, 'T': 51, 'W': 54, 'V': 53, 'Y': 56, 'X': 55,
            '[': 58, 'Z': 57, ']': 60, '\\': 59, '_': 62, '^': 61, 'a': 64,
            '`': 63, 'c': 66, 'b': 65, 'e': 68, 'd': 67, 'g': 70, 'f': 69,
            'i': 72, 'h': 71, 'k': 74, 'j': 73, 'm': 76, 'l': 75, 'o': 78,
            'n': 77, 'q': 80, 'p': 79, 's': 82, 'r': 81, 'u': 84, 't': 83
        },
        'int_to_char': [
            '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
            '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':',
            ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a',
            'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u'
        ]
    },
    'rfc1924': {
        'byte_order': '!',
        'char_to_int': {
            '0': 0, '1': 1, '2': 2,  '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
            'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21,
            'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28,
            'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35,
            'a': 36, 'b': 37, 'c': 38, 'd': 39, 'e': 40, 'f': 41, 'g': 42,
            'h': 43, 'i': 44, 'j': 45, 'k': 46, 'l': 47, 'm': 48, 'n': 49,
            'o': 50, 'p': 51, 'q': 52, 'r': 53, 's': 54, 't': 55, 'u': 56,
            'v': 57, 'w': 58, 'x': 59, 'y': 60, 'z': 61, '!': 62, '#': 63,
            '$': 64, '%': 65, '&': 66, '(': 67, ')': 68, '*': 69, '+': 70,
            '-': 71, ';': 72, '<': 73, '=': 74, '>': 75, '?': 76, '@': 77,
            '^': 78, '_': 79, '`': 80, '{': 81, '|': 82, '}': 83, '~': 84
        },
        'int_to_char': [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C',
            'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c',
            'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '#', '$',
            '%', '&', '(', ')', '*', '+', '-', ';', '<', '=', '>', '?', '@',
            '^', '_', '`', '{', '|', '}', '~'
        ]
    },
    'arnold': {
        'byte_order': '<',
        'expansion_char': '!',
        'char_to_int': {
            '%': 1, '$': 0, "'": 3, '&': 2, ')': 5, '(': 4, '+': 7, '*': 6,
            '-': 9, ',': 8, '/': 11, '.': 10, '1': 13, '0': 12, '3': 15,
            '2': 14, '5': 17, '4': 16, '7': 19, '6': 18, '9': 21, '8': 20,
            ';': 23, ':': 22, '=': 25, '<': 24, '?': 27, '>': 26, 'A': 29,
            '@': 28, 'C': 31, 'B': 30, 'E': 33, 'D': 32, 'G': 35, 'F': 34,
            'I': 37, 'H': 36, 'K': 39, 'J': 38, 'M': 41, 'L': 40, 'O': 43,
            'N': 42, 'Q': 45, 'P': 44, 'S': 47, 'R': 46, 'U': 49, 'T': 48,
            'W': 51, 'V': 50, 'Y': 53, 'X': 52, '[': 55, 'Z': 54, ']': 57,
            '\\': 56, '_': 59, '^': 58, 'a': 61, '`': 60, 'c': 63, 'b': 62,
            'e': 65, 'd': 64, 'g': 67, 'f': 66, 'i': 69, 'h': 68, 'k': 71,
            'j': 70, 'm': 73, 'l': 72, 'o': 75, 'n': 74, 'q': 77, 'p': 76,
            's': 79, 'r': 78, 'u': 81, 't': 80, 'w': 83, 'v': 82, 'x': 84
        },
        'int_to_char': [
            '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=',
            '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
            'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c',
            'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x'
        ]
    },
}


def __b85_encode(data, lut, byte_order, zero_pack=True):
    """Encodes the given string data in to Base85 using the given LUT

    :param str data: A string which contains a string to be encoded in Base85
    :param dict lut: The lut to be used in encoding
    :param str byte_order: The byte order character for struct.unpack
    :param bool zero_pack: If true the value of 0 will be encoded to "z"
    :returns: str
    """
    # pad data
    padding = (4 - len(data) % 4) % 4
    data = ''.join([data, '\0' * padding])
    parts = []
    parts_append = parts.append
    number_of_chunks = len(data) // 4
    byte_format = '%s%sI' % (byte_order, number_of_chunks)
    unpack = struct.unpack
    for x in unpack(byte_format, data):
        # network order (big endian), 32-bit unsigned integer
        # note: x86 is little endian
        parts_append(lut[(x // 52200625)])
        parts_append(lut[(x // 614125) % 85])
        parts_append(lut[(x // 7225) % 85])
        parts_append(lut[(x // 85) % 85])
        parts_append(lut[x % 85])
    return_val = ''.join(parts)
    if zero_pack:
        return return_val.replace(lut[0] * 5, 'z')
    return return_val


def b85_encode(data):
    """Encodes the given string data in to Base85 using the standard LUT

    :param str data: A string which contains a string to be encoded in Base85
    :returns: str
    """
    lut = LUTS['standard']['int_to_char']
    byte_order = LUTS['standard']['byte_order']
    return __b85_encode(data, lut, byte_order, False)


def rfc1924_b85_encode(data):
    """Encodes the given string data in to Base85 using the RFC1924 LUT

    :param str data: A string which contains a string to be encoded in Base85
    :returns: str
    """
    lut = LUTS['rfc1924']['int_to_char']
    byte_order = LUTS['rfc1924']['byte_order']
    return __b85_encode(data, lut, byte_order, False)

def arnold_b85_encode(data):
    """Encodes the given string data in to Base85 using the arnold LUT

    :param str data: A string which contains a string to be encoded in Base85
    :returns: str
    """
    lut = LUTS['arnold']['int_to_char']
    byte_order = LUTS['arnold']['byte_order']
    return __b85_encode(data, lut, byte_order, True)

def __b85_decode(data, lut, byte_order, unpack_z=True):
    """Decodes the given string data by using the given LUT and byte order

    :param str data: A string which contains the encoded data
    :param dict lut: A dict where the keys are encoded characters and the
      values are the integer correspondence of those characters and will be
      used to generate an integer number.
    :param str byte_order: The byte order character for struct.pack
    :param bool unpack_z: replaces character "z" with appropriate characters
      for the "0 special case" (where it is not converted to a 5 character
      string but "z")
    """
    if unpack_z:
        zero_key = None
        for key in lut.keys():
            if lut[key] == 0:
                zero_key = key
                break
        if zero_key:
            data = data.replace('z', zero_key * 5)

    parts = []
    parts_append = parts.append
    pack = struct.pack
    byte_format = '%sI' % byte_order 
    for i in xrange(0, len(data), 5):
        int_sum = 52200625 * lut[data[i]] + \
               614125 * lut[data[i + 1]] + \
               7225 * lut[data[i + 2]] + \
               85 * lut[data[i + 3]] + \
               lut[data[i + 4]]
        parts_append(pack(byte_format, int_sum))
    return ''.join(parts)

def b85_decode(data):
    """Decodes the given string data by using the standard LUT and network (=
    big endian) byte order.

    :param str data: A string which contains the encoded data
    """
    lut = LUTS['standard']['char_to_int']
    byte_order = LUTS['standard']['byte_order']
    return __b85_decode(data, lut, byte_order)

def rfc1924_b85_decode(data):
    """Decodes the given string data by using the RFC1924 LUT and network (=
    big endian) byte order.

    :param str data: A string which contains the encoded data
    """
    lut = LUTS['rfc1924']['char_to_int']
    byte_order = LUTS['rfc1924']['byte_order']
    return __b85_decode(data, lut, byte_order, unpack_z=False)

def arnold_b85_decode(data):
    """Decodes the given string data by using the Arnold LUT and network (=
    big endian) byte order.

    :param str data: A string which contains the encoded data
    """
    lut = LUTS['arnold']['char_to_int']
    byte_order = LUTS['arnold']['byte_order']
    return __b85_decode(data, lut, byte_order)

def mapper(encoded_data, raw_data, strip_z=True):
    """A simple utility to create a lut for known Base85 encoding

    :param str encoded_data: The path of the encoded file,
    :param list raw_data: A list of raw data, showing the unencoded data
    """
    
    if strip_z:
        # special case replace 'z's with '!!!!!'
        data = encoded_data.replace('z', '!!!!!').strip()
    else:
        data = encoded_data

    # half encode to base85, without using a lut
    half_encoded = []
    unpack = struct.unpack
    pack = struct.pack
    for i in xrange(0, len(raw_data)):
        # get the unencoded base85 of the
        # integer corresponding of the float number
        unencoded_base85 = unpack('I', pack('f', raw_data[i]))[0]
        half_encoded.append(unencoded_base85 // 52200625)
        half_encoded.append((unencoded_base85 // 614125) % 85)
        half_encoded.append((unencoded_base85 // 7225) % 85)
        half_encoded.append((unencoded_base85 // 85) % 85)
        half_encoded.append(unencoded_base85 % 85)

    lut = {}
    for i in range(len(half_encoded)):
        lut[data[i]] = half_encoded[i]

    return lut


def auto_mapper(encoded_data_path, raw_data):
    """A simple utility to create a lut for known Base85 encoding

    :param str encoded_data_path: The path of the encoded file,
    :param list raw_data: A list of raw numbers, showing the unencoded data
    """
    data = open(encoded_data_path, 'r').read().strip()
    return mapper(data, raw_data)