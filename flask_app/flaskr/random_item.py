import pandas as pd
import random
import sqlite3
import numpy as np

# file_sqlite3 = "./seven_data.db"
# con = sqlite3.connect(file_sqlite3)

# df=pd.read_sql_query('SELECT * FROM data', con)

# con.close()

# print(len(df))
# df= pd.read_json('data/seven_data_shaped.json')

def main(cal):
    item = random.randrange(1,4)
    # item = 3
    cal_flag = cal / 100
    cal_flag = int(cal_flag)
    
    use_flag = cal_flag - 1
    use_flag = str(cal_flag)
    
    #ボールの数は5,10,15,20,25,30,35,40,45,50
    ball = [5,10,15,20,25,30,35,40,45,50]
    cal_ball = ball[cal_flag-1]
    count = 1

    file_sqlite3 = "./seven_data.db"
    con = sqlite3.connect(file_sqlite3)
    df=pd.read_sql_query('SELECT * FROM data', con)
    con.close()

    # df['カロリーフラグ'] = df['カロリーフラグ'].astype(np.int64)
    
    print('上限は{0}kcal'.format(cal))
    print('アイテム数'+ str(item))
    # print(df['カロリーフラグ'][0],type(df['カロリーフラグ'][0]))
    
    if item == 1:
        item_list = []
        try:
            df1 = df.query('カロリーフラグ == @use_flag').reset_index() #ここをDBからSQLでひっぱるコードに変える？

            rnd = random.randrange(len(df1))
            cal = df1['カロリー'][rnd]
            name = df1['商品名'][rnd]
            price_sum = df1['税抜き'][rnd]
    
            item_list.append(name)
            item_list.append(cal)
            item_list.append(price_sum)
            return item, item_list, price_sum
        except:
            print('該当なし')
    
    elif item == 2:
        item_list = []
        seg_rnd = random.randrange(1,cal_ball)
        seg1 = seg_rnd
        seg2 = cal_ball - seg_rnd
        
        none = [45,47,49]
        if seg1 in none:
            seg1 -= 1
        if seg2 in none:
            seg2 -= 1
        
        use_seg1 = seg1 - 1
        use_seg1 = str(use_seg1)
        use_seg2 = seg2 - 1
        use_seg2 = str(use_seg2)
        
        df1 = df.query('カロリーフラグ20 == @use_seg1').reset_index()
        df2 = df.query('カロリーフラグ20 == @use_seg2').reset_index()
        
        rnd1 = random.randrange(len(df1))
        cal1 = df1['カロリー'][rnd1]
        name1 = df1['商品名'][rnd1]
        price1 = df1['税抜き'][rnd1]

        item_list.append(name1)
        item_list.append(cal1)
        item_list.append(price1)
        
        rnd2 = random.randrange(len(df2))
        cal2 = df2['カロリー'][rnd2]
        name2 = df2['商品名'][rnd2]
        price2 = df2['税抜き'][rnd2]
        
        price_sum = price1 + price2

        item_list.append(name2)
        item_list.append(cal2)
        item_list.append(price2)

        # print(item_list)
        return item, item_list, price_sum
        
    else:
        item_list = []
        # price_sum = 0
        while count < item-1:
            price_sum = 0
            seg_rnd = random.randrange(1,cal_ball)
            seg1 = seg_rnd
            seg2 = cal_ball - seg_rnd
            if seg1 < seg2:
                seg_main = seg1

                use_main = seg_main - 1
                use_main = str(use_main)

                df1 = df.query('カロリーフラグ20 == @use_main').reset_index()
                
                rnd = random.randrange(len(df1))
                # item_list.append(seg_main)
                item_list.append(df1['商品名'][rnd])
                item_list.append(df1['カロリー'][rnd])
                item_list.append(df1['税抜き'][rnd])
                count += 1
                cal_ball -= seg_main
                price = df1['税抜き'][rnd] 
                price_sum += price
            
            elif seg1 > seg2:
                seg_main = seg2

                use_main = seg_main - 1
                use_main = str(use_main)

                df1 = df.query('カロリーフラグ20 == @use_main').reset_index()
                
                rnd = random.randrange(len(df1))
                # item_list.append(seg_main)
                item_list.append(df1['商品名'][rnd])
                item_list.append(df1['カロリー'][rnd])
                item_list.append(df1['税抜き'][rnd])
                count+=1
                cal_ball -= seg_main
                price = df1['税抜き'][rnd] 
                price_sum += price
                
            else:
                seg_main = seg1

                use_main = seg_main - 1
                use_main = str(use_main)

                df1 = df.query('カロリーフラグ20 == @use_main').reset_index()
                
                rnd = random.randrange(len(df1))
                # item_list.append(seg_main)
                item_list.append(df1['商品名'][rnd])
                item_list.append(df1['カロリー'][rnd])
                item_list.append(df1['税抜き'][rnd])
                count+=1
                cal_ball -= seg_main
                price = df1['税抜き'][rnd] 
                price_sum += price
        
        # print('ループ後price_sum:{0}'.format(price_sum))
                
        seg_rnd = random.randrange(1,cal_ball)
        seg1 = seg_rnd
        seg2 = cal_ball - seg_rnd  
        none = [45,47,49]
        
        if seg1 in none:
            seg1 -= 1
        if seg2 in none:
            seg2 -= 1

        use_seg1 = seg1 - 1
        use_seg1 = str(use_seg1)
        use_seg2 = seg2 - 1
        use_seg2 = str(use_seg2)
        
        df1 = df.query('カロリーフラグ20 == @use_seg1').reset_index()
        df2 = df.query('カロリーフラグ20 == @use_seg2').reset_index()
        # print(seg1,seg2)
        # print(len(df1),len(df2))
        
        rnd1 = random.randrange(len(df1))
        name1 = df1['商品名'][rnd1]
        cal1 = df1['カロリー'][rnd1]
        price1 = df1['税抜き'][rnd1]
        price_sum += price1
        
        rnd2 = random.randrange(len(df2))
        name2 = df2['商品名'][rnd2]
        cal2 = df2['カロリー'][rnd2]
        price2 = df2['税抜き'][rnd2]
        price_sum += price2
        
        # item_list.append(seg1)
        item_list.append(name1)
        item_list.append(cal1)
        item_list.append(price1)
        # item_list.append(seg2)
        item_list.append(name2)
        item_list.append(cal2)
        item_list.append(price2)      
        
        # print(item_list)
        return item, item_list, price_sum
    # print('mainOK')

def result(item,item_list):
    if item == 1:
        name1 = item_list[0]
        cal1 = item_list[1]
        price1 = item_list[2]
        print('商品名:{0}'.format(name1))
        print('カロリー:{0}kcal'.format(cal1))
        print('金額:{0}円'.format(price1))
        print('----------------------')
        print('合計カロリー:{0}kcal'.format(cal1))
        print('合計金額:{0}円'.format(price1))
        
    if item == 2:
        name1 = item_list[0]
        cal1 = item_list[1]
        price1 = item_list[2]
        name2 = item_list[3]
        cal2 = item_list[4]
        price2 = item_list[5]
        print('商品名1:{0}'.format(name1))
        print('カロリー1:{0}kcal'.format(cal1))
        print('金額1:{0}円'.format(price1))
        print('')
        print('商品名2:{0}'.format(name2))
        print('カロリー2:{0}kcal'.format(cal2))
        print('金額2:{0}円'.format(price2))
        cal_sum = cal1 + cal2
        price_sum = price1 + price2
        print('----------------------')
        print('合計カロリー:{0}kcal'.format(cal_sum))
        print('合計金額:{0}円'.format(price_sum))
        
        return price_sum
        
    if item == 3:
        name1 = item_list[0]
        cal1 = item_list[1]
        price1 = item_list[2]
        name2 = item_list[3]
        cal2 = item_list[4]
        price2 = item_list[5]
        name3 = item_list[6]
        cal3 = item_list[7]
        price3 = item_list[8]
        
        print('商品名1:{0}'.format(name1))
        print('カロリー1:{0}kcal'.format(cal1))
        print('金額1:{0}円'.format(price1))
        print('')
        print('商品名2:{0}'.format(name2))
        print('カロリー2:{0}kcal'.format(cal2))
        print('金額2:{0}円'.format(price2))
        print('')
        print('商品名3:{0}'.format(name3))
        print('カロリー3:{0}kcal'.format(cal3))
        print('金額3:{0}円'.format(price3))
        
        cal_sum = cal1 + cal2 + cal3
        price_sum = price1 + price2 + price3
        
        print('----------------------')
        print('合計カロリー:{0}kcal'.format(cal_sum))
        print('合計金額:{0}円'.format(price_sum))
        
        return price_sum

def judge(cal):
    for x in range(5):
        item, item_list,price_sum = main(cal)
        if price_sum < 1000:
            # print('{0}回目で発見'.format(x+1))
            result(item,item_list)
            break
        else:
            pass


cal = int(input('カロリーを入力:'))
judge(cal)