WhiteText = "\033[37m"
BlackText = "\033[30m"
RedText = "\033[31m"
YellowText = "\033[33m"
BlueText = "\033[34m"


DefaultText = "\033[0m"
BoldText = "\033[1m"

ResetText = BlackText + DefaultText

def PRINT_BLUE(text, info=None, end=None):
    if info is None:
        print(BoldText + BlueText + text + ResetText, end=end)
    else:
        print(BoldText + BlueText + text + ": " + ResetText, end='')
        print(info, end=end)

def PRINT_RED(text, info=None, end=None):
    if info is None:
        print(BoldText + RedText + text + ResetText, end=end)
    else:
        print(BoldText + RedText + text + ": " + ResetText, end='')
        print(info, end=end)

def PRINT_BLACK(text, info=None, end=None):
    if info is None:
        print(BoldText + BlackText + text + ResetText, end=end)
    else:
        print(BoldText + BlackText + text + ": " + ResetText, end='')
        print(info, end=end)

def PRINT_YELLOW(text, info=None, end=None):
    if info is None:
        print(BoldText + YellowText + text + ResetText, end=end)
    else:
        print(BoldText + YellowText + text + ": " + ResetText, end='')
        print(info, end=end)
