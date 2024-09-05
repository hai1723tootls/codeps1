import os

def ps1run(payload):
    a = "powershell -e " + base64.b64encode(payload.encode("utf-16")[2:]).decode()
    os.system(a)

ps1run("""
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

# Định nghĩa độ phân giải màn hình
$Screen = [System.Windows.Forms.SystemInformation]::VirtualScreen
$Width = $Screen.Width
$Height = $Screen.Height

# Tạo đối tượng bitmap để lưu ảnh chụp màn hình
$Bitmap = New-Object System.Drawing.Bitmap $Width, $Height
$Graphics = [System.Drawing.Graphics]::FromImage($Bitmap)

# Chụp màn hình
$Graphics.CopyFromScreen($Screen.Left, $Screen.Top, 0, 0, $Bitmap.Size)

# Lưu ảnh dưới dạng PNG
$Bitmap.Save("screenshot.png", [System.Drawing.Imaging.ImageFormat]::Png)

# Giải phóng tài nguyên
$Graphics.Dispose()
$Bitmap.Dispose()
""")
