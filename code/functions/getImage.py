# Defining getImage function
def getImage(path):
    # This function is created to help read an image file and returns it into a plot. 
    # It takes the argument "path" which is the full file path to the image.
    # Example: '/Users/wesjurden/Documents/GitHub/Personal/college-football-project/assets/conferences/Pac-12.png'
    
    import matplotlib.pyplot as plt
    from matplotlib.offsetbox import OffsetImage
    return OffsetImage(plt.imread(path), zoom=.012, alpha = 1) # Adjust zoom to change size