import tkinter as tk
import random

def call_name_mode1():
    students = ["周昕妤", "尤佳媛", "沈书秋", "王佳祺", "蔡辰熙", "朱婧妤", "王馨瑶", "吴杨悦", "许昕妤", "蒋乐伊", "武知音", "黄雨轩", "任安娜", "罗雯瑶", "周一诺", "黄瑞佳", "周玥", "喻文萱", "沈芸", "邵子轩", "何可人", "金宋洋", "何若松", "周梅昂", "鞠辰", "吴昊", "徐何俊贤", "富一言", "周昱辰", "朱昱帆", "凌安", "杨栩昊", "朱皓宇", "蒋昊洋", "刘恒卓", "王亦宸", "潘博文", "冯泽州", "潘翌", "常景亮", "骆佳俊", "夏一铭", "戴乐凡", "周宇鑫", "喻俊杰", "范家齐", "王田亮", "喻韦杰"]
    selected_students = random.sample(students, 4)
    result_label.config(text=f"被点名的同学是（答题）：{', '.join(selected_students)}")

def call_name_mode2():
    students = ["周昕妤", "尤佳媛", "沈书秋", "王佳祺", "蔡辰熙", "朱婧妤", "王馨瑶", "吴杨悦", "许昕妤", "蒋乐伊", "武知音", "黄雨轩", "任安娜", "罗雯瑶", "周一诺", "黄瑞佳", "周玥", "喻文萱", "沈芸", "邵子轩", "何可人", "金宋洋", "何若松", "周梅昂", "鞠辰", "吴昊", "徐何俊贤", "富一言", "周昱辰", "朱昱帆", "凌安", "杨栩昊", "朱皓宇", "蒋昊洋", "刘恒卓", "王亦宸", "潘博文", "冯泽州", "潘翌", "常景亮", "骆佳俊", "夏一铭", "戴乐凡", "周宇鑫", "喻俊杰", "范家齐", "王田亮", "喻韦杰"]
    answerers = random.sample(students, 4)
    others = [student for student in students if student not in answerers]
    if len(others) >= 4:
        graders = random.sample(others, 4)
        result_label.config(text=f"被点名的同学是（答题）：{', '.join(answerers)}；（批题）：{', '.join(graders)}")
    else:
        graders = others
        result_label.config(text=f"被点名的同学是（答题）：{', '.join(answerers)}；（批题）：{', '.join(graders)}。由于人数不足，批题人数小于4人。")

def call_name_mode3():
    num_students = int(entry.get())
    students = ["周昕妤", "尤佳媛", "沈书秋", "王佳祺", "蔡辰熙", "朱婧妤", "王馨瑶", "吴杨悦", "许昕妤", "蒋乐伊", "武知音", "黄雨轩", "任安娜", "罗雯瑶", "周一诺", "黄瑞佳", "周玥", "喻文萱", "沈芸", "邵子轩", "何可人", "金宋洋", "何若松", "周梅昂", "鞠辰", "吴昊", "徐何俊贤", "富一言", "周昱辰", "朱昱帆", "凌安", "杨栩昊", "朱皓宇", "蒋昊洋", "刘恒卓", "王亦宸", "潘博文", "冯泽州", "潘翌", "常景亮", "骆佳俊", "夏一铭", "戴乐凡", "周宇鑫", "喻俊杰", "范家齐", "王田亮", "喻韦杰"]
    selected_students = random.sample(students, min(num_students, len(students)))
    result_label.config(text=f"被点名的同学是：{', '.join(selected_students)}")

root = tk.Tk()
root.title("课堂随机点名系统")

# 标题及作用说明
title_label = tk.Label(root, text="课堂随机点名系统", font=("Helvetica", 16))
title_label.pack()
description_label = tk.Label(root, text="这个系统用于在课堂上随机点名学生回答问题或参与其他活动，提供了多种点名模式以满足不同的教学需求。")
description_label.pack()

# 按钮一（模式一）
button1 = tk.Button(root, text="模式一（抽选4人答题）", command=call_name_mode1)
button1.pack()

# 按钮二（模式二）
button2 = tk.Button(root, text="模式二（抽选4人答题，四人批题）", command=call_name_mode2)
button2.pack()

# 模式三输入框和按钮
entry_label = tk.Label(root, text="请输入人数：")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()
button3 = tk.Button(root, text="模式三（自定义人数答题）", command=call_name_mode3)
button3.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()