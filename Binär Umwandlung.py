def binaer():
    try:
        x = input("gib Binär ein: ")
        print(int(x,2))
        binaer()
    except:
        print("geht nicht")
        binaer()

binaer()
