DAY = [None, 'first', 'second', 'third', 'fourth', 'fifth', 'sixth',
       'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

GIFTS = [
    "twelve Drummers Drumming",
    "eleven Pipers Piping",
    "ten Lords-a-Leaping",
    "nine Ladies Dancing",
    "eight Maids-a-Milking",
    "seven Swans-a-Swimming",
    "six Geese-a-Laying",
    "five Gold Rings",
    "four Calling Birds",
    "three French Hens",
    "two Turtle Doves",
    "and a Partridge in a Pear Tree."
]


def _get_gift(start_verse: int) -> str:
    if start_verse == 1:
        return GIFTS[-start_verse].replace("and ", "")
    return ", ".join(GIFTS[-start_verse:])


def recite(start_verse, end_verse):
    return [f"On the {DAY[i]} day of Christmas my true love gave to me: {_get_gift(i)}" for i in range(start_verse, end_verse+1)]


print(recite(1, 1))
