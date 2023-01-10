import win32file

### Function extracted from: https://stackoverflow.com/questions/4273252/detect-inserted-usb-on-windows

### GLOBAL VARIABLES ###
props_dict = {}




### FUNCTIONS ###
def init(props):
    global props_dict
    print("Python: starting challenge init()")

    # Save properties in the global variable
    props_dict = props
    
    # Execute the challenge once during the init, so key is calculated from the beginning
    executeChallenge()
    return 0


def locate_usb():
    drive_list = []
    drivebits = win32file.GetLogicalDrives()
    for d in range(1, 26):
        mask = 1 << d
        if drivebits & mask:
            # here if the drive is at least there
            drname = '%c:\\' % chr(ord('A') + d)
            t = win32file.GetDriveType(drname)
            if t == win32file.DRIVE_REMOVABLE:
                drive_list.append(drname)
    return drive_list

def executeChallenge():
    print("Python: starting executeChallenge()")
    medias=locate_usb()
    print(medias)
    key=""
    key='-'.join(medias)
    key = bytes(key, 'utf-8')
    key_size = len(key)

    # The result is a tuple (key, key_size)
    result = (key, key_size)
    print("Python:", result)

    return result


if __name__ == "__main__":
    # Use a dictionary as example of properties obtained from the json
    props_example_dict = {"param1": "hola", "param2": 3}
    init(props_example_dict)
    executeChallenge()








