import os
from PIL import Image
import pandas as pd

# 数据路径
train_dir = './data/train'

# 保存结果
results = []

# 遍历类别
for class_name in os.listdir(train_dir):

    class_path = os.path.join(train_dir, class_name)

    if not os.path.isdir(class_path):
        continue

    total_images = 0
    broken_images = 0
    broken_files = []

    # 遍历图片
    for filename in os.listdir(class_path):

        file_path = os.path.join(class_path, filename)

        try:
            # 检查图片是否损坏
            with Image.open(file_path) as img:
                img.verify()

            total_images += 1

        except Exception:
            broken_images += 1
            broken_files.append(filename)

    results.append({
        '类别': class_name,
        '图片数量': total_images,
        '损坏图片数量': broken_images
    })

    # 输出损坏文件
    if broken_files:
        print(f'\n[{class_name}] 损坏图片：')

        for f in broken_files:
            print(f'  - {f}')

# 生成表格
df = pd.DataFrame(results)

print('\n===== 数据集统计结果 =====')
print(df)

# 保存 csv
df.to_csv('dataset_statistics.csv', index=False, encoding='utf-8-sig')

print('\n统计表已保存：dataset_statistics.csv')
