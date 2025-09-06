from PIL import Image
import os

# Load the sprite sheet
sprite_sheet_path = 'Enemies/Death.png'
sprite_sheet = Image.open(sprite_sheet_path)

# Define frame dimensions (based on visual inspection of the warrior)
frame_width = 150 # Width of each frame
frame_height = 150 # Height of each frame (assuming all frames are the same height)

# Calculate the number of frames
num_frames = sprite_sheet.width // frame_width

# Extract each frame and save as individual images
frame_paths = []
for i in range(num_frames):
    left = i * frame_width
    right = left + frame_width
    frame = sprite_sheet.crop((left, 0, right, frame_height))
    file_name = "../Enemies"
    if not os.path.exists(file_name):
        os.mkdir(file_name)

    frame_path = os.path.join(file_name, f"death_frame_{i}.gif")  # Save each frame as a GIF for turtle compatibility
    frame.save(frame_path, format="GIF")
    frame_paths.append(frame_path)

# img = Image.open('l4r.jpg')
# img.save('l4.gif')