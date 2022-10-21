import time


def get_day(song_days):
    lyrics_day = ""
    match song_days:
        case 1:
            lyrics_day = "first day"
        case 2:
            lyrics_day = "second day"
        case 3:
            lyrics_day = "third day"
        case 4:
            lyrics_day = "fourth day"
        case 5:
            lyrics_day = "fifth day"
        case 6:
            lyrics_day = "sixth day"
        case 7:
            lyrics_day = "seventh day"
        case 8:
            lyrics_day = "eight day"
        case 9:
            lyrics_day = "ninth day"
        case 10:
            lyrics_day = "tenth day"
        case 11:
            lyrics_day = "eleventh day"
        case 12:
            lyrics_day = "twelfth day"
    return "On the " + lyrics_day


time.sleep(2)


def generate_lyrics(day):
    lyrics = ""
    for count in range(day, 0, -1):
        match count:
            case 12:
                lyrics += "Twelve drummers drumming\n"
            case 11:
                lyrics += "Eleven pipers piping\n"
            case 10:
                lyrics += "Ten lords a-leaping\n"
            case 9:
                lyrics += "Nine ladies dancing\n"
            case 8:
                lyrics += 'Eight maids a-milking\n'
            case 7:
                lyrics += 'Seven swans a-swimming\n'
            case 6:
                lyrics += 'Six geese a-laying\n'
            case 5:
                lyrics += 'Five golden rings\n'
            case 4:
                lyrics += 'Four calling birds\n'
            case 3:
                lyrics += 'Three french hens\n'
            case 2:
                lyrics += "Two turtle doves\n"
            case 1:
                lyrics += 'And a partridge in a pear tree\n'
    return lyrics


if __name__ == '__main__':
    for day in range(1, 13):
        print(get_day(day) + " of christmas my true love sent to me")
        print(generate_lyrics(day))
        time.sleep(2)

