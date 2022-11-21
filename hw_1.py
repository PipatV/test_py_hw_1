#จำนวนเฉพาะเริ่ม 100-200
for i in range(100,201):

    #สร้างตัวนับ
    count = 0

    #หาตัวมาหาร i
    for j in range(1,i+1):

        #ถ้าหารลงตัวให้บวกค่า
        if i%j ==0:
            count = count+1
    
    #ถ้ามีตัวมันเองกับ 1 ให้แสดงผล
    if count == 2:
        print(i,end=" ")