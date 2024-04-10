import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load the images
img1 = cv2.imread('images/img1.jpg')
img2 = cv2.imread('images/img2.jpg')

# Convert the images to RGB
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# Create a figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

# Display the images
ax1.imshow(img1)
ax2.imshow(img2)

# Create a list to store the points
points1 = []
points2 = []

# Create a function to collect the points
def collect_points(event, ax, points):
    if event.inaxes != ax:
        return

    # Get the x and y coordinates
    x = event.xdata
    y = event.ydata

    # Append the points
    points.append([x, y])

    # Plot the points
    ax.plot(x, y, 'ro')
    plt.draw()

# Connect the event. Make sure that select the points in the same order
cid1 = fig.canvas.mpl_connect('button_press_event', lambda event: collect_points(event, ax1, points1))
cid2 = fig.canvas.mpl_connect('button_press_event', lambda event: collect_points(event, ax2, points2))

# Show the plot
plt.show()

# Disconnect the event
fig.canvas.mpl_disconnect(cid1)
fig.canvas.mpl_disconnect(cid2)

# Save the points
np.save('points/img1.npy', np.array(points1))
np.save('points/img2.npy', np.array(points2))