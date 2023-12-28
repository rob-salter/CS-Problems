DAYS = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

GIFTS = ["a Partridge in a Pear Tree.", "two Turtle Doves, ", "three French Hens, ", "four Calling Birds, ", "five Gold Rings, ", "six Geese-a-Laying, ", "seven Swans-a-Swimming, ", "eight Maids-a-Milking, ", "nine Ladies Dancing, ", "ten Lords-a-Leaping, ", "eleven Pipers Piping, ", "twelve Drummers Drumming, "]

def recite(start_verse, end_verse):

    return ["On the " + DAYS[i] + " day of Christmas my true love gave to me: " + "".join(GIFTS[i:0:-1]) + "and " + GIFTS[0] if i > 0 else "On the " + DAYS[i] + " day of Christmas my true love gave to me: " + "".join(GIFTS[i::-1]) for i in range((start_verse - 1), end_verse)]
