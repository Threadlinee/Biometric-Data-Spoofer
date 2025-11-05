from skimage import io, filters

iris_image = io.imread('captured_iris.png')

enhanced_image = filters.median(iris_image)

io.imsave('enhanced_iris.png', enhanced_image)
print("Iris enhanced and saved as 'enhanced_iris.png'")

