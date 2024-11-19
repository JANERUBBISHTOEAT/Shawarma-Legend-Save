# Shawarma-Legend-Save

沙威玛传奇存档

存档位置：

```shell
%AppData%\..\Local\s1941
```

TODO:

- [ ] Read Data Structure
- [ ] Write Data Structure
- [ ] A static web page to create and edit save data

## Data Structure

Raw:
00 49 00 4e 18 5a 00 3c 0a 33 00 3c 00 80 fd 44 00 42 00 00 00 00 00 3c 00 3c 00 3c 00 3c 00 bc 00 bc 00 40 00 40 00 40 00 42 00 bc 00 bc 00 3c 00 bc 00 40 00 40 00 00 00 00 00 3c 00 40 00 40 00 00 00 3c 00 00 00 40

Assumptions:

- Non-encrypted
- Little Endian
- The Author/Engine likes to use 16-bit float

Suspect:
[00 49] [00 4e] [18 5a] **(00 3c)** **0a 33** **(00 3c)** [00 80 fd 44] (00 42 00 00 00 00 00 3c 00 3c 00 3c 00 3c 00 bc 00 bc 00 40 00 40 00 40 00 42 00 bc 00 bc 00 3c 00 bc 00 40 00 40 00 00 00 00 00 3c 00 40 00 40 00 00 00 3c 00 00 00 40)

> where [] means somehow related, () means suspect only

| value | type | position | description |
| --- | --- | --- | --- |
| 00 49 | float-16 | 0000 | Lan 10? |
| 00 4e | float-16 | 0002 | Day 24 |
| 18 5a | float-16 | 0004 | 3:15 min (195 sec) |
| 00 80 fd 44 | float-32 | 000C | 2028 Coin |

Suspicious values:

| value | type | position | description |
| --- | --- | --- | --- |
| 00 bc | float-16 | multiple | equipment lv.-1 |
| 00 00 | float-16 | multiple | equipment lv.0 |
| 00 3c | float-16 | multiple | equipment lv.1 |
| 00 40 | float-16 | multiple | equipment lv.2 |
| 00 42 | float-16 | multiple | equipment lv.3 |

---

Conclusion:

- 0x00-0x01: Language, 2 (0x02) bytes, float-16

  ```json
    { // float-16
        0x3C: English, // 1
        0x46: Italian, // 6
        0x49: Chinese  // 10
    }
  ```

- 0x02-0x03: Day count, 2 (0x02) bytes, float-16
- 0x04-0x05: Time count, 2 (0x02) bytes, float-16
- **Unknown**
- 0x0C-0x0F: Coin count, 4 (0x04) bytes, float-32
- 0x10-0x47: Store equipment, 56 (0x38) bytes, float-16

Unknown (unlisted values):

- Volume
- Music
- Voice
- Fullscreen
-
