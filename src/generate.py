from colorhash import ColorHash

def round(val):
    return int(val) + 1 if ".5" in str(val) else int(val)

def generateColor(string: str):
    length = len(string)
    string1 = string[0:int(round(length/2))]
    string2 = string[int(round(length/2)):length]
    colorOne = ColorHash(string1).hex
    colorTwo = ColorHash(string2).hex
    return [colorOne, colorTwo]

def generateImage(string: str, size: int = 512, square: bool = False):
    colorOne, colorTwo = generateColor(string)
    rect = f'rect height="{size}" width="{size}"'
    circle = f'circle cx="{size / 2}" cy="{size / 2}" r="{size / 2}"'
    Image = f"""
<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <{rect if square else circle} fill="url(#gradient)"/>
  <defs>
    <linearGradient id="gradient" x1="0" y1="0" x2="{size}" y2="{size}" gradientUnits="userSpaceOnUse">
      <stop stop-color="{colorOne}"/>
      <stop offset="1" stop-color="{colorTwo}"/>
    </linearGradient>
  </defs>
</svg>
    """.strip()
    return Image