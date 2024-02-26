
#Import โมดูล
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno
import csv
import datetime

#กำหนดค่าตัวแปร
i = 3
j = 0 

#กำหนดเวลา
currenttime = datetime.datetime.now()
showtime = datetime.datetime.strftime(currenttime, "%Y-%m-%d %H:%M:%S")

#กำหนดไฟล์
filepath = 'flavor.csv'

#กำหนด List
customlist = [] #List ที่เลือกจากหน้า Add Menu
pricelist = [] #List ราคาแต่ละเมนู
totalpricelist = [] #List ราคารวม
savetotalpricelist = [] #List ใช้สำหรับเก็บข้อมูลบันทึกลงประวัติ
timelist = [] # List เวลา
historylist = [] #List ประวัติข้อมูล

#ฟังก์ชันเรียกหน้าต่าง Add Menu
def create_menulist():
    menulist = Toplevel()
    # menulist.iconbitmap('SSR.ico')
    
    #หน้าต่าง Add Menu
    menulist.title('Swainsense Add Menu')
    
    #ตำแหน่งหน้าต่าง Add Menu และขนาดเล็กที่สุด
    menulist.geometry('200x200+500+100')
    menulist.minsize(500, 180)

    #หน้าต่างเมนู
    icecream = ttk.Label(menulist, text='Select Icecream Flavor')
    icecream.grid(row = 0, column = 0, padx = 10, pady = 10)
    
    #ฟังก์ชันเพิ่มเมนูที่เลือกไปหน้าแรก
    def submitMenu():
        answer = askyesno(title = 'Confirm Add Menu', message = 'Are you sure that you confirm menu?')
        if answer:
            global i, j
            i += 1
            j += 1
            
            #เพิ่ม Order ลง List
            customlist.append([j,
                   icecreamVar.get(), 
                   toppingVar1.get(), 
                   toppingVar2.get(), 
                   toppingVar3.get(),
                   toppingVar4.get(),
                   toppingVar5.get(),
                   toppingVar6.get(),
                   toppingVar7.get()])

            def customlistprint(clp):
                print('{}: {}' .format(clp ,customlist))
            customlistprint('Order')
            
            global iprice, t1price, t2price, t3price, t4price, t5price, t6price, t7price
        
            #วนลูปเช็คข้อมูลใน List
            for y in range(len(customlist)):
            #โปรแกรมคำนวณราคา
                if customlist[y][1] == 'Vanilla' or customlist[y][1] == 'Chocolate': 
                    iprice = 60
                elif customlist[y][1] == 'Chocolate Chip' or customlist[y][1] == 'Cookies&Cream' or customlist[y][1] == 'Lime' or customlist[y][1] == 'Rainbow':
                    iprice = 70
                elif customlist[y][1] == 'Green Tea':
                    iprice = 80
                elif customlist[y][1] == 'Strawberry':
                    iprice = 90
    
                if customlist[y][2] == 'Rainbow Sprinkles':
                    t1price = 10
                elif customlist[y][2] == '':
                    t1price = 0
    
                if customlist[y][3] == 'Chocolate Sprinkles':
                    t2price = 10
                elif customlist[y][3] == '':
                    t2price = 0
        
                if customlist[y][4] == 'Whipped Cream':
                    t3price = 15
                elif customlist[y][4] == '':
                    t3price = 0
        
                if customlist[y][5] == 'Cherry':
                    t4price = 15
                elif customlist[y][5] == '':
                    t4price = 0
        
                if customlist [y][6] == 'M&M':
                    t5price = 10
                elif customlist[y][6] == '':
                    t5price = 0
        
                if customlist [y][7] == 'Chocolate Sauce':
                    t6price = 10
                elif customlist[y][7] == '':
                    t6price = 0
    
                if customlist [y][8] == 'Strawberry Sauce':
                    t7price = 10
                elif customlist[y][8] == '':
                    t7price = 0

                #คำนวณราคาแต่ละเมนู
                sumprice = iprice + t1price + t2price + t3price + t4price + t5price + t6price + t7price 
            
                #รวบรวมราคาแต่ละเมนูเข้า List
                pricelist.append(sumprice)
                def pricelistprint(plp):
                        print('{}: {}' .format(plp ,pricelist))
                pricelistprint('Price')
            
                #ปุ่ม Submit Order
                def calTotal():
                    pricelist.reverse()
                    totalprice = sum(pricelist[0:j])
                    pricelist.reverse()
                    
                    def totalprint(tpc):
                        print('{}: {}' .format(tpc ,totalprice))
                    totalprint('Total Price')
                    
                    totalLabel = Label(root, text = totalprice)
                    totalLabel.grid(row = [i+1], column = 1)
                
                    totalpriceLabel = Label(root, text = 'Total Price:')
                    totalpriceLabel.grid(row = [i+1], column = 0, sticky = E)

                    bahttpLabel = Label(root, text = '฿')
                    bahttpLabel.grid(row = [i+1], column = 2)
                
                    #บันทึกเวลา ราคารวมลง List
                    try:
                        timelist.append(showtime)
                        totalpricelist = ([totalprice])
                        
                        pricelist.reverse()
                        
                        savetotalpricelist = pricelist[0:j]
                        savetotalpricelist.reverse()
                        
                        pricelist.reverse()
                        
                        def timeprint(tp):
                            print('{}: {}' .format(tp ,showtime))
                        timeprint('Date&Time')
                        
                        historylist = [[timelist], [customlist], [savetotalpricelist], [totalpricelist]]
                        
                        #ประวัติใบเสร็จลูกค้า
                        with open('history.txt', 'a', encoding = 'utf-8') as h:
                            hwriter = csv.writer(h, lineterminator = '\n')
                            hwriter.writerows(historylist)      
                    except Exception as e:
                        return print("{}" .format(e))
                
                #โชว์ราคาแต่ละเมนู
                priceLabel = Label(root, text = sumprice)
                priceLabel.grid(row = [i], column = 1)
                bahtLabel = Label(root, text = '฿')
                bahtLabel.grid(row = [i], column = 2)
            
            #โชว์ Order หน้าแรก
            orderList = '{} Icecream Flavor: {} \nTopping: {} {} {} {} {} {} {}'.format(
            [j],
            icecreamVar.get(), 
            toppingVar1.get(), 
            toppingVar2.get(),
            toppingVar3.get(),
            toppingVar4.get(),
            toppingVar5.get(),
            toppingVar6.get(),
            toppingVar7.get()
                )
            orderLabel = Label(root, text = orderList, justify = LEFT)
           
            orderLabel.grid(row = [i], column = 0, sticky = W)
          
            submitButton = ttk.Button(root, text = 'Submit Order', command = calTotal)
            submitButton.grid(row = 0, column = 2, pady = 5)
        else:
            print("You didn't add menu")
    #ดึงข้อมูลรสชาติไอศกรีม จาก CSV (สำรองข้อมูล) 
    try:
        icecreamFile = open(filepath)
        icecreamReader = csv.reader(icecreamFile)
        icecreamData = list(icecreamReader)
        del(icecreamData[0])
        icecreamOption = []
        for x in list(range(0, len(icecreamData))):
            icecreamOption.append(icecreamData[x][0])
        print('Use List from flavor.csv')
    except:
        icecreamOption = ['Vanilla',
                          'Chocolate',
                          'Chocolate Chip',
                          'Cookies&Cream',
                          'Green Tea',
                          'Lime',
                          'Rainbow',
                          'Strawberry',
                          ]
        print('Use List from icecreamOption')
         
    #รสชาติ Icecream
    icecreamVar = StringVar(menulist)
    icecreamVar.set(icecreamOption[0])
    icecreamMenu = ttk.Combobox(menulist, textvariable = icecreamVar)
    icecreamMenu['values'] = icecreamOption
    icecreamMenu['state'] = 'readonly'
    icecreamMenu.config(width = 20)
    icecreamMenu.grid(row = 0, column = 1, pady = 5)
   
    #เช็คลิสท์ Topping
    topping = ttk.Label(menulist, text = 'Add Topping')
    topping.grid(row = 1, column = 0, padx = 5, pady = 5)
    
    toppingVar1 = StringVar(value = '')
    toppingBox1 = ttk.Checkbutton(menulist, 
                               text = 'Rainbow Sprinkles',
                               variable = toppingVar1, 
                               onvalue = 'Rainbow Sprinkles', 
                               offvalue = '', 
                               )
    toppingBox1.grid(row = 1, column = 1, pady = 5, sticky = W)
    
    toppingVar2 = StringVar(value = '')
    toppingBox2 = ttk.Checkbutton(menulist, 
                               text = 'Chocolate Sprinkles',
                               variable = toppingVar2, 
                               onvalue = 'Chocolate Sprinkles', 
                               offvalue = '',
                               )
    toppingBox2.grid(row = 1, column = 2, pady = 5, sticky = W)
    
    toppingVar3 = StringVar(value = '')
    toppingBox3 = ttk.Checkbutton(menulist, 
                               text = 'Whipped Cream',
                               variable = toppingVar3, 
                               onvalue = 'Whipped Cream', 
                               offvalue = '', 
                               )
    toppingBox3.grid(row = 2, column = 1, pady = 5, sticky = W)
    
    toppingVar4 = StringVar(value = '')
    toppingBox4 = ttk.Checkbutton(menulist, 
                               text = 'Cherry',
                               variable = toppingVar4, 
                               onvalue = 'Cherry', 
                               offvalue = '', 
                               )
    toppingBox4.grid(row = 2, column = 2, pady = 5, sticky = W)
    
    toppingVar5 = StringVar()
    toppingBox5 = ttk.Checkbutton(menulist, 
                               text = 'M&M',
                               variable = toppingVar5, 
                               onvalue = 'M&M', 
                               offvalue = '', 
                               )
    toppingBox5.grid(row = 3, column = 1, pady = 5, sticky = W)
    
    toppingVar6 = StringVar()
    toppingBox6 = ttk.Checkbutton(menulist, 
                               text = 'Chocolate Sauce',
                               variable = toppingVar6, 
                               onvalue = 'Chocolate Sauce', 
                               offvalue = '', 
                               )
    toppingBox6.grid(row = 3, column = 2, pady = 5, sticky = W)
    
    toppingVar7 = StringVar()
    toppingBox7 = ttk.Checkbutton(menulist, 
                               text = 'Strawberry Sauce',
                               variable = toppingVar7, 
                               onvalue = 'Strawberry Sauce', 
                               offvalue = '', 
                               )
    toppingBox7.grid(row = 4, column = 1, pady = 5, sticky = W)
    
    #ปุ่ม Submit หน้า Add Menu
    submitmenuButton = ttk.Button(menulist, text = 'Submit Menu', command = submitMenu)
    submitmenuButton.grid(row = 5, column = 1, pady = 5, sticky = W)
    
    #ปุ่ม Close หน้า Add Menu
    closeButton = ttk.Button(menulist, text = 'Close', command = menulist.destroy)
    closeButton.grid(row = 5, column = 2, pady = 5, sticky = W)
    
    menulist.mainloop()

#หน้าต่างหลัก
root = Tk()
root.title('Swainsense')
root.iconbitmap('SSR.ico')

welcome = ttk.Label(root, text = 'Welcome to Swainsense Program')
welcome.grid(row = 0, column = 0, pady = 5, sticky = W)

#ปุ่มเรียกหน้าต่างเมนู
addmenuButton = ttk.Button(root, text = '+ Add Menu',command = create_menulist)
addmenuButton.grid(row = 0, column = 1, pady = 5)

welcome.mainloop()