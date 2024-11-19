import struct
from base64 import b64decode, b64encode
from json import dumps
from os.path import dirname, expandvars, join


def pretty_print(data):
    print(dumps(data, indent=4, ensure_ascii=False))


def read_save(file_path):
    with open(file_path, "rb") as file:
        base64_str = file.read()

    data = b64decode(base64_str)
    language = struct.unpack("<e", data[0:2])[0]
    day_count = struct.unpack("<e", data[2:4])[0]
    time_count = struct.unpack("<e", data[4:6])[0]
    volume = struct.unpack("<e", data[6:8])[0]
    music = struct.unpack("<e", data[8:10])[0]
    voice = struct.unpack("<e", data[10:12])[0]
    coin_count = struct.unpack("<f", data[12:16])[0]
    equipment = [struct.unpack("<e", data[i : i + 2])[0] for i in range(16, 72, 2)]

    return {
        "language": language,
        "day_count": day_count,
        "time_count": time_count,
        "volume": volume,
        "music": music,
        "voice": voice,
        "coin_count": coin_count,
        "equipment": equipment,
    }


def write_save(file_path, save_data):
    language = struct.pack("<e", save_data["language"])
    day_count = struct.pack("<e", save_data["day_count"])
    time_count = struct.pack("<e", save_data["time_count"])
    volume = struct.pack("<e", save_data["volume"])
    music = struct.pack("<e", save_data["music"])
    voice = struct.pack("<e", save_data["voice"])
    coin_count = struct.pack("<f", save_data["coin_count"])
    equipment = b"".join(struct.pack("<e", val) for val in save_data["equipment"])

    data = (
        language
        + day_count
        + time_count
        + volume
        + music
        + voice
        + coin_count
        + equipment
    )
    base64_str = b64encode(data)

    with open(file_path, "w") as file:
        file.write(base64_str.decode("utf-8"))

    return base64_str


if __name__ == "__main__":
    save_data = read_save(expandvars(r"%AppData%\..\Local\s1941\save.dat"))
    pretty_print(save_data)
    base64_str = write_save(join(dirname(__file__), "new_save.dat"), save_data)
    print(base64_str)
