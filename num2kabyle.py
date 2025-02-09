#!/usr/bin/env python3
import sys

def print_usage():
    usage = (
        "Kabyle Number Converter\n"
        "Usage:\n"
        "  python num2kabyle.py <number>         # Convert a single number\n"
        "  python num2kabyle.py <start>-<end>      # Convert a range of numbers (inclusive)\n"
        "\n"
        "Examples:\n"
        "  python num2kabyle.py 1203514           # Single number conversion\n"
        "  python num2kabyle.py 10-100            # Convert numbers from 10 to 100\n"
        "\n"
        "Supported ranges:\n"
        "  Numbers up to 999,999,999,999 are supported.\n"
    )
    print(usage)

def print_interactive_menu():
    menu = (
        "\nWelcome to the Kabyle Number Converter Interactive Mode!\n"
        "-----------------------------------------------------------\n"
        "Enter a number or range to convert (e.g., '1203514' or '10-100').\n"
        "Type '-h' or '--help' for usage instructions.\n"
        "Type 'exit', 'quit', or 'q' to end the session.\n"
    )
    print(menu)

def num2words_kabyle(n):
    # Base dictionary for numbers up to 101 and common tens.
    base = {
        0: "sifr", 1: "yiwen", 2: "sin", 3: "tlata", 4: "rebɛa",
        5: "xemsa", 6: "setta", 7: "sebɛa", 8: "tmanya", 9: "ttesɛa",
        10: "ɛecra", 11: "ḥḍac", 12: "tnac", 13: "telṭac", 14: "rbeɛṭac",
        15: "xemsṭac", 16: "seṭṭac", 17: "sbeɛṭac", 18: "tmenṭac", 19: "tseɛṭac",
        20: "ɛecrin", 21: "waḥed u ɛecrin", 22: "tnayen u ɛecrin", 23: "tlata u ɛecrin",
        24: "rebɛa u ɛecrin", 25: "xemsa u ɛecrin", 26: "setta u ɛecrin", 27: "sebɛa u ɛecrin",
        28: "tmanya u ɛecrin", 29: "ttesɛa u ɛecrin", 30: "tlatin", 31: "waḥed u tlatin",
        32: "tnayen u tlatin", 33: "tlata u tlatin", 34: "rebɛa u tlatin", 35: "xemsa u tlatin",
        36: "setta u tlatin", 37: "sebɛa u tlatin", 38: "tmanya u tlatin", 39: "ttesɛa u tlatin",
        40: "rebɛin", 41: "waḥed u rebɛin", 42: "tnayen u rebɛin", 43: "tlata u rebɛin",
        44: "rebɛa u rebɛin", 45: "xemsa u rebɛin", 46: "setta u rebɛin", 47: "sebɛa u rebɛin",
        48: "tmanya u rebɛin", 49: "ttesɛa u rebɛin", 50: "xemsin", 51: "waḥed u xemsin",
        52: "tnayen u xemsin", 53: "tlata u xemsin", 54: "rebɛa u xemsin", 55: "xemsa u xemsin",
        56: "setta u xemsin", 57: "sebɛa u xemsin", 58: "tmanya u xemsin", 59: "ttesɛa u xemsin",
        60: "settic", 61: "waḥed u settic", 62: "tnayen u settic", 63: "tlata u settic",
        64: "rebɛa u settic", 65: "xemsa u settic", 66: "setta u settic", 67: "sebɛa u settic",
        68: "tmanya u settic", 69: "ttesɛa u settic", 70: "sebɛin", 71: "waḥed u sebɛin",
        72: "tnayen u sebɛin", 73: "tlata u sebɛin", 74: "rebɛa u sebɛin", 75: "xemsa u sebɛin",
        76: "setta u sebɛin", 77: "sebɛa u sebɛin", 78: "tmanya u sebɛin", 79: "ttesɛa u sebɛin",
        80: "tmanyin", 81: "waḥed u tmanyin", 82: "tnayen u tmanyin", 83: "tlata u tmanyin",
        84: "rebɛa u tmanyin", 85: "xemsa u tmanyin", 86: "setta u tmanyin", 87: "sebɛa u tmanyin",
        88: "tmanya u tmanyin", 89: "ttesɛa u tmanyin", 90: "tesɛin", 91: "waḥed u tesɛin",
        92: "tnayen u tesɛin", 93: "tlata u tesɛin", 94: "rebɛa u tesɛin", 95: "xemsa u tesɛin",
        96: "setta u tesɛin", 97: "sebɛa u tesɛin", 98: "tmanya u tesɛin", 99: "ttesɛa u tesɛin",
        100: "miyya", 101: "miyya u waḥed"
    }
    if n in base:
        return base[n]
    
    if n < 100:
        tens = (n // 10) * 10
        ones = n % 10
        result = base[tens]
        if ones:
            if ones == 1:
                result += " u waḥed"
            elif ones == 2:
                result += " u tnayen"
            else:
                result += " u " + base[ones]
        return result
    
    hundreds_map = {
        1: "miyya",
        2: "mitin",
        3: "telt-mya",
        4: "rebɛ-mya",
        5: "xems-mya",
        6: "sett-mya",
        7: "sebɛ-mya",
        8: "temn-mya",
        9: "tesɛ-mya"
    }
    if n < 1000:
        h = n // 100
        remainder = n % 100
        word = hundreds_map[h]
        if remainder:
            word += " u " + num2words_kabyle(remainder)
        return word
    
    # Thousands mapping (for n < 1,000,000)
    if n < 1000000:
        t = n // 1000  # thousands part
        remainder = n % 1000
        
        thousands_map = {
            1: "alef",
            2: "alfin",
            3: "telt-alaf",
            4: "rebɛ-alaf",
            5: "xemsa-alaf",
            6: "sett-alaf",
            7: "sebɛ-alaf",
            8: "tmanya-alaf",
            9: "ttesɛa-alaf"
        }
        if t < 10:
            word = thousands_map[t]
        elif t == 10:
            word = "ɛecr-alaf"
        elif t % 100 == 0:
            round_thousands_map = {
                1: "myat-alef",
                2: "mitin-alef",
                3: "telt-myat-alef",
                4: "rebɛ-myat-alef",
                5: "xems-myat-alef",
                6: "sett-myat-alef",
                7: "sebɛ-myat-alef",
                8: "temn-myat-alef",
                9: "tesɛ-myat-alef"
            }
            word = round_thousands_map[t // 100]
        else:
            # For compound thousands that are not round:
            if t < 100:
                word = num2words_kabyle(t) + " n alef"
            else:
                th_hundreds = t - (t % 100)
                th_units = t % 100
                if th_units < 10:
                    word = num2words_kabyle(th_hundreds) + " u " + thousands_map[th_units]
                else:
                    word = num2words_kabyle(t) + " n alef"
        if remainder:
            word += " u " + num2words_kabyle(remainder)
        return word
    
    # Millions mapping (for n < 1,000,000,000)
    if n < 1000000000:
        m = n // 1000000
        remainder = n % 1000000
        # For 1,000,000 use "amelyun", for multiples use numeral + " imelyan"
        if m == 1:
            word = "amelyun"
        else:
            word = num2words_kabyle(m) + " imelyan"
        if remainder:
            word += " u " + num2words_kabyle(remainder)
        return word
    
    # Billions mapping (for n < 1,000,000,000,000)
    if n < 1000000000000:
        b = n // 1000000000
        remainder = n % 1000000000
        if b == 1:
            word = "amelyar"
        else:
            word = num2words_kabyle(b) + " amelyar"
        if remainder:
            word += " u " + num2words_kabyle(remainder)
        return word

    return "Number not supported"

def interactive_mode():
    print_interactive_menu()
    while True:
        user_input = input("Input: ").strip()
        if user_input.lower() in ("exit", "quit", "q"):
            print("Ar tufat!")
            break
        if user_input in ("-h", "--help"):
            print_usage()
            continue
        if not user_input:
            continue
        try:
            if '-' in user_input:
                parts = user_input.split('-')
                if len(parts) != 2:
                    print("Error: Range must be in the format start-end.")
                    continue
                start = int(parts[0])
                end = int(parts[1])
                if start > end:
                    print("Error: Start of range must be less than or equal to end.")
                    continue
                for n in range(start, end + 1):
                    print(f"{n}: {num2words_kabyle(n)}")
            else:
                n = int(user_input)
                print(num2words_kabyle(n))
        except ValueError:
            print("Error: Please enter a valid integer or a range (e.g., 10-100).")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    try:
        # Check if user requested help via command-line
        if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
            print_usage()
            sys.exit(0)
        
        # If command-line argument is provided, handle it.
        if len(sys.argv) > 1:
            arg = sys.argv[1]
            if '-' in arg:
                parts = arg.split('-')
                if len(parts) != 2:
                    print("Error: Range must be in the format start-end.")
                    sys.exit(1)
                try:
                    start = int(parts[0])
                    end = int(parts[1])
                except ValueError:
                    print("Error: Range bounds must be integers.")
                    sys.exit(1)
                if start > end:
                    print("Error: Start of range must be less than or equal to end.")
                    sys.exit(1)
                for n in range(start, end + 1):
                    print(f"{n}: {num2words_kabyle(n)}")
            else:
                try:
                    n = int(arg)
                except ValueError:
                    print("Error: Input must be an integer or a range in the format start-end.")
                    sys.exit(1)
                print(num2words_kabyle(n))
        else:
            # No command-line arguments: enter interactive mode.
            interactive_mode()
    except Exception as e:
        print("Error:", e)
