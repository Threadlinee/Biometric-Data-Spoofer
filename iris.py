from iris_recognition import IrisRecognizer

iris_recognizer = IrisRecognizer()

iris_image = iris_recognizer.capture_iris()

iris_recognizer.save_iris_image(iris_image, 'captured_iris.png')
print("Iris captured and saved as 'captured_iris.png'")