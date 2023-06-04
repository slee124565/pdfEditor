import tkinter as tk
import subprocess

def execute_command():
    item = entry_item.get()
    name = entry_name.get()
    number = entry_number.get()
    # 获取其他输入项的值，可根据实际需要进行处理

    # 执行相应的操作
    print("报销事项:", item)
    print("经费名称:", name)
    print("经费编号:", number)
    # 可在此处添加更多操作

# 创建主窗口
window = tk.Tk()

# 创建第一部分标签和输入框
label_item = tk.Label(window, text="报销事项:")
label_item.grid(row=0, column=0)
entry_item = tk.Entry(window)
entry_item.grid(row=0, column=1)

label_name = tk.Label(window, text="经费名称:")
label_name.grid(row=1, column=0)
entry_name = tk.Entry(window)
entry_name.grid(row=1, column=1)

label_number = tk.Label(window, text="经费编号:")
label_number.grid(row=2, column=0)
entry_number = tk.Entry(window)
entry_number.grid(row=2, column=1)

# 创建第二部分多个输入项
items = [
    "办公费",
    "飞机票",
    "印刷费",
    "邮寄费",
    "车(船)费",
    "材料、试剂费",
    "物业管理费",
    "过路过桥及停车费",
    "图书资料费",
    "水电费",
    "住宿费",
    "版面、检索费",
    "电话费/网络通信费",
    "会议培训费",
    "维修维护费",
    "装订线",
    "公车运行维护费",
    "差旅补助",
    "设备购置费",
    "因公出国党",
    "公务接待费",
    "劳务费",
    "基建工程款",
    "奖助学金",
    "其他(填)"
]

row_start = 3
column_start = 0

column_names = ["类别", "张数", "金额"]

for i, column_name in enumerate(column_names):
    label = tk.Label(window, text=column_name)
    label.grid(row=row_start - 1, column=column_start + i, padx=10)

for i, item in enumerate(items):
    label = tk.Label(window, text=item + ":")
    label.grid(row=row_start + i, column=column_start)
    entry_count = tk.Entry(window)
    entry_count.grid(row=row_start + i, column=column_start + 1)
    entry_amount = tk.Entry(window)
    entry_amount.grid(row=row_start + i, column=column_start + 2)

# 创建按钮
button = tk.Button(window, text="执行指令", command=execute_command)
button.grid(row=row_start + len(items), column=column_start + 1, pady=10, columnspan=2)

# 运行主循环
window.mainloop()
