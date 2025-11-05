import pyfingerprint

f = pyfingerprint.PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

print("Number of templates currently enrolled: " + str(f.getTemplateCount()))

try:
    print("Waiting for finger...")
    while ( f.readImage() == False ):
        pass

    print("Remove finger...")
    time.sleep(2)

    print("Waiting for same finger again...")
    while ( f.readImage() == False ):
        pass

    f.createModel()
    positionNumber = f.storeModel(1)
    print("Finger enrolled successfully!")
    print("New template position #" + str(positionNumber))
except Exception as e:
    print("Operation failed!")
    print("Exception message: " + str(e))

