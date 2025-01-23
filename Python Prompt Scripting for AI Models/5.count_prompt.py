# เปิดไฟล์อ่านข้อมูล
with open('genbu.txt', 'r', encoding='utf8') as file:
    lines = file.readlines()

# ตัวนับจำนวน Positive และ Negative
positive_count = 0
negative_count = 0

# วนลูปเพื่อตรวจสอบบรรทัด
for line in lines:
    if line.strip().startswith('positive:'):
        positive_count += 1
    elif line.strip().startswith('negative:'):
        negative_count += 1

# แสดงผลลัพธ์
print(f"จำนวน Positive: {positive_count}")
print(f"จำนวน Negative: {negative_count}")
