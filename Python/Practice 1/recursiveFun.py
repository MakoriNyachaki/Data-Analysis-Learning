def main():
    print(printTriangle(6))

def printTriangle(sideLenght):
    if sideLenght < 1:
        return
    print("[]" * sideLenght)
    printTriangle(sideLenght - 1)
    

main()



