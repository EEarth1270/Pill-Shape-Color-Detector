from func import fed
#
img = fed.load_img('../pillbox_production_images_full_201812/00002-4462-30_B215591A.jpg')
# gray_img= fed.cvt2gray(img)
# mask = fed.create_mask(gray_img)
fed.show_image(img)
