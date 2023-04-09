int_="変更しないで"
while not type(int_)==int:
    try:
        int_=int(input("数"))
        if int_==0:
            int_=""
            print("0は禁止です")
    except:
        print("int型ではありません")
while not int_==1:
        if not int_%2:
            int_=int_//2
            print(int_)
        else:
            int_=int_*3 + 1
            print(int_)
print(int_)
