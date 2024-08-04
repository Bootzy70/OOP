
# ฟังก์ชั่นหลัก เรียกใช้ฟังก์ชั่นย่อยในการคำนวณ
def generate_tree(max_rows):
    def left_half_tree(max_rows):
        """ lab 2.1 รูปที่ 1 left_half_tree """
        data_tree1 = []
        for i in range(1,max_rows+1):
            data_tree1.append('* ' * i)
       
    def invert_left_half_tree(max_rows):
        """ lab 2.1 รูปที่ 2 invert_left_half_tree """
        data_tree2 = []
        for i in range(max_rows,0,-1):
            data_tree2.append('* '*i)

    def full_tree(max_rows):
        """ lab 2.1 รูปที่ 3 full_tree """
        data_tree3 = []
        for i in range(1, max_rows + 1):
            data_tree3.append(' ' * (max_rows - i) + '* ' * i)

    def inverst_full_tree(max_rows):
        """ lab 2.1 รูปที่ 4 inverst_full_tree """
        data_tree4 = []
        for i in range(max_rows, 0, -1):
            data_tree4.append(' ' * (max_rows - i) + '* ' * i)

    def right_half_tree(max_rows):
        """ lab 2.1 รูปที่ 5 right_half_tree """
        data_tree5 = []
        for i in range(1,max_rows + 1):
            data_tree5.append('  '*(max_rows-i) + '* '*i)

    return data_tree1 , data_tree2, data_tree3, data_tree4, data_tree5
    

max_rows = int(input("Enter max_rows: "))   # กำหนดแถวทั้งหมด
data_tree1, data_tree2, data_tree3, data_tree4, data_tree5 = generate_tree(max_rows)  # กำหนดตัวแปรใช้รับค่าและส่งจำนวนแถวทั้งหมดเข้าฟังก์ชั่น

print("left_half_tree")
print("\n".join(data_tree1))

print("\n Invert_left_half_tree")
print("\n".join(data_tree2))

print("\n Full_Tree")
print("\n".join(data_tree3))

print("\n Inverst_Full_Tree")
print("\n".join(data_tree4))

print("\n right_half_tree")
print("\n".join(data_tree5))



