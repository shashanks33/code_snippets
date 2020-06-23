from mtcnn.mtcnn import MTCNN
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle

def draw_image_with_boxes(filename, result_list):
    data = plt.imread(filename)
    plt.imshow(data)

    ax = plt.gca()

    for result in result_list:
        x, y, width, height = result['box']
        rect = Rectangle((x, y), width, height, fill=False, color='red')
        ax.add_patch(rect)

        for key, value in result['keypoints'].items():
            dot = Circle(value, radius = 2, color='red')
            ax.add_patch(dot)
    plt.show()


filename = 'E:\\Project\\face_detection\\images\\IMG_20200131_005543.jpg'
pixels = plt.imread(filename)
detector = MTCNN()
faces = detector.detect_faces(pixels)

draw_image_with_boxes(filename, faces)
