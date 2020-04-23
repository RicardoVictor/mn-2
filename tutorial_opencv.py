### Tutorial ###

import cv2

cv2.imshow('Imagem', imagem)
cv2.waitKey(0) # espera indefinidamente
cv2.destroyAllWindows()

# representacao dos pixels: (y, x)

print(imagem.shape) # (y, x, representacao de cor(BGR))
print(
	imagem.item(0, 0, 2), # R
	imagem.item(0, 0, 1), # G
	imagem.item(0, 0, 0)  # B
)

imagem.itemset(
	(0, 0, 2), # pixel pos (0, 0), canal R
	255
)

imagem.itemset(
	(0, 0, 1), # pixel pos (0, 0), canal G
	0
)

imagem.itemset(
	(0, 0, 0), # pixel pos (0, 0), canal B
	0
)

cv2.imwrite('imagem2.jpg', imagem)

sub_imagem = imagem[100:200, 100:200]
cv2.imwrite('sub_imagem.jpg', sub_imagem)

# modificando a imagem
imagem[250:350, 250:350] = sub_imagem
