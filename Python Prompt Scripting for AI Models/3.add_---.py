# เปิดไฟล์อ่านข้อมูล
with open('genbu.txt', 'r', encoding='utf8') as file:
    lines = file.readlines()

# สร้างเนื้อหาใหม่ที่มีการเติม "------" หลังบรรทัด Negative
modified_lines = []
for line in lines:
    modified_lines.append(line)
    if line.strip().startswith('negative:'):
        modified_lines.append('---\n')  # เพิ่มบรรทัด ------ หลังจาก Negative:

# เขียนเนื้อหาใหม่กลับลงในไฟล์
with open('genbu.txt', 'w', encoding='utf8') as file:
    file.writelines(modified_lines)

print("ไฟล์ถูกแก้ไขเรียบร้อยแล้ว!")
