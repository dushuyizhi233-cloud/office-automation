from PIL import Image
import os
from tkinter import Tk, Label, Button, StringVar, filedialog, Frame, Entry
from natsort import natsorted, natsort_keygen

def combine_images():
    # 获取文件夹路径
    folder_path = filedialog.askdirectory()

    # 获取文件夹中所有的.jpg文件，并按文件名称自然数顺序排序
    image_files = natsorted([img for img in os.listdir(folder_path) if img.endswith(".jpg")], key=natsort_keygen())

    # 打开并存储排序后的图片
    images = [Image.open(os.path.join(folder_path, img)) for img in image_files]

    # 创建子窗口
    sub_window = Tk()
    sub_window.title("输入行列数")
    sub_window.geometry("200x150")

    def get_row_column():
        # 获取行数和列数的输入值
        num_rows = int(row_entry.get())
        num_columns = int(column_entry.get())
        sub_window.destroy()

        # 计算拼接图像的大小。我们假设所有的图片都有相同的大小。
        image_width = images[0].size[0]
        image_height = images[0].size[1]
        num_images = len(images)

        # 计算新图像的宽度和高度
        new_img_width = num_columns * image_width
        new_img_height = num_rows * image_height

        # 创建一个新的空白图像
        new_img = Image.new('RGB', (new_img_width, new_img_height))

        # 在新图像上添加每个图片
        for i, img in enumerate(images):
            x = i % num_columns * image_width
            y = i // num_columns * image_height
            new_img.paste(img, (x, y))

        # 保存新图像
        new_img.save(os.path.join(folder_path, "combined.jpg"))

        # 更新标签文字
        result_string.set("图片合成完成，保存在" + os.path.join(folder_path, "combined.jpg") +
                          "\n行数: " + str(num_rows) + ", 列数: " + str(num_columns))

    row_label = Label(sub_window, text="行数：")
    row_label.pack()

    row_entry = Entry(sub_window)
    row_entry.pack()

    column_label = Label(sub_window, text="列数：")
    column_label.pack()

    column_entry = Entry(sub_window)
    column_entry.pack()

    confirm_button = Button(sub_window, text="确定", command=get_row_column)
    confirm_button.pack()

    sub_window.mainloop()

def close_program():
    root.quit()

# 创建主窗口
root = Tk()

# 设置窗口标题和大小
root.title("图片拼接工具")
root.geometry("400x200")

# 创建并放置标签和按钮
frame = Frame(root)
frame.pack(padx=10, pady=10)

combine_button = Button(frame, text="选择文件夹并生成大图", command=combine_images)
combine_button.pack(fill='x', pady=5)

close_button = Button(frame, text="关闭程序", command=close_program)
close_button.pack(fill='x', pady=5)

result_string = StringVar()
result_label = Label(frame, textvariable=result_string)
result_label.pack(pady=10)

# 运行主循环
root.mainloop()
