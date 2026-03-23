#!/usr/bin/env python3
"""Create a modern Quarx AI favicon with atomic/quantum design"""

from PIL import Image, ImageDraw, ImageFont
import math

# Create a 256x256 image
size = 256
image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(image)

# Create gradient background (teal to purple)
for y in range(size):
    # Gradient from teal (#00D4D4) to purple (#9D4EDD)
    r = int(0 + (157 - 0) * (y / size))  # 0 to 157
    g = int(212 + (78 - 212) * (y / size))  # 212 to 78
    b = int(212 + (221 - 212) * (y / size))  # 212 to 221
    draw.rectangle([(0, y), (size, y+1)], fill=(r, g, b, 255))

# Draw atomic orbits (rings) representing quantum/atomic nature
center = (size // 2, size // 2)
orbit_colors = [
    (255, 255, 255, 80),   # White, semi-transparent
    (200, 255, 255, 60),   # Cyan, semi-transparent
]

# Draw 3 orbital rings
for i, (radius, color) in enumerate([(40, orbit_colors[0]), (60, orbit_colors[1]), (45, orbit_colors[0])]):
    draw.ellipse([
        (center[0] - radius, center[1] - radius),
        (center[0] + radius, center[1] + radius)
    ], outline=color, width=2)

# Draw nucleus electrons (small circles on orbits)
num_electrons = 9
for i in range(num_electrons):
    angle = (i / num_electrons) * 2 * math.pi
    orbit_radius = 50
    x = center[0] + orbit_radius * math.cos(angle)
    y = center[1] + orbit_radius * math.sin(angle)
    electron_size = 3
    draw.ellipse([
        (x - electron_size, y - electron_size),
        (x + electron_size, y + electron_size)
    ], fill=(255, 255, 255, 200))

# Draw central nucleus with "Q"
nucleus_radius = 35
# Nucleus background circle (bright cyan)
draw.ellipse([
    (center[0] - nucleus_radius, center[1] - nucleus_radius),
    (center[0] + nucleus_radius, center[1] + nucleus_radius)
], fill=(0, 212, 212, 255))

# Add some depth with a darker ring
draw.ellipse([
    (center[0] - nucleus_radius, center[1] - nucleus_radius),
    (center[0] + nucleus_radius, center[1] + nucleus_radius)
], outline=(157, 78, 221, 200), width=3)

# Draw "Q" letter in the center
try:
    # Try to use a bold font
    font = ImageFont.truetype("/Windows/Fonts/arial.ttf", 80)
except:
    # Fallback to default font
    font = ImageFont.load_default()

text = "Q"
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
text_x = center[0] - text_width // 2
text_y = center[1] - text_height // 2
draw.text((text_x, text_y), text, fill=(255, 255, 255, 255), font=font)

# Add some subtle glow effect by drawing semi-transparent circles
glow_radius = nucleus_radius + 5
draw.ellipse([
    (center[0] - glow_radius, center[1] - glow_radius),
    (center[0] + glow_radius, center[1] + glow_radius)
], outline=(200, 255, 255, 40), width=2)

# Resize and save in multiple formats
# Save as PNG (256x256)
image.save('favicon.png', 'PNG')
print("✓ Created favicon.png (256x256)")

# Also create smaller versions for better performance
for size_px in [128, 96, 64, 48, 32, 16]:
    small_image = image.resize((size_px, size_px), Image.Resampling.LANCZOS)
    small_image.save(f'favicon-{size_px}.png', 'PNG')
    print(f"✓ Created favicon-{size_px}.png")

# Create ICO format (for Windows)
try:
    ico_image = image.resize((64, 64), Image.Resampling.LANCZOS)
    ico_image.save('favicon.ico', 'ICO')
    print("✓ Created favicon.ico")
except Exception as e:
    print(f"⚠ Could not create ICO: {e}")

print("\n✅ Quarx AI favicon created successfully!")
print("Files created:")
print("  - favicon.png (primary, 256x256)")
print("  - favicon-128.png, favicon-96.png, favicon-64.png, etc.")
print("  - favicon.ico (Windows shortcut)")
