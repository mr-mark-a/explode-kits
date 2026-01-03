from PIL import Image
import os

def split_card_set(input_path, output_dir, set_name, rows, cols):
    """Split a card set image into individual cards"""
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Open the image
    img = Image.open(input_path)
    img_width, img_height = img.size
    
    print(f"\nProcessing {set_name}:")
    print(f"Image size: {img_width}x{img_height}")
    print(f"Grid layout: {rows} rows x {cols} columns")
    
    # Calculate card dimensions based on grid
    card_width = img_width // cols
    card_height = img_height // rows
    
    print(f"Card size: {card_width}x{card_height}")
    print(f"Total cards: {rows * cols}")
    
    card_num = 1
    
    # Extract each card
    for row in range(rows):
        for col in range(cols):
            # Calculate crop coordinates
            left = col * card_width
            top = row * card_height
            right = left + card_width
            bottom = top + card_height
            
            # Crop the card
            card = img.crop((left, top, right, bottom))
            
            # Save the card
            output_path = os.path.join(output_dir, f"{set_name}_card_{card_num:02d}.jpg")
            card.save(output_path, "JPEG", quality=95)
            print(f"Saved: {set_name}_card_{card_num:02d}.jpg")
            
            card_num += 1
    
    print(f"Completed {set_name}! Extracted {card_num - 1} cards.\n")

# Process both card sets
assets_dir = "d:/marks shortcuts/SOFT/explode-kits/explo-cats/assets"
cards_dir = os.path.join(assets_dir, "cards")

# First card set: 9 cards (3 rows x 3 columns)
split_card_set(
    os.path.join(assets_dir, "cards-set-1.jpg"),
    cards_dir,
    "set1",
    rows=3,
    cols=3
)

# Second card set: 6 cards (3 rows x 2 columns)
split_card_set(
    os.path.join(assets_dir, "cards-set-2.jpg"),
    cards_dir,
    "set2",
    rows=3,
    cols=2
)

print("All cards extracted successfully!")
