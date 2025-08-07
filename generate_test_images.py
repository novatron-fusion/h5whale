import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os
import math

def generate_test_images():
    """Generate a progressing sequence of 5 camera test pattern images"""
    
    # Create output directory if it doesn't exist
    output_dir = "test_images"
    os.makedirs(output_dir, exist_ok=True)
    
    # Image dimensions
    width, height = 800, 600
    
    # Test pattern types
    patterns = [
        "color_bars",
        "checkerboard", 
        "resolution_test",
        "color_gradient",
        "comprehensive_test"
    ]
    
    for i in range(5):
        # Create new image
        img = Image.new('RGB', (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        if patterns[i] == "color_bars":
            # Standard SMPTE color bars
            bar_width = width // 7
            colors = [
                (192, 192, 192),  # White
                (255, 255, 0),    # Yellow
                (0, 255, 255),    # Cyan
                (0, 255, 0),      # Green
                (255, 0, 255),    # Magenta
                (255, 0, 0),      # Red
                (0, 0, 255)       # Blue
            ]
            
            for j, color in enumerate(colors):
                x1 = j * bar_width
                x2 = (j + 1) * bar_width
                draw.rectangle([x1, 0, x2, height * 2 // 3], fill=color)
            
            # Bottom section with smaller bars
            small_bar_width = width // 7
            bottom_colors = [
                (0, 0, 255),      # Blue
                (0, 0, 0),        # Black
                (255, 0, 255),    # Magenta
                (0, 0, 0),        # Black
                (0, 255, 255),    # Cyan
                (0, 0, 0),        # Black
                (192, 192, 192)   # White
            ]
            
            for j, color in enumerate(bottom_colors):
                x1 = j * small_bar_width
                x2 = (j + 1) * small_bar_width
                draw.rectangle([x1, height * 2 // 3, x2, height], fill=color)
        
        elif patterns[i] == "checkerboard":
            # Checkerboard pattern for focus testing
            square_size = 40
            for x in range(0, width, square_size):
                for y in range(0, height, square_size):
                    if (x // square_size + y // square_size) % 2 == 0:
                        color = (255, 255, 255)  # White
                    else:
                        color = (0, 0, 0)        # Black
                    draw.rectangle([x, y, x + square_size, y + square_size], fill=color)
        
        elif patterns[i] == "resolution_test":
            # Resolution test with fine lines
            img_array = np.zeros((height, width, 3), dtype=np.uint8)
            
            # Horizontal frequency sweep
            for y in range(height // 2):
                freq = 1 + (y / (height // 2)) * 20  # Frequency increases with y
                for x in range(width):
                    intensity = int(127.5 * (1 + math.sin(2 * math.pi * freq * x / width)))
                    img_array[y, x] = [intensity, intensity, intensity]
            
            # Vertical frequency sweep  
            for x in range(width):
                freq = 1 + (x / width) * 20  # Frequency increases with x
                for y in range(height // 2, height):
                    intensity = int(127.5 * (1 + math.sin(2 * math.pi * freq * y / height)))
                    img_array[y, x] = [intensity, intensity, intensity]
            
            img = Image.fromarray(img_array)
            draw = ImageDraw.Draw(img)
        
        elif patterns[i] == "color_gradient":
            # RGB color gradients
            img_array = np.zeros((height, width, 3), dtype=np.uint8)
            
            # Red gradient (top third)
            for y in range(height // 3):
                for x in range(width):
                    intensity = int(255 * x / width)
                    img_array[y, x] = [intensity, 0, 0]
            
            # Green gradient (middle third)
            for y in range(height // 3, 2 * height // 3):
                for x in range(width):
                    intensity = int(255 * x / width)
                    img_array[y, x] = [0, intensity, 0]
            
            # Blue gradient (bottom third)
            for y in range(2 * height // 3, height):
                for x in range(width):
                    intensity = int(255 * x / width)
                    img_array[y, x] = [0, 0, intensity]
            
            img = Image.fromarray(img_array)
            draw = ImageDraw.Draw(img)
        
        elif patterns[i] == "comprehensive_test":
            # Comprehensive test pattern
            # White background
            draw.rectangle([0, 0, width, height], fill=(255, 255, 255))
            
            # Central crosshair
            center_x, center_y = width // 2, height // 2
            draw.line([(0, center_y), (width, center_y)], fill=(0, 0, 0), width=2)
            draw.line([(center_x, 0), (center_x, height)], fill=(0, 0, 0), width=2)
            
            # Corner registration marks
            mark_size = 20
            corners = [(0, 0), (width - mark_size, 0), (0, height - mark_size), (width - mark_size, height - mark_size)]
            for x, y in corners:
                draw.rectangle([x, y, x + mark_size, y + mark_size], fill=(255, 0, 0))
            
            # Color patches in corners
            patch_size = 60
            colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
            positions = [(30, 30), (width - 90, 30), (30, height - 90), (width - 90, height - 90)]
            
            for color, (x, y) in zip(colors, positions):
                draw.rectangle([x, y, x + patch_size, y + patch_size], fill=color)
            
            # Concentric circles for focus testing
            for radius in range(50, 200, 30):
                draw.ellipse([center_x - radius, center_y - radius, 
                             center_x + radius, center_y + radius], 
                            outline=(0, 0, 0), width=2)
        
        # Add title and pattern info
        try:
            font = ImageFont.truetype("arial.ttf", 24)
        except:
            font = ImageFont.load_default()
        
        title = f"Camera Test Pattern {i + 1}/5 - {patterns[i].replace('_', ' ').title()}"
        
        # Black background for text
        text_bbox = draw.textbbox((0, 0), title, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = (width - text_width) // 2
        text_y = 10
        
        # Draw text background
        draw.rectangle([text_x - 5, text_y - 2, text_x + text_width + 5, text_y + text_height + 2], 
                      fill=(0, 0, 0))
        draw.text((text_x, text_y), title, fill=(255, 255, 255), font=font)
        
        # Save image
        filename = f"{output_dir}/test_image_{i + 1:02d}.png"
        img.save(filename)
        print(f"Generated: {filename}")
    
    print(f"\nSuccessfully generated 5 test images in the '{output_dir}' directory!")

if __name__ == "__main__":
    generate_test_images()
