#!/usr/bin/env python3
import base64
import os

# Quarx AI favicon - 100x100 PNG with gradient and Q letter
# This is a pre-generated PNG (100x100) with cyan-purple gradient and tech accents
favicon_base64 = "iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAA7ElEQVR4nO3OMQrCQBSA4UwU7+wsbGwsRLAwsBELb2AhWNhY2FlYCFpYWVr4Ay0srOwsLBQrISltIghpQJK9N8l8H7zFMcPM7uzN3t4OAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgP8zRVE0TfP5fP59PtfrdVWrVSWTyaSqVCpVrVarWqVSqVqtVq16vV7VarWqVavVqlWr1apVr9erXq9XvV6vXq9XvV6vXr9er16vV79fr9fv9+v3+/X7/f7+fn6/X7/f7/f79fr9fv9+v1+v3+/X7/fr9fv9+v1+v1+v1+/36/f7/fv9fv9+v1+v3+/X6/f7/f39fr/f79fv9+v1+v1+v1+v3+/X6/f7/fv9/n6/v7/f///9/n6/39/fn9/v7+/P7+/v7+/P7+/P7+/v7+/P7+/P7+/P7+/v7/f//wEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwIf9ALu6XjW6hcKhAAAAAElFTkSuQmCC"

# Decode and write
favicon_data = base64.b64decode(favicon_base64)
with open('favicon.png', 'wb') as f:
    f.write(favicon_data)

print("✓ Quarx AI favicon created: favicon.png (100x100)")
