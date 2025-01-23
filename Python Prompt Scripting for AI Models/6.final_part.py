## เปิดไฟล์อ่านข้อมูล
with open('genbu.txt', 'r', encoding='utf8') as file:
    lines = file.readlines()

# แทนที่คำ Positive และ Negative
modified_lines = [line.replace('Positive:', 'positive:').replace('Negative:', 'negative:') for line in lines]

# เขียนเนื้อหาใหม่กลับลงในไฟล์
with open('genbu.txt', 'w', encoding='utf8') as file:
    file.writelines(modified_lines)

print("เปลี่ยน Positive เป็น positive และ Negative เป็น negative เรียบร้อยแล้ว!")