#!/usr/bin/env python3
"""Create Quarx AI favicon with modern design"""

import struct
import zlib

def create_png(width, height, filename):
    """Create a simple PNG with gradient and geometric shapes"""
    
    # Create raw image data (RGBA)
    pixels = []
    
    for y in range(height):
        row = []
        for x in range(width):
            # Gradient: cyan to purple
            ratio_y = y / height
            r = int(156 * ratio_y)
            g = int(200 * (1 - ratio_y))
            b = int(255 * (1 - ratio_y) + 176 * ratio_y)
            a = 255
            
            # Draw white circle in center with tech accents
            dx = x - width // 2
            dy = y - height // 2
            dist = (dx**2 + dy**2) ** 0.5
            
            if dist < width // 3:
                # Inner purple circle
                if dist < (width // 3 - 60):
                    r, g, b = 156, 39, 176
                else:
                    # White outer ring
                    r, g, b = 255, 255, 255
            
            # Add tech lines
            if abs(dx) < 10 or abs(dy) < 10:
                if 100 < dist < width // 3:
                    r, g, b = 0, 200, 255
            
            row.extend([r, g, b, a])
        pixels.append(bytes(row))
    
    # PNG header
    png_header = b'\x89PNG\r\n\x1a\n'
    
    # IHDR chunk
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)
    ihdr_crc = zlib.crc32(b'IHDR' + ihdr_data) & 0xffffffff
    ihdr_chunk = struct.pack('>I', 13) + b'IHDR' + ihdr_data + struct.pack('>I', ihdr_crc)
    
    # IDAT chunk
    raw_data = b''
    for row in pixels:
        raw_data += b'\x00' + row  # Filter type 0 for each row
    
    compressed = zlib.compress(raw_data, 9)
    idat_crc = zlib.crc32(b'IDAT' + compressed) & 0xffffffff
    idat_chunk = struct.pack('>I', len(compressed)) + b'IDAT' + compressed + struct.pack('>I', idat_crc)
    
    # IEND chunk
    iend_crc = zlib.crc32(b'IEND') & 0xffffffff
    iend_chunk = struct.pack('>I', 0) + b'IEND' + struct.pack('>I', iend_crc)
    
    # Write PNG
    with open(filename, 'wb') as f:
        f.write(png_header + ihdr_chunk + idat_chunk + iend_chunk)
    
    print(f"✓ PNG favicon created: {filename}")

if __name__ == '__main__':
    create_png(512, 512, 'favicon.png')
    print("✓ Quarx AI favicon ready!")
