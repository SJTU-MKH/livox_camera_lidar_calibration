import cv2

# 指定图片路径
image_path = 'corrected.jpg'

# 读取图片
image = cv2.imread(image_path)

# 检查图片是否成功加载
if image is None:
    print(f"无法加载图片: {image_path}")
else:
    # 显示图片
    cv2.imshow('Image', image)

    # 等待用户按下任意键
    cv2.waitKey(0)

    # 关闭所有窗口
    cv2.destroyAllWindows()

