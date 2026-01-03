# remove_rbxcdn.py

input_file = "urls.txt"
output_file = "filtered_urls.txt"

with open(input_file, "r") as f:
    lines = f.readlines()

# 去掉换行符，并筛选不包含 .rbxcdn.com 的 URL
filtered = [line.strip() for line in lines if ".rbxcdn.com" not in line]

# 写入新文件
with open(output_file, "w") as f:
    for url in filtered:
        f.write(url + "\n")

print(f"完成！过滤后的 URL 已保存到 {output_file}")
