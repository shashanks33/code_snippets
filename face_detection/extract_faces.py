from mtcnn.mtcnn import MTCNN
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle

def draw_faces(filename, result_list):
    data = plt.imread(filename)
    # plot each face as a subplot
    for i in range(len(result_list)):
    		# get coordinates
    		x1, y1, width, height = result_list[i]['box']
    		x2, y2 = x1 + width, y1 + height
    		# define subplot
    		plt.subplot(1, len(result_list), i+1)
    		plt.axis('off')
    		# plot face
    		plt.imshow(data[y1:y2, x1:x2])
    	# show the plot
    plt.show()
    
filename = 'E:\\Project\\face_detection\\images\\IMG_20200131_005543.jpg'
pixels = plt.imread(filename)
detector = MTCNN()
faces = detector.detect_faces(pixels)

draw_faces(filename, faces)
