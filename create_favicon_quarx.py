#!/usr/bin/env python3
"""Create Quarx AI favicon - a modern tech-inspired design"""

from PIL import Image, ImageDraw, ImageFont
import os

# Create a 512x512 image with gradient background (cyan to purple)
size = 512
img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Draw gradient background from cyan to purple
for y in range(size):
    # Gradient: start at cyan (0, 200, 255) to purple (156, 39, 176)
    r = int(156 * (y / size))
    g = int(200 * (1 - y / size))
    b = int(255 * (1 - y / size) + 176 * (y / size))
    draw.line([(0, y), (size, y)], fill=(r, g, b, 255))

# Draw a modern "Q" shape or tech icon
# Let's draw a stylized "Q" with a tech accent
center_x, center_y = size // 2, size // 2
radius = size // 3

# Draw outer circle (white)
draw.ellipse(
    [(center_x - radius, center_y - radius), 
     (center_x + radius, center_y + radius)],
    fill=(255, 255, 255, 255),
    outline=(255, 255, 255, 255)
)

# Draw inner circle (gradient color)
inner_radius = radius - 40
draw.ellipse(
    [(center_x - inner_radius, center_y - inner_radius),
     (center_x + inner_radius, center_y + inner_radius)],
    fill=(156, 39, 176, 255)
)

# Draw accent lines (tech style)
line_color = (0, 200, 255, 255)
draw.line([(center_x - radius - 20, center_y), (center_x + radius + 20, center_y)], 
          fill=line_color, width=8)
draw.line([(center_x, center_y - radius - 20), (center_x, center_y + radius + 20)], 
          fill=line_color, width=8)

# Save as PNG
output_path = os.path.join(os.path.dirname(__file__), 'favicon.png')
img.save(output_path, 'PNG')
print(f"✓ Favicon created: {output_path} (512x512)")

# Create smaller versions for web
sizes = [256, 128, 96, 64, 32, 16]
for s in sizes:
    resized = img.resize((s, s), Image.Resampling.LANCZOS)
    print(f"✓ Created {s}x{s} version")

print("\n✓ Quarx AI favicon ready!")
