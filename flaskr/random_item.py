import pandas as pd
import random

df= pd.read_json('data/seven_data_shaped.json')

def main(cal,item):
    cal_flag = cal / 100 
    cal_flag = int(cal_flag)
    count = 1
    
    print('上限は{0}kcal'.format(cal))
    print('アイテム数'+ str(item))
    
    if item == 1:
        df1 = df.query('カロリーフラグ == @cal_flag-1').reset_index() #ここをDBからSQLでひっぱるコードに変える？
        rnd = random.randrange(len(df1))
        cal = df1['カロリー'][rnd]
        name = df1['商品名'][rnd]
        print(name,cal)
        print('合計カロリー:'+ str(cal) )
    
    elif item == 2:
        num = []
        seg_rnd = random.randrange(1,cal_flag)
        seg1 = seg_rnd
        seg2 = cal_flag - seg_rnd
        
        df1 = df.query('カロリーフラグ == @seg1-1').reset_index()
        df2 = df.query('カロリーフラグ == @seg2-1').reset_index()
        
        for x in range(0,len(df1)):
                num.append(x)
        rnd = random.sample(num, item)

        cal1 = df1['カロリー'][rnd[0]]
        name1 = df1['商品名'][rnd[0]]
        
        cal2 = df2['カロリー'][rnd[1]]
        name2 = df2['商品名'][rnd[1]]
        
        sum = cal1 + cal2
        
        print(seg1,name1,cal1)
        print(seg2,name2,cal2)
        print('合計カロリー:'+ str(sum) )
        
    else:
        tmp = []
        
        if cal_flag == item: #アイテム数＝カロリー上限/100のとき
            num = []
            df1 = df.query('カロリーフラグ == 0').reset_index()
            for x in range(0,len(df1)):
                num.append(x)
            rnd = random.sample(num, item)
            if item == 3:
                print('1',df1['カロリー'][rnd[0]],df1['商品名'][rnd[0]])
                print('1',df1['カロリー'][rnd[1]],df1['商品名'][rnd[1]])
                print('1',df1['カロリー'][rnd[2]],df1['商品名'][rnd[2]])
                sum = df1['カロリー'][rnd[0]] + df1['カロリー'][rnd[1]] + df1['カロリー'][rnd[2]] 
                print('合計カロリー:'+ str(sum) )
            
            elif item == 4:
                print('1',df1['カロリー'][rnd[0]],df1['商品名'][rnd[0]])
                print('1',df1['カロリー'][rnd[1]],df1['商品名'][rnd[1]])
                print('1',df1['カロリー'][rnd[2]],df1['商品名'][rnd[2]])
                print('1',df1['カロリー'][rnd[3]],df1['商品名'][rnd[3]])
                sum = df1['カロリー'][rnd[0]] + df1['カロリー'][rnd[1]] + df1['カロリー'][rnd[2]] + df1['カロリー'][rnd[3]]
                print('合計カロリー:'+ str(sum) )
        
        else:
            while count < item-1:
                seg_rnd = random.randrange(1,cal_flag)
                seg1 = seg_rnd
                seg2 = cal_flag - seg_rnd
                if seg1 < seg2:
                    seg_main = seg1
                    df1 = df.query('カロリーフラグ == @seg_main-1').reset_index()
                    
                    rnd = random.randrange(len(df1))
                    tmp.append(seg_main)
                    tmp.append(df1['カロリー'][rnd])
                    tmp.append(df1['商品名'][rnd])
                    count += 1
                    cal_flag -= seg_main
                
                elif seg1 > seg2:
                    seg_main = seg2
                    df1 = df.query('カロリーフラグ == @seg_main-1').reset_index()
                    
                    rnd = random.randrange(len(df1))
                    tmp.append(seg_main)
                    tmp.append(df1['カロリー'][rnd])
                    tmp.append(df1['商品名'][rnd])
                    count+=1
                    cal_flag -= seg_main

                else:
                    seg_main = seg1
                    df1 = df.query('カロリーフラグ == @seg_main-1').reset_index()
                    
                    rnd = random.randrange(len(df1))
                    tmp.append(seg_main)
                    tmp.append(df1['カロリー'][rnd])
                    tmp.append(df1['商品名'][rnd])
                    count+=1
                    cal_flag -= seg_main

            seg_rnd = random.randrange(1,cal_flag)
            seg1 = seg_rnd
            seg2 = cal_flag - seg_rnd  
            
            df1 = df.query('カロリーフラグ == @seg1-1').reset_index()
            df2 = df.query('カロリーフラグ == @seg2-1').reset_index()
            
            rnd1 = random.randrange(len(df1))
            cal1 = df1['カロリー'][rnd1]
            name1 = df1['商品名'][rnd1]
            
            rnd2 = random.randrange(len(df2))
            cal2 = df2['カロリー'][rnd2]
            name2 = df2['商品名'][rnd2]
            
            tmp.append(seg1)
            tmp.append(cal1)
            tmp.append(name1)
            tmp.append(seg2)
            tmp.append(cal2)
            tmp.append(name2)      
        
            if item == 3:
                print(tmp[0],tmp[1],tmp[2])
                print(tmp[3],tmp[4],tmp[5])
                print(tmp[6],tmp[7],tmp[8])
                sum = tmp[1] + tmp[4] + tmp[7]
                print('合計カロリー:'+ str(sum) )
            if item == 4:
                print(tmp[0],tmp[1],tmp[2])
                print(tmp[3],tmp[4],tmp[5])
                print(tmp[6],tmp[7],tmp[8])
                print(tmp[9],tmp[10],tmp[11])
                sum = tmp[1] + tmp[4] + tmp[7] +tmp[10]
                print('合計カロリー:'+ str(sum) )
    
        
cal_list = [400,500,600,700,800,900,1000]
cal = cal_list[random.randrange(0,7)]
item = random.randrange(3,5)
# main(cal,item)
main(cal,2)