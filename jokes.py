import requests as rq 
from bs4 import BeautifulSoup as bfs 
import json
import random

#extracting / storing data from / into the jokes.txt file


try:
    with open('jokes.txt','r',encoding='utf-8') as file:
        markup=file.read()



except:
    try:
        response=rq.get('http://quotes.toscrape.com/')
        with open('jokes.txt','w',encoding='utf-8') as file:
            file.write(response.text)

        with open('jokes.txt','r',encoding='utf-8') as file:
            markup=file.read()
    except:
        print('internet error to download necessary resources...')
        exit()

#now our file part is done and we have extracted the data into the variable 'markup'

#now creating joke.json to store data if dont exist
try:
    with open('jokes.json','r') as file:
        pass

except:
    soup=bfs(markup,'html.parser')

    #now making the json file (jokes.json) where i will store each and every joke with their respective authors

    #catching authors and their jokes

    joke_div=soup.find_all(name='div',class_='quote')
    author_list=[]
    joke_list=[]

    

    for i in joke_div:
        joke_list.append(i.span.string)
        author_list.append(i.find('small',class_='author').string)


         #putting them in jokes.json file
    combined_list=[]
    for i in joke_list:
        
        temporary_list=[[i,author_list[joke_list.index(i)]]]
        combined_list+=temporary_list

    
    with open('jokes.json','w') as file:
        json.dump(combined_list,file,indent=4)

    #here our work comes to end
        
# now the joke machine starts
active=True

with open('jokes.json','r') as file:
    content=json.load(file)

    while active:
        command=input('joke: ')
        if command=='j':
            rand_joke=random.randrange(0,len(content))
            print(f'''{content[rand_joke][0]}    -by{content[rand_joke][1]}
                  ''')
        else:
            active=False
    exit()
