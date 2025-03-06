from bs4 import BeautifulSoup as bjir
import os
import requests as rq
# print(dir(bjir))

def clear() :
    os.system("cls")

def task1() :
    with open("index.html", "r") as html_file :
        clear()
        content = html_file.read()
        soup = bjir(content, 'lxml')

        # # Mencari Elemen HTML h5 yang paling awal
        # tag = soup.find('h5')
        # print('==================================================================')
        # print("INI YANG BESERTA TAG HTMLNYA")
        # print(f'Ini adalah tag htmlnya : {tag}\nIni adalah Contentnya : {tag.contents}\nIni adalah Textnya : {tag.text}')
        # print('==================================================================\n')

        # # Mencari Semua Elemen HTML h5 beserta tag html nya
        # tags = soup.find_all('h5')
        # print('==================================================================')
        # print("INI YANG BESERTA TAG HTMLNYA")
        # for i in tags : 
        #     print(i)
        # print('==================================================================\n')

        # # Mencari Semua Elemen HTML h5 hanya content html nya
        # print('==================================================================')
        # print("INI YANG HANYA CONTENT HTMLNYA")
        # for i in tags : 
        #     print(i.text)
        # print('==================================================================\n')

        # Mencari Semua Elemen HTML div dengan nama class "card"
        print('==================================================================')
        print(f"Elemen HTML yang nama class nya card")
        course_card = soup.find_all('div', class_='card')
        for course in course_card :
            course_title = course.h5.text
            course_price = course.a.text.split()[-1]
            print(course.find_all('a', href="#"))
            print(f"\nCourse {course_title} Harganya {course_price}")
            
        print('==================================================================\n')
def task2() :
    clear()
    html_text = rq.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=').text
    soup = bjir(html_text, 'lxml')
    cards = soup.find('ul')
    for card in cards.find_all('li'):
        job_exp = card.find('div', class_='srp-exp')
        job_loc = card.find('div', class_='srp-loc')
        job_sal = card.find('div', class_='srp-sal')
        print(f"Job Experience : {job_exp}\nJob Location   : {job_loc}\nJob Salary     : {job_sal}\n")

    # for card in cards.find_all('li'):
    #     tes = card.find('div', class_='srp-job-bx')
    #     if tes :  # Cek apakah 'srp-job-bx' ditemukan
    #         tess = tes.find('div', class_='clearfix exp-loc')
    #         if tess :  # Cek apakah 'clearfix exp-loc' ditemukan
    #             location = tess.find('div', class_='srp-loc')
    #             experience = tess.find('div', class_='srp-exp')
    #             salary = tess.find('div', class_='srp-sal')

    #             # Gunakan .text.strip() jika ditemukan, jika tidak, ganti dengan "None"
    #             location_text = location.text.strip() if location and location.text.strip() else "None"
    #             experience_text = experience.text.strip() if experience else "None"
    #             salary_text = salary.text.strip() if salary else "None"

    #             print(f"Location: {location_text}\nExperience: {experience_text}\nSalary: {salary_text}\n")
def task3() :
    clear()
    scrapping = rq.get('https://news.detik.com/berita/d-7807995/ketua-kpk-minta-kepala-daerah-kurangi-protokoler-saat-bicara-efisiensi').text
    soup = bjir(scrapping, 'lxml')
    testing = soup.find_all("li", class_="nav__item")
    # print(testing)
    # for i in testing :
    #     anjay = i.find("a").text.strip()
    #     print(anjay)
    # for i in testing:
    #     link = i.find("a")  
    #     if link:  
    #         print(link.text.strip())    
    with open("testing.csv", "w", encoding="utf-8") as f:  # Simpan ke file
        for i in testing:
            link = i.find("a")  
            if link:
                text = link.text.strip()
                print(text)
                f.write(text + "\n")  # Simpan ke file
    

# testing

task3()