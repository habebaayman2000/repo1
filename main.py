from flask import Flask, render_template,request
from numpy import full
import requests
from bs4 import BeautifulSoup as bs
zcxxcxd

ppp = Flask(__name__)

################################################################################33
url = 'https://www.jmir.org/'
article = requests.get(url)

soup = bs(article.content, 'html.parser')


def title():
    news_list=[]
    no_of_news =0

    # find all headers in bbc home 
    for e in soup.find_all('a',class_='h5'):
        news_title=e.contents[0]
        news_title=" ".join(news_title.split())


        if news_title not in news_list and no_of_news < 12:
            news_list.append(news_title)
            no_of_news +=1


    no_of_news =0
    for i, title in enumerate(news_list):
        no_of_news +=1
        #print(i+1,':',title)

    return news_list    


#titles(123)
#print(50*'-')

def sub_titles():
    news_list=[]
    no_of_news =0

    # find all headers in bbc home 
    for e in soup.find_all('a',class_='link card-theme'):
        news_title=e.contents[0]
        #print(news_title)
        news_title=" ".join(news_title.split())


        if  no_of_news < 12:
            news_list.append(news_title)
            no_of_news +=1


    no_of_news =0
    for i, title in enumerate(news_list):
        no_of_news +=1
        #print(i+1,':',title)
    return news_list 

#sub_titles(123)


def paragraph():
    news_list=[]
    no_of_news =0

    # find all headers in bbc home 
    for e in soup.find_all('p',class_='card-info-text'):
        e=e.find('span')
        news_title=e.contents[0]
        #print(news_title)
        news_title=" ".join(news_title.split())


        if  no_of_news < 12:
            news_list.append(news_title)
            no_of_news +=1


    no_of_news =0
    for i, title in enumerate(news_list):
        no_of_news +=1
       # print(i+1,':',title)
    return news_list 

#paragraph(123)



#print(50*'-')

def extract_links():
    url='https://www.jmir.org'
    links=[]
    i=0
    for link in soup.find_all('a',class_='h5'):
        href=link['href']
        if 'http' not in href and f'{url}{href}' not in links and i<12:
            links.append(f'{url}{href}')  
            i+=1  



    j=0
    for i in links:
        #print(f'{j+1} : {i}')
        j+=1
    return links 


#extract_links()


#print(100*'-')

def extract_imgs():
    src=[]
    i=0

    Image_item=soup.find('div',{'class':'cards'})
    Image_div=Image_item.find_all(class_='card mb-80')
    #print(Image_div)
    for img in Image_div:
        image=img.find('img')
        img_src=image.get('data-srcset')
        imgs=img_src.split()

        #img_src=img_src.replace('{width}','240')
        src.append(imgs[0])    

    j=0
    for i in src:
        #print(f'{j+1} : {i}')
        j+=1
    return src

def date():
    news_list=[]
    no_of_news =0

    # find all headers in bbc home 
    for e in soup.find_all('time',class_='mb-0'):
        news_title=e.contents[0]
        news_title=" ".join(news_title.split())


        if  no_of_news < 12:
            news_list.append(news_title)
            no_of_news +=1


    no_of_news =0
    for i, title in enumerate(news_list):
        no_of_news +=1
        #print(i+1,':',title)

    return news_list

#extract_imgs()
#########################################################################################################




@ppp.route("/")
def home():
    titles=title()
    links=extract_links()
    images=extract_imgs()
    sub_title=sub_titles()
    para=paragraph()
    d=date()
    return render_template("index.html",t0=titles[0],t1=titles[1],t2=titles[2],d0=d[0],d1=d[1],d2=d[2],s_t0=sub_title[0],s_t1=sub_title[1],s_t2=sub_title[2],p0=para[0],p1=para[1],p2=para[2],link0=links[0],link1=links[1],link2=links[2],image0=images[0],image1=images[1],image2=images[2])



@ppp.route("/index.html")
def home1():
    titles=title()
    links=extract_links()
    images=extract_imgs()
    sub_title=sub_titles()
    para=paragraph()
    d=date()
    return render_template("index.html",t0=titles[0],t1=titles[1],t2=titles[2],d0=d[0],d1=d[1],d2=d[2],s_t0=sub_title[0],s_t1=sub_title[1],s_t2=sub_title[2],p0=para[0],p1=para[1],p2=para[2],link0=links[0],link1=links[1],link2=links[2],image0=images[0],image1=images[1],image2=images[2])


@ppp.route("/Eldery.html")
def elder():
    return render_template("Eldery.html")

@ppp.route("/Alzehimer.html")
def Alzehimer():
    return render_template("Alzehimer.html")

@ppp.route("/Autism.html")
def Autism():
    return render_template("Autism.html")


@ppp.route("/about")
def about():
    return"about from falsd"    

@ppp.route("/blog.html")
def news():
    titles=title()
    links=extract_links()
    images=extract_imgs()
    sub_title=sub_titles()
    para=paragraph()
    da=date()
    return render_template("blog.html",t=titles,link=links,image=images,s_t=sub_title,p=para,d=da)



if __name__=="__main__":
    ppp.run(debug=True,port=8000)


