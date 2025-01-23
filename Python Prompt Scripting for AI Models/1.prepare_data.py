# เปิดไฟล์อ่านข้อมูล
with open('genbu.txt', 'r', encoding='utf8') as file:
    lines = file.readlines()

# เก็บเฉพาะบรรทัดที่ขึ้นต้นด้วย Positive หรือ Negative
filtered_lines = [line for line in lines if line.strip().startswith('positive:') or line.strip().startswith('negative:')]

# เขียนเนื้อหาใหม่กลับลงในไฟล์
with open('genbu.txt', 'w', encoding='utf8') as file:
    file.writelines(filtered_lines)

print("บรรทัดที่ไม่ขึ้นต้นด้วย Positive หรือ Negative ถูกลบเรียบร้อยแล้ว!")
