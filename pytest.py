"""
This script tests the addons.

You ***SHOULDN'T*** load this on your HexChat. :)
"""

if __name__ == "__main__":
    import os
    import sys
    broken = 0
    for val in os.listdir("addons"):
        print("{0} = TESTING".format(val))
        try:
            __import__('addons.{0}'.format(val), globals={"__name__": __name__})
            print("{0} = WORKING".format(val))
        except Exception as err:
            print("{0} = BROKEN".format(val))
            print(err)
            broken = 1
    if broken == 1:
        print("\nThere's broken addons. :(")
        sys.exit(1)
    else:
        print("\nAll is fine. :)")
        sys.exit(0)
