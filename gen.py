import os

# 获取当前目录下的所有文件夹，排除 .git 文件夹
folders = [f for f in os.listdir('.') if os.path.isdir(f) and f != '.git']

# 生成 Markdown 列表项
content = ""
for folder in folders:
    content += f"- **[{folder}](https://bin-sites.pages.dev/{folder})**\n"

# 将生成的内容写入 index.md 文件
with open('index.md', 'w', encoding='utf-8') as file:
    file.write(content)