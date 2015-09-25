"""
This script tests the addons.

You ***SHOULDN'T*** load this on your HexChat. :)
"""

if __name__ == "__main__":
    import os
    import sys
    broken = 0
    for val in os.listdir("addons"):
        try:
            __import__('addons.{0}'.format(val), globals={"__name__": __name__})
            print("{0} = WORKING".format(val))
        except:
            print("{0} = BROKEN".format(val))
            broken = 1
    if broken == 1:
        print("There's broken addons. :(")
        sys.exit(1)
    else:
        print("All is fine. :)")
        sys.exit(0)
