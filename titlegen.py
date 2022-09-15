from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Open an Image
img = Image.open('model7_phase_0.png')
 
# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

myFont = ImageFont.truetype('arial.ttf', 30)

# Add Text to an image
I1.text((20, 30), "Phase 1", font=myFont, fill=(0,0,0))
 
# Display edited image
img.show()
 
# Save the edited image
img.save("car2.png")