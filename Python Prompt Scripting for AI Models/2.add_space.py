# เปิดไฟล์อ่านข้อมูล
with open('genbu.txt', 'r', encoding='utf8') as file:
    lines = file.readlines()

# เพิ่มบรรทัดว่างหลังแต่ละบรรทัด
modified_lines = []
for line in lines:
    modified_lines.append(line)
    modified_lines.append('\n')  # เพิ่มบรรทัดว่าง

# เขียนเนื้อหาใหม่กลับลงในไฟล์
with open('genbu.txt', 'w', encoding='utf8') as file:
    file.writelines(modified_lines)

print("เพิ่มบรรทัดว่างเรียบร้อยแล้ว!")
