from colorhash import ColorHash


def generate_color(seed: int | str) -> str:
    """Generate a random color and return it in hex (#xxxxxx) format."""
    return ColorHash(seed).hex


def generate_avatar_svg(seed: str, size: int = 512, square: bool = False) -> str:
    """Generate an avatar (just a gradient) SVG."""

    color_1 = generate_color(seed)
    color_2 = generate_color(seed[::-1])

    square_svg = f'rect width="{size}" height="{size}"'
    circle_svg = f'circle cx="{size // 2}" cy="{size // 2}" r="{size // 2}"'

    return f"""
<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" fill="none" xmlns="http://www.w3.org/2000/svg">
    <{square_svg if square else circle_svg} fill="url(#gradient)" />
    <defs>
        <linearGradient id="gradient" x1="0" y1="0" x2="{size}" y2="{size}" gradientUnits="userSpaceOnUse">
            <stop stop-color="{color_1}" />
            <stop offset="1" stop-color="{color_2}" />
        </linearGradient>
    </defs>
</svg>
    """
