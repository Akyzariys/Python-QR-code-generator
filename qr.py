import qrcode
from PIL import Image

def generate_qr():
    print("QR code generator")
    
    data = input("Enter text/link: ").strip()
    if not data:
        print("Error: Please enter text or link.!")
        return
    
    filename = input("Enter a file name (without extension): ").strip() + ".png"
    
    # Настройки QR-кода
    version = int(input("Size (1-40, Enter for auto): ") or 1)
    box_size = int(input("Square size (pixels, Enter=10): ") or 10)
    border = int(input("Frame (pixels, Enter=4): ") or 4)
    fill_color = input("Color of squares (Enter=black): ") or "black"
    back_color = input("Background color (Enter=white): ") or "white"
    
    try:
        qr = qrcode.QRCode(
            version=version,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(filename)
        
        print(f"QR code saved as {filename}")
        img.show()
    except Exception as e:
        print(f"Error: {e}")

generate_qr()
