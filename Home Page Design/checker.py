from PIL import Image

def generateCheckerBoard(width, height, color1, color2, cellSize):
    if cellSize == 0:
        print("Cell size must be > 0")
        return
    
    image = Image.new('RGB', (width, height), color1)

    offsetX = (width % cellSize) // 2
    offsetY = (height % cellSize) // 2

    for x in range(width):
        for y in range(height):
            if(((x + offsetX) // cellSize + (y + offsetY) // cellSize) % 2 == 0):
                image.putpixel((x, y), color2)

    image.save("test.png")
    image.show()
    
    return 0


if __name__ == "__main__":
    generateCheckerBoard(1920, 1080, (245, 245, 245), (255, 255, 255), 100)