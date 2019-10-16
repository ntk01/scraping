import scrape
import describe


def test_scrape():
    keys, values = scrape.get_co_occur("test")
    try:
        (len(keys) == 10) and (len(values) == 10)
        print("OK")
    except ValueError:
        print("Unexpected error")


def test_describe():
    keys, values = describe.get_word("test")
    try:
        (len(keys) == 10) and (len(values) == 10)
        print("OK")
    except ValueError:
        print("Unexpected error")
