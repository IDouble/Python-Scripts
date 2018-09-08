def heximal():
    try:
        x = input("gib Hex ein: ")
        print(int(x,16))
        heximal()
    except:
        print("geht nicht")
        heximal()

heximal()
