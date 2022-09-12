from Others.style import Style


def passed():
    return Style.GREEN + "Passed" + Style.WHITE


def failed():
    return Style.RED + "Failed" + Style.WHITE


def main(id, test_name, status):
    test_status = passed() if status else failed()
    print( 'Test Id: ', id, '###, ', test_name, ' is ', test_status)
