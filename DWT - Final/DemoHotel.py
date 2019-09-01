from requests import get
from bs4 import BeautifulSoup
import sqlite3
import schedule, time

def job():

    
    conn = sqlite3.connect('tutorial.db')
    c = conn.cursor()

    

    c.execute('DROP TABLE IF EXISTS RESTAURANT_DATA')
    c.execute('CREATE TABLE IF NOT EXISTS RESTAURANT_DATA(Restaurant_id text NOT NULL, Restaurant_Name text NOT NULL, Dish_name text NOT NULL, price text NOT NULL, Details text NOT NULL ,Contact text NOT NULL, Address text NOT NULL, Days_Open text NOT NULL, Opening_time text NOT NULL, Closing_time text NOT NULL)')    

    url1 = 'http://cafeturtle.com/menu/'
    url2 = 'http://theburgerhouse.com/food/'
    url3 = 'http://www.thebaluchi.com/chandigarh/vegeterian-menu.php'

    response1 = get(url1)
    response2 = get(url2)
    response3 = get(url3)

    html_soup1 = BeautifulSoup(response1.text, 'html.parser')
    html_soup2 = BeautifulSoup(response2.text, 'html.parser')
    html_soup3 = BeautifulSoup(response3.text, 'html.parser')

    rname1 = 'Cafe Turtle'
    rname2 = 'The Burger House'
    rname3 = 'Baluchi'

    r_id1 = 'r001'
    r_id2 = 'r002'
    r_id3 = 'r003'

    cnt1 = '+91 11 24655641'
    cnt2 = '+49 89 45209637'
    cnt3 = '+91 82880 33892'

    addr3 = 'Baluchi - A Pan Indian Restaurant, The LaLiT Chandigarh, Rajiv Gandhi IT Park , Near DLF Commercial Complex, Chandigarh, India - 160101'
    addr2 = 'KHAN MARKET, GREATER KAILASH 1 & NIZAMUDDIN EAST NEW DELHI INDIA'
    addr1 = 'Burger House GmbH ,Schellingstr. 36 ,80799 München'

    days1 = 'Mon-Fri'
    days2 = 'Mon-Fri'
    days3 = 'Mon-Fri'

    oTime1 = '9:00 a.m.'
    oTime2 = '9:00 a.m.'
    oTime3 = '9:00 a.m.'

    cTime1 = '5:00 p.m.'
    cTime2 = '5:00 p.m.'
    cTime3 = '5:00 p.m.'

    dish_name = html_soup1.find_all('div', class_ = 'menu-item')
    second_dish_name = html_soup2.find_all('div', class_ = 'd50 food-item')
    third_dish_name = html_soup3.find_all('ul')
    third_dish_name = html_soup3.find_all('span', class_ = 'title-box')
    third_dish_name2 = html_soup3.find_all('li', class_ = 'clearfix')
    third_dish_name3 = html_soup3.find_all('li', class_ = 'text')


#  Extraction of data for the first Resturant

    for i in range(0,55) :
    
        a = dish_name[i]
        m_score2 = a.find('div', class_ = 'menu-item-title').text
        m_score2 = m_score2.strip()
        m_score2 = m_score2.replace('\n', '')

        print (m_score2)

        m_score = a.find('span', class_ = 'menu-item-price-top').text
        m_score = m_score.strip()
        m_score = m_score.replace('\n', '$')
        print (m_score)


        details = a.find('div', class_ = 'menu-item-description').text
        details = details.replace('\r\n\n', '')
        details = details.replace('\r\n', '')
        details = details.replace('\xa0\xa0\xa010.29 \xa0\xa0\xa0', '')
        details = details.strip()

        print (details)
        
        c.execute('INSERT INTO RESTAURANT_DATA (Restaurant_id,Restaurant_name,Dish_name,Price,Details,Contact,Address,Days_Open,Opening_time,Closing_time) values (?,?,?,?,?,?,?,?,?,?)',(r_id1,rname1,m_score2,m_score,details,cnt1,addr1,days1,oTime1,cTime1))
        conn.commit()




#  Extraction of data for the second Resturant

    for i in range(0,36) :
    
        second_hotel = second_dish_name[i]
        name2 = second_hotel.find('h4').text
        name2 = name2.strip()
        name2 = name2.replace('\n', '')

        print (name2)

        price2 = second_hotel.find('span', class_ = 'price').text
        price2 = price2.strip()
        price2 = price2.replace('\n', '')
        print (price2)


        details2 = second_hotel.find('span', class_ = 'ingredients').text
        details2 = details2.replace('\r\n\n', '')
        details2 = details2.replace('\r\n', '')
        details2 = details2.replace('\xa0\xa0\xa010.29 \xa0\xa0\xa0', '')
        details2 = details2.strip()

        print (details2)

       
        c.execute('INSERT INTO RESTAURANT_DATA (Restaurant_id,Restaurant_name,Dish_name,Price,Details,Contact,Address,Days_Open,Opening_time,Closing_time) values (?,?,?,?,?,?,?,?,?,?)',(r_id2,rname2,name2,price2,details2,cnt2,addr2,days2,oTime2,cTime2))
        conn.commit()

#  Extraction of data for the third Resturant

    for i in range(0,61) :
    
        third_hotel = third_dish_name[i]
        third_hotel2 = third_dish_name2[i]
        third_hotel3 = third_dish_name3[i]

        name3 = third_hotel.text
        name3 = name3.strip()
        name3 = name3.replace('\n', '')

        print (name3)

        price3 = third_hotel2.find('span', class_ = 'price').text
        price3 = price3.strip('₹ ')
        price3 = price3.replace('\n', '')

        print (price3)

        details3 = third_hotel3.text
        details3 = details3.replace('\r\n\n', '')
        details3 = details3.replace('\r\n', '')
        details3 = details3.replace('\xa0\xa0\xa010.29 \xa0\xa0\xa0', '')
        details3 = details3.strip()

        print (details3)

        c.execute('INSERT INTO RESTAURANT_DATA (Restaurant_id,Restaurant_name,Dish_name,Price,Details,Contact,Address,Days_Open,Opening_time,Closing_time) values (?,?,?,?,?,?,?,?,?,?)',(r_id3,rname3,name3,price3,details3,cnt3,addr3,days3,oTime3,cTime3))
        conn.commit()

# Update the data after 1 day

    time.sleep(86400)
  

schedule.every(2).seconds.do(job)

while 1:
    schedule.run_pending()

