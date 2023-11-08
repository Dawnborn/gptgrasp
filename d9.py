#%%
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 读取图片
image_path = 'image2.jpg'  # 替换为您的图片路径
img = mpimg.imread(image_path)

# 显示图片
plt.imshow(img)

# 获取图片尺寸
height, width, _ = img.shape

# 绘制九宫格线
# 垂直线
plt.axvline(x=width/3, color='g', linestyle='--')
plt.axvline(x=2*width/3, color='g', linestyle='--')
# 水平线
plt.axhline(y=height/3, color='g', linestyle='--')
plt.axhline(y=2*height/3, color='g', linestyle='--')

# 移除坐标轴
plt.axis('off')

# 显示结果
plt.show()
# %%
