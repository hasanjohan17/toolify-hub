Add-Type -AssemblyName System.Drawing

# Create a 100x100 PNG with gradient
$bitmap = New-Object System.Drawing.Bitmap(100, 100)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)

# Create gradient brush (Cyan to Purple)
$color1 = [System.Drawing.Color]::FromArgb(0, 212, 212)    # Cyan
$color2 = [System.Drawing.Color]::FromArgb(157, 78, 221)  # Purple
$rect = New-Object System.Drawing.Rectangle(0, 0, 100, 100)
$brush = New-Object System.Drawing.Drawing2D.LinearGradientBrush($rect, $color1, $color2, 45)

# Draw gradient background
$graphics.FillRectangle($brush, $rect)

# Draw circles (atomic structure)
$pen_white = New-Object System.Drawing.Pen([System.Drawing.Color]::White, 1.5)
$graphics.DrawEllipse($pen_white, 18, 18, 64, 64)   # Outer circle

# Draw center circle
$brush_cyan = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(0, 212, 212))
$graphics.FillEllipse($brush_cyan, 35, 35, 30, 30)

# Draw Q text
$font = New-Object System.Drawing.Font("Arial", 32, [System.Drawing.FontStyle]::Bold)
$brush_text = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
$graphics.DrawString("Q", $font, $brush_text, 30, 25)

# Draw small particles
$brush_yellow = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(255, 215, 0))
@(
    @(70, 30),
    @(80, 50),
    @(70, 70),
    @(20, 30),
    @(20, 70),
    @(50, 10),
    @(50, 90),
    @(15, 50)
) | ForEach-Object {
    $graphics.FillEllipse($brush_yellow, $_[0]-2, $_[1]-2, 4, 4)
}

# Save as PNG
$bitmap.Save("favicon.png", [System.Drawing.Imaging.ImageFormat]::Png)
$graphics.Dispose()
$bitmap.Dispose()

Write-Host "✓ Favicon created: favicon.png (100x100 PNG)"
