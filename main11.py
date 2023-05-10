import struct


def main(input):

    a = struct.unpack_from(">HIIHI", input, offset=4)


    b = struct.unpack_from(">h3Hqq", input, offset=a[1])

    c = [
        struct.unpack_from(">2HB", input, offset=b[i])
         for
         ]

    d = struct.unpack_from(">8cqI", input, offset=a[4])

    e = struct.unpack_from(">BhB4b", input, offset=d[-1])

    f = struct.unpack_from(">dBfB", input, offset=a[6])

    dict_f = {
        "F1": f[0],
        "F2": f[1],
        "F3": f[2],
        "F4": f[3],
    }

    dict_e = {
        "E1": e[0],
        "E2": e[1],
        "E3": e[2],
        "E4": list(e[3:]),
    }

    dict_d = {
        "D1": "".join([i.decode("utf-8") for i in d[:-2]]),
        "D2": d[-2],
        "D3": dict_e,
    }

    dict_c = [{
        "C1": i[0],
        "C2": i[1],
        "C3": i[2],
        "C4": i[3],
    } for i in c]

    dict_b = [{
        "B1": i,
        "B2": j[1],
        "B3": j[2],
    } for i, j in zip(dict_c, b)]

    dict_a = {
        "A1": dict_b,
        "A2": a[2],
        "A3": a[3],
        "A4": dict_d,
        "A5": a[5],
        "A6": dict_f,
        "A7": list(a[7:-1]),
        "A8": a[-1],
    }

    return dict_a


main(b'DBOH.\x00\x03\x00rl\xd8\xdd\xd2\x00\x86\x16\x00\x00\x00\x9a\xceh\xcd\xb9'
 b'\xbcC\xfc\xe6"\xf5\xb7\xb0D#\xc1\xb8\xd4\xe0\x8e\xe7]\xfc\x14\xe9X@\xaa`'
 b'\xad\x8f\xc5\xe8z~\xfc\xb1\x98\xb60\xb5?\x0e/R\xba\xd5\xfd\xd4|\x1al\x00'
 b'\x00\x00<u\xa2\xd9?\\\r\xa36u@l\xaeU$\x00\x00\x00N\xd8\x91\x9d'
 b'\xbf\x1e\x01\x00\x1edEn5|\xef\x00\x00\x00`1t\xdc\x00\x00\x00G\x00\x00'
 b'\x00Y\x00\x00\x00ki"\xc9\xe6\xbc\x1f\xc4)yogqrjlu\x9e\xa7\x9f\x80\xac{'
 b'\x7f\xef\x00\x00\x00~?\xe3\xb6\x85\xb2\xc0\xec\x8ca\xbf\x00\\(\x1e')