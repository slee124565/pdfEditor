from PyPDF2 import PdfReader, PdfWriter
import tkinter as tk
import subprocess

# 创建主窗口
window = tk.Tk()
fields = {}


# def execute_command():
#     item = fill_67.get()
#     name = fill_68.get()
#     number = fill_69.get()
#     # 获取其他输入项的值，可根据实际需要进行处理
#
#     # 执行相应的操作
#     print("报销事项:", item)
#     print("经费名称:", name)
#     print("经费编号:", number)
#     # 可在此处添加更多操作
def execute_command():
    reader = PdfReader("form.pdf")
    writer = PdfWriter()

    page = reader.pages[0]
    # fields = reader.get_fields()
    txt_fields = reader.get_form_text_fields()

    writer.add_page(page)

    for key in txt_fields.keys():
        if key in fields.keys():
            writer.update_page_form_field_values(
                writer.pages[0], {key: f'{key}'}
            )

    # write "output" to PyPDF2-output.pdf
    with open("print.pdf", "wb") as output_stream:
        writer.write(output_stream)

    # input('Press any key to continue ...')
    cmd = 'open print.pdf'
    subprocess.run(cmd.split(' '))


# 创建第一部分标签和输入框
label_item = tk.Label(window, text="报销事项:")
label_item.grid(row=0, column=0)
fill_67 = tk.Entry(window)
fill_67.grid(row=0, column=1)
fields['fill_67'] = fill_67

label_name = tk.Label(window, text="经费名称:")
label_name.grid(row=1, column=0)
fill_68 = tk.Entry(window)
fill_68.grid(row=1, column=1)
fields['fill_68'] = fill_68

label_number = tk.Label(window, text="经费编号:")
label_number.grid(row=2, column=0)
fill_69 = tk.Entry(window)
fill_69.grid(row=2, column=1)
fields['fill_69'] = fill_69

# 创建第二部分多个输入项
items = [
    (1, "办公费"),
    (3, "飞机票"),
    (5, "印刷费"),
    (7, "邮寄费"),
    (9, "车(船)费"),
    (11, "材料、试剂费"),
    (13, "物业管理费"),
    (15, "过路过桥及停车费"),
    (17, "图书资料费"),
    (19, "水电费"),
    (21, "住宿费"),
    (23, "版面、检索费"),
    (25, "电话费/网络通信费"),
    (27, "会议培训费"),
    (29, "维修维护费"),
    (31, "公车运行维护费"),
    (33, "差旅补助"),
    (35, "设备购置费"),
    (37, "因公出国费"),
    (39, "劳务费"),
    (41, "基建工程款"),
    (43, "公务接待费"),
    (44, "奖助学金"),
    # ('47', "其他(填)")
]

row_start = 4
column_start = 0

column_names = ["类别", "张数", "金额"]

for i, column_name in enumerate(column_names):
    label = tk.Label(window, text=column_name)
    label.grid(row=row_start - 1, column=column_start + i, padx=10)

for i, item in enumerate(items):
    fill_index, fill_txt = item
    label = tk.Label(window, text=f"{fill_txt}:")
    label.grid(row=row_start + i, column=column_start)
    entry_count = tk.Entry(window)
    entry_count.grid(row=row_start + i, column=column_start + 1)
    fields[f'fill_{fill_index}'] = entry_count
    entry_amount = tk.Entry(window)
    entry_amount.grid(row=row_start + i, column=column_start + 2)
    fields[f'fill_{fill_index + 1}'] = entry_amount

# 创建按钮
button = tk.Button(window, text="执行指令", command=execute_command)
button.grid(row=row_start + len(items), column=column_start + 1, pady=10, columnspan=2)

# 运行主循环
window.mainloop()
