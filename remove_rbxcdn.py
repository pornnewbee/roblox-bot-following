# remove_rbxcdn_and_data.py

input_file = "urls.txt"
output_file = "filtered_urls.txt"

with open(input_file, "r") as f:
    lines = f.readlines()

# 去掉换行符，并筛选不包含 .rbxcdn.com 且不以 data: 开头的 URL
filtered = [line.strip() for line in lines if ".rbxcdn.com" not in line and not line.strip().startswith("data:")]

# 写入新文件
with open(output_file, "w") as f:
    for url in filtered:
        f.write(url + "\n")

print(f"完成！过滤后的 URL 已保存到 {output_file}")
