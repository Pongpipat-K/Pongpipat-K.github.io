# เปิดไฟล์อ่านข้อมูล
with open('genbu.txt', 'r', encoding='utf8') as file:
    lines = file.readlines()

# ลบบรรทัดว่างที่อยู่ถัดจาก "------"
modified_lines = []
skip_next_blank = False
for line in lines:
    if skip_next_blank and line.strip() == '':
        # ข้ามบรรทัดว่าง
        skip_next_blank = False
        continue
    modified_lines.append(line)
    if line.strip() == '---':
        # เจอบรรทัด ------ แล้วข้ามบรรทัดว่างถัดไป
        skip_next_blank = True

# เขียนเนื้อหาใหม่กลับลงในไฟล์
with open('genbu.txt', 'w', encoding='utf8') as file:
    file.writelines(modified_lines)

print("บรรทัดว่างถัดจาก ------ ถูกลบเรียบร้อยแล้ว!")
