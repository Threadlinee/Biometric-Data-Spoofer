from skimage import io, filters

fingerprint_image = io.imread('captured_fingerprint.png')

enhanced_image = filters.gaussian(fingerprint_image, sigma=1)

io.imsave('enhanced_fingerprint.png', enhanced_image)
print("Fingerprint enhanced and saved as 'enhanced_fingerprint.png'")

