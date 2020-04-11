





"""
判断文件图片个数
"""

def count_image(file_list):
    """
    判断一组文件中图片的个数
    :param file_list:文件列表

    :return:图片文件数量
    """
    count = 0
    for file in file_list:
        if file.endswith('png') or file.endswith('jpg') \
            or file.endswith('webp') or file.endswith('bmg'):
             count = count + 1
    return count

#调用函数
img_list = {'1.jpg', '2.png', '3webp', '4.bmp', '5.mp3', '6.wav'}
result = count_image(img_list)
print('一共有', result, '个图片文件')
            
    