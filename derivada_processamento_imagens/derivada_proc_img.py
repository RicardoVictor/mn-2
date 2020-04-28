import cv2

# Lê a img em escala de cinza
img = cv2.imread('original.png', 0)

# Converte img para escala de cinza
#gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Converte para hsv
#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Adiciona bordas
border = cv2.copyMakeBorder(
    img,
    top=1,
    bottom=1,
    left=1,
    right=1,
    borderType=cv2.BORDER_CONSTANT,
    value=[0, 0, 0]
)

# Cria imagens auxiliares para receber as mascaras
img_dx = border.copy()
img_dy = border.copy()
img_edge_detection = border.copy()
img_box_blurring = border.copy()
img_gaussian_blurring = border.copy()
img_sharpen = border.copy()
img_embossing = border.copy()
img_central = border.copy()

for i in range(1, border.shape[0]-1):
	for j in range(1, border.shape[1]-1):
		
		img_dx[i, j] = border[i, j+1] - border[i, j-1]
		
		img_dy[i, j] = border[i-1, j] - border[i+1, j]
		
		img_edge_detection[i, j] = border[i-1, j] \
						  		 - border[i+1, j] \
						  		 + border[i, j+1] \
						  		 - border[i, j-1]

		img_box_blurring[i, j] = (border[i+1, j] \
							   + border[i-1, j]  \
							   + border[i, j+1]  \
							   + border[i, j-1]) / 4

		img_gaussian_blurring[i, j] = (4*border[i, j]  \
									+ 2*border[i+1, j] \
							   		+ 2*border[i-1, j] \
							   		+ 2*border[i, j+1] \
							   		+ 2*border[i, j-1] \
									+ border[i+1, j+1] \
									+ border[i-1, j-1] \
									+ border[i-1, j+1] \
									+ border[i+1, j-1] ) / 16

		img_sharpen[i, j] = 5*border[i, j] \
						  - border[i+1, j] \
						  - border[i-1, j] \
						  - border[i, j+1] \
						  - border[i, j-1]

		img_embossing[i, j] = border[i-1, j] \
						  	- border[i+1, j] \
						  	- border[i, j+1] \
						  	+ border[i, j-1] \
						  	+ border[i-1, j-1] \
						  	- border[i+1, j+1] \

		img_central[i, j] = (border[i, j+1] - border[i, j-1]) / 2


# Exibe as imagens
#cv2.imshow('img original', img) # em escala de cinza
cv2.imshow('img original (com bordas)', border)
cv2.imshow('img_dx', img_dx)
cv2.imshow('img_dy', img_dy)
cv2.imshow('img_edge_detection', img_edge_detection)
cv2.imshow('img_box_blurring', img_box_blurring)
cv2.imshow('img_gaussian_blurring', img_gaussian_blurring)
cv2.imshow('img_sharpen', img_sharpen)
cv2.imshow('img_embossing', img_embossing)
cv2.imshow('img_central', img_central)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
# Salva as imagens
cv2.imwrite('original_com_bordas.jpg', border)
cv2.imwrite('img_dx.jpg', img_dx)
cv2.imwrite('img_dy.jpg', img_dy)
cv2.imwrite('img_edge_detection.jpg', img_edge_detection)
cv2.imwrite('img_box_blurring.jpg', img_box_blurring)
cv2.imwrite('img_gaussian_blurring.jpg', img_gaussian_blurring)
cv2.imwrite('img_sharpen.jpg', img_sharpen)
cv2.imwrite('img_embossing.jpg', img_embossing)
cv2.imwrite('img_central.jpg', img_central)
'''
