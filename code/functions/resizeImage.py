# The purpose of this function is to resize images in a file folder. 
# You will need 3 parameters - a file path to the folder, the length, and width of the files
# Example path: '/Users/wesjurden/Documents/GitHub/Personal/college-football-project/assets/conferences'
# Example length: 2000
# Example width: 1750

def resizeImage(path, length, width):
    # Import packages
    # import PIL
    import os
    import os.path
    from PIL import Image

    f = str(path) # Path to file folder. Converted to string just in case the user did not pass it as a string
    for file in os.listdir(f):
        f_img = f+"/"+file
        img = Image.open(f_img)
        img = img.resize((int(length),int(width))) # Resize image based off of length and width
        img.save(f_img)