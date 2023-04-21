# Defining getImage function
def getImage(path):
    """
    path: full path to computer file
    """
    # This function is created to help read an image file and returns it into a plot. 
    # It takes the argument "path" which is the full file path to the image.
    # Example: '/Users/wesjurden/Documents/GitHub/Personal/college-football-project/assets/conferences/Pac-12.png'
    
    import matplotlib.pyplot as plt
    from matplotlib.offsetbox import OffsetImage

    img = OffsetImage(plt.imread(path), zoom=0.012, alpha = 1) # Adjust zoom to change size
    return img