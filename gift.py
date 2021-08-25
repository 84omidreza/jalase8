import imageio
import os 

images=[]
file = os.listdir("omid")
for i in range(len(file)):
    img= imageio.imread("omid/"+file[i])
    images.append(img)

imageio.mimsave("omid.gif",images)