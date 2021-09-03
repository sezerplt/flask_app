
from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template,request
import soupsieve as sv



app=Flask(__name__)




@app.route('/' ,methods=["GET","POST"])
def filter():
    #&address_city=35 sözlük olarak sehirlerin plaklarını gönder
    #https://www.sahibinden.com/kategori-vitrin?viewType=Gallery&price_min=500000&category=3517&price_max=100000&address_city=35
    cty_list=["İstanbul","İzmir",
    "Ankara","Adana","Adıyaman","Afyonkarahisar","Ağrı","Aksaray","Amasya","Antalya",
     "Ardahan","Artvin","Aydın","Balıkesir","Bartın","Batman","Bayburt",
     "Bilecik","Bingöl","Bitlis","Bolu","Burdur","Bursa","Çanakkale","Çankırı","Çorum","Denizli","Diyarbakır",
     "Düzce","Edirne","Elazığ","Erzincan","Erzurum","Eskişehir","Gaziantep",
     "Giresun","Gümüşhane","Hakkâri","Hatay","Iğdır","Isparta","Kahramanmaraş","Karabük",
     "Karaman","Kars","Kastamonu","Kayseri","Kırıkkale","Kırıklareli","Kırşehir","Kilis","Kocaeli","Konya","Kütahya",
     "Malatya","Manisa","Mardin","Mersin","Muğla","Muş","Nevşehir","Niğde","Ordu","Osmaniye",
     "Rize","Sakarya","Samsun","Siirt","Sinop","Sivas","Şanlıurfa","Şırnak","Tekirdağ","Tokat",
     "Trabzon","Tunceli","Uşak","Van","Yalova","Yozgat","Zonguldak"]
    checkbox_value=["34","35",
    "06","01","02","03","04","68","05","07",
     "75","08","09","10","74","	72","69",
     "11","12","13","14","15","16","17","18","19","20","21",
     "81","22","23","24","25","26","27",
     "28","29","30","31","76","32","46","78",
     "70","36","37","38","71","39","40","79","41","42","43",
     "44","45","47","33","48","49","50","51","52","80",
     "53","54","55","56","57","58","63","73","59","60",
     "61","62","64","65","77","66","67"]
    coordinate={"34":["41.00823760000001","28.97835889999999"],"35":["38.42373400000001","27.142825999999992"],
    "06":["39.933363499999984","32.85974189999999"],"01":["37.26123150000002","35.390504600000014"],"02":["37.9078291","38.48499230000001"],
    "03":["38.7568852","30.538703800000018"],"04":["39.6269218","43.021596500000015"],
    "68":["38.335204299999994","33.97500180000002"],"05":["40.6516608","35.9037966"],
    "07":["36.896890799999994","30.713323299999978"],"75":["36.896890799999994","30.713323299999978"],
    "08":["41.078663999999996","41.76282230000002"],"09":["37.8117033","28.48639629999998"],"10":["39.653297599999995","27.890342300000004"],
    "74":["41.58105090000002","32.4609794"],"72":["37.8362496","41.36057390000001"],"69":["40.33175549999999","40.14378629999999"],
    "11":["40.0566555","30.066523600000004"],"12":["39.06263540000002","40.76960950000001"],"13":["38.65231330000002","42.4202028"],
    "14":["40.575976600000004","31.578808599999995"],"15":["37.46126690000001","30.066523600000004"],"16":["40.18852809999997","29.0609636"],
    "17":["40.05101040000002","26.98524220000002"],"18":["40.536907299999996","33.58838930000001"],"19":["40.49982110000003","34.59862629999998"],
    "20":["37.61283949999999","29.23207839999999"],"21":["37.92497330000002","40.2109826"],"81":["40.877053100000005","31.319271300000004"],
    "22":["41.151722199999966","26.513796400000018"],"23":["38.49648039999999","39.21990289999998"],"24":["39.768191400000006","39.0501306"],
    "25":["39.90549930000002","41.26582359999999"],"26":["39.76670609999999","30.525631099999995"],"27":["37.065953000000015","37.378110000000014"],
    "28":["40.64616720000002","38.593551099999985"],"29":["40.28036729999998","39.314325300000014"],"30":["37.57742700000001","43.736781999999984"],
    "31":["36.40184880000001","36.34980970000001"],"76":["39.887984100000004","44.00483650000002"],"32":["38.02114640000002","31.079370500000007"],
    "46":["37.57527550000001","36.92282230000001 "],"78":["41.18748900000001","32.741741900000015"],
    "70":["37.2436336&","33.61757699999998"],"36":["40.280763599999986","42.9919527"],"37":["",""],
     "38":["38.720488999999986","35.48259700000003"],"71":["39.88768779999999","33.75552480000001"],"39":["41.725979499999994","27.483838999999985"],
     "40":["39.22689050000001","33.97500180000002"],"79":["36.82047749999999","37.16873389999998"],"41":["40.8532704","29.881520299999995"],
     "42":["37.874642900000005","32.493155399999985"],"43":["39.358137000000006","29.603549499999993"],
     "44":["38.3553627","38.33352470000001"],"45":["38.84193729999999","28.112267900000017"],"47":["37.57527550000001","36.92282230000001"],
     "33":["36.812085800000006","34.641475000000014"],"48":["37.1835819","28.48639629999998"],"49":["38.946188799999995","41.753893099999985"],
     "50":["38.6939399","34.685650899999985"],"51":["38.0993086","34.685650899999985"],
     "52":["40.79905800000002","37.389900500000024"],"80":["37.21302580000001","36.176261499999995"],"53":["41.02551100000003","40.517666"],
     "54":["40.77307429999999","30.3948169"],"55":["41.2797031","36.336066699999996"],"56":["37.90763854059878","41.940712065625"],
     "57":["41.5594749","34.858053199999986"],
     "58":["39.44880390000002","37.12944969999999"],"63":["37.1674039","38.79551489999999"],"73":["37.41874809999997","42.491833799999995"],
     "59":["41.112122699999986","27.267611599999977"],"60":["40.3902713","36.625186299999996"],"61":["40.79924100000001","39.58479439999999"],
     "62":["39.30735540000001","39.43877780000002"],"64":["38.54313189999999","29.23207839999999"],
     "65":["38.501208500000004","43.37297930000002"],"77":["40.5775986","29.208830300000013"],"66":["39.727197900000014","35.10778590000001"],"67":["41.31249170000002","31.859825100000005"]}
    #https://www.letgo.com/tr-tr/c/all?distance=50&latitude=41.00823760000001&longitude=28.97835889999999&price%5Bmin%5D=100000&price%5Bmax%5D=250000
   





    list_count=[li for li in range(0,len(cty_list))]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Accept-Encoding": "*",
        "Connection": "keep-alive"
                    }
    #form request
    if request.method=="POST":
        cty_letgo=[]
        cty_arabam=""
        cty_sahibinden=""
        for ctys in checkbox_value:
            ctys_get=request.form.get(ctys)
            if ctys_get != None:
                cty_letgo.append(ctys_get)
                cty_arabam +="&city="+ctys_get
                cty_sahibinden +="&address_city="+ctys_get
             
        min_tl=request.form.get("min_tl")
        max_tl=request.form.get("max_tl")
      

        #https://www.letgo.com/tr-tr/c/cars?price%5Bmin%5D=100000&price%5Bmax%5D=300000&latitude=41.00823760000001&longitude=28.97835889999999&distance=50
        #letgo
        l_img=[]
        letgo_a=[]
        date_p=[]
        if bool(cty_letgo) == True: 
            for letGO in cty_letgo:  
                print(coordinate[letGO])
                latitude=coordinate[letGO][0]
                longitude=coordinate[letGO][1]
                #letgo
                print(latitude)
                l_url="https://www.letgo.com/tr-tr/c/cars?price%5Bmin%5D={mintl}&price%5Bmax%5D={maxtl}&latitude={latitude}&longitude={longitude}&distance=50".format(latitude=latitude,longitude=longitude,mintl=min_tl,maxtl=max_tl)
                r=requests.get(l_url)
                print(r)
                l_soup=BeautifulSoup(r.content,"lxml")
                
                multi_data=l_soup.find_all("div",attrs={"class":"Spacer__SpacerStyled-sc-11kae1j-0 eoQYxt Boxstyle__BoxStyled-h0e1j3-0 fLetif Cardstyle__CardStyled-v4il1t-0 iUeSPP ProductCardstyles__ProductCardStyled-sc-12t6nbg-0 bVWoli"})
                ad_letgo_number=l_soup.find("div",attrs={"class":"Spacer__SpacerStyled-sc-11kae1j-0 jnXsVH"})
                advert_letgo=ad_letgo_number.text.split()[3].replace(".","")
                ad_letgo=advert_letgo.strip()

                for i in multi_data:
                    letgo_content=i.find_all("div",attrs={"class":"slick-slide slick-active slick-current"})
                    for letgo_img in letgo_content:
                        l_img.append(letgo_img.img["data-src"])

                    letgo_a.append(i.a["href"])
                    paragraph=i.select("div > p")
                    p_tag=[]
                    for p in paragraph:
                        
                        p_tag.append(p.text)
                    date_p.append(p_tag)
        else:
             #letgo
            letgo_url="https://www.letgo.com/tr-tr/c/cars"
            r=requests.get(letgo_url)

            l_soup=BeautifulSoup(r.content,"lxml")
            
            multi_data=l_soup.find_all("div",attrs={"class":"Spacer__SpacerStyled-sc-11kae1j-0 eoQYxt Boxstyle__BoxStyled-h0e1j3-0 fLetif Cardstyle__CardStyled-v4il1t-0 iUeSPP ProductCardstyles__ProductCardStyled-sc-12t6nbg-0 bVWoli"})
            ad_letgo_number=l_soup.find("div",attrs={"class":"Spacer__SpacerStyled-sc-11kae1j-0 jnXsVH"})
            advert_letgo=ad_letgo_number.text.split()[3].replace(".","")
            ad_letgo=advert_letgo.strip()
            
            for i in multi_data:
                letgo_content=i.find_all("div",attrs={"class":"slick-slide slick-active slick-current"})
                for letgo_img in letgo_content:
                    l_img.append(letgo_img.img["data-src"])

                letgo_a.append(i.a["href"])
                paragraph=i.select("div > p")
                p_tag=[]
                for p in paragraph:
                    
                    p_tag.append(p.text)
                date_p.append(p_tag)

        counts=[i for i in range(0,len(l_img))]


        #arabam.com
        a_url="https://www.arabam.com/ikinci-el?currency=TL&minPrice={min}&maxPrice={max}{cty}".format(cty=cty_arabam,min=min_tl,max=max_tl)
        a_req=requests.get(a_url,headers=headers)
        print(a_req)
        a_soup=BeautifulSoup(a_req.content,"lxml")
        data_arabamcom=a_soup.find_all("tr",attrs={"class":"listing-list-item pr should-hover bg-white"})
        ad_arabamcom_number=a_soup.find("span",attrs={"id":"js-hook-for-advert-count"})
        advert_arabam=ad_arabamcom_number.text.replace(".","")
        arabam_img=[]
        arabam_a=[]
        first_data=[]
        for a_data in data_arabamcom:
            
            arabam_img.append(a_data.img["data-src"])
          
            arabam_a.append(a_data.a["href"])
        
            #print(a_data.h4.text)
            f_text=[]
            selector="""
            .crop-after,
            .fade-out-content-wrapper,
            .db no-wrap
            
            """
            first=sv.select(selector,a_data)

            for first_text in first:
                
                #first_clear=first_text.i
                #first_content=first_clear.clear()
                #print(first_content)

                texts=first_text.text
                if "" != texts:
                    f_text.append(texts)
                else:
                    pass
            first_data.append(f_text) 
     
        
    
       
        #sahibinden.com
       
        r_sahibinden=requests.get("https://www.sahibinden.com/kategori-vitrin?viewType=Gallery&price_min={min}&category=3517&price_max={max}{cty}".format(cty=cty_sahibinden,min=min_tl,max=max_tl),headers=headers)
        s_soup=BeautifulSoup(r_sahibinden.content,"lxml")

        s_findAll=s_soup.find_all("td",attrs={"class":"searchResultsGalleryItem searchResultsPromoHighlight searchResultsPromoBold"})
        ad_sahibinden_number=s_soup.find("div",attrs={"class":"result-text"})
        advert_sahibinden=ad_sahibinden_number.text.split()[3].replace(".","")
        print(advert_sahibinden)
        s_image=[]
        s_href=[]
        s_data=[]
        for s_all in s_findAll:
            s_imgALL=s_all.select(".searchResultsLargeThumbnail")
    
            selector="""
            .classifiedTitle,
            .searchResultsPriceValue,
            .searchResultsGallerySubContent
            
            """
        
            s_texts=sv.select(selector,s_all)
            s_textall=[]
            for s_text in s_texts:
                
                s=s_text.text.splitlines()
                for ss in s:
                    if ss !="":
                        s_strip=ss.strip(" ")
                        s_end=s_strip.strip("\xa0")
                        s_textall.append(s_end)
                    else:
                        pass
                
            s_data.append(s_textall)
            for s_imageALL in s_imgALL:
                photo=s_imageALL.img
                hrefs=s_imageALL.a
                s_image.append(photo["src"])
                s_href.append(hrefs["href"])
        count=[c for c in range(0,len(s_image))]
        #advers sum
        
        advert_sum=int(advert_arabam.strip())+int(advert_sahibinden.strip())+int(ad_letgo)

       
        return render_template("index.html",s_img=s_image,s_href=s_href,s_data=s_data,cty_list=cty_list
        ,checkbox_value=checkbox_value,list_count=list_count,
        arabam_img=arabam_img,arabam_a=arabam_a,count=count,a_text=first_data,
        l_img=l_img,counts=counts,l_text=date_p,letgo_a=letgo_a,advert=advert_sum)

    arabam_img=[]
    arabam_a=[]
    first_data=[]
   
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Accept-Encoding": "*",
        "Connection": "keep-alive"
                    }
    a_url="https://www.arabam.com/ikinci-el?tag=Ana%20Sayfa%20Vitrin&page={}".format(0)
    a_req=requests.get(a_url,headers=headers)

    a_soup=BeautifulSoup(a_req.content,"lxml")
    data_abm=a_soup.find_all("tr",attrs={"class":"listing-list-item pr should-hover bg-white"})
    
    ad_arabamcom_number=a_soup.find("span",attrs={"id":"js-hook-for-advert-count"})
    advert_arabam=ad_arabamcom_number.text.replace(".","")

    for a_data in data_abm:
            
        arabam_img.append(a_data.img["data-src"])
          
        arabam_a.append(a_data.a["href"])
        
        #print(a_data.h4.text)
        f_text=[]
        selector="""
            .crop-after,
            .fade-out-content-wrapper,
            .db no-wrap
            
            """
        first=sv.select(selector,a_data)

        for first_text in first:
                
                #first_clear=first_text.i
                #first_content=first_clear.clear()
                #print(first_content)

            texts=first_text.text
            if "" != texts:
                f_text.append(texts)
            else:
                    pass
        first_data.append(f_text)

    s=requests.Session()
    
    s_image=[]
    s_href=[]
    s_data=[]
    
    headers_s = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Accept-Encoding": "*",
        "Connection": "keep-alive"
                        }
    
    
    headers_s = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Accept-Encoding": "*",
        "Connection": "keep-alive"
                        }
    response=s.get("https://www.sahibinden.com/kategori-vitrin?viewType=Gallery&pagingOffset={}&category=3517".format(0), headers=headers_s)
    
    print(response)
    s_soup=BeautifulSoup(response.content,"lxml")
    s_findAll=s_soup.find_all("td",attrs={"class":"searchResultsGalleryItem searchResultsPromoHighlight searchResultsPromoBold"})
    
    
    for s_all in s_findAll:
        s_imgALL=s_all.select(".searchResultsLargeThumbnail")
        for s_imageALL in s_imgALL:
            photo=s_imageALL.img
            hrefs=s_imageALL.a
            s_image.append(photo["src"])
            s_href.append(hrefs["href"])
        selector="""
            .classifiedTitle,
            .searchResultsPriceValue,
            .searchResultsGallerySubContent
            
            """
        
        s_texts=sv.select(selector,s_all)
        s_textall=[]
        for s_text in s_texts:
                
            s=s_text.text.splitlines()
            for ss in s:
                if ss !="":
                    s_strip=ss.strip(" ")
                    s_end=s_strip.strip("\xa0")
                    s_textall.append(s_end)
                else:
                    pass
                
        s_data.append(s_textall)

    l_img=[]
    letgo_a=[]
    date_p=[] 
    letgo_url="https://www.letgo.com/tr-tr/c/cars/page/{}".format(1)
    r=requests.get(letgo_url,headers=headers)

    soup=BeautifulSoup(r.content,"lxml")
        
    multi_data=soup.find_all("div",attrs={"class":"Spacer__SpacerStyled-sc-11kae1j-0 eoQYxt Boxstyle__BoxStyled-h0e1j3-0 fLetif Cardstyle__CardStyled-v4il1t-0 iUeSPP ProductCardstyles__ProductCardStyled-sc-12t6nbg-0 bVWoli"})
    for i in multi_data:
        letgo_content=i.find_all("div",attrs={"class":"slick-slide slick-active slick-current"})
        for letgo_img in letgo_content:
            l_img.append(letgo_img.img["data-src"])
    
        letgo_a.append(i.a["href"])
        paragraph=i.select("div > p")
        p_tag=[]
        for p in paragraph:
                
            p_tag.append(p.text)
        date_p.append(p_tag)                

    
        
    counts=[i for i in range(0,len(l_img))]
    count=[a_len for a_len in range(0,len(s_image))]
    #count=[a_len for a_len in range(0,len(arabam_img))]

   
    return render_template("index.html",cty_list=cty_list,checkbox_value=checkbox_value,
    list_count=list_count,arabam_img=arabam_img,arabam_a=arabam_a,count=count,
    a_text=first_data,s_img=s_image,s_href=s_href,s_data=s_data,l_img=l_img,counts=counts,l_text=date_p,letgo_a=letgo_a,letgo_url=letgo_url)


    
if __name__=="__main__":
    app.run(debug=True)
    