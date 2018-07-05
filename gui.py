import sys,os
import urllib
from Tkinter import *
from bs4 import BeautifulSoup
import tkFont
from collections import Counter
import re
from itertools import izip

def mhello():

    text1=entry1.get()
    text2=entry2.get()
    urllib.urlretrieve(text1,text2)
    return

def sSearch():
    searched_word=entry3.get()
    print searched_word
    #query string
    path=entry4.get()

    #--------------------------------Finds the list of text files in that directory ----------------------------------------------------#
    
    text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
    print text_files

    #----------------------------- Find the url of those text files --------------------------------------------------#
    url=[]
    path1=''
    for items in text_files:
        path1=path+"\\"+items
        url.append(path1)
    #print url

    #--------------------------- Find the pages containing the string --------------------------------------#
    url_with_required_word=[]
    for items in url:
        #print items
        page = open(items,'r')
        soup = BeautifulSoup(page.read(),"html.parser")
        #searched_word = 'What'
        results = soup.body.find_all(string=re.compile('.*{0}.*'.format(searched_word)), recursive=True)
        #print results
        if len(results)!=0:
            url_with_required_word.append(items)
    #print "Pages containing required word are=",url_with_required_word

    #------------------------ To remove the stop words and find top 3 words from each page -----------------------#
    stop_words1=["a","b","c","d","s", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whether", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]
    max1=[]
    for items in url_with_required_word:
        page = open(items,'r')
        soup = BeautifulSoup(page.read(),"html.parser")
        k=soup.get_text()
        words = re.findall(r'\w+', k)
        #words will give the list of all words in the html page
        cap_words = [word.upper() for word in words] #capitalizes all the words
        #print cap_words
        stop_words=[word.upper() for word in stop_words1]
        list3 = [item for item in cap_words if item not in stop_words]
        word_counts = Counter(list3) #counts the number each time a word appears
        #print "URL=",items
        max=word_counts.most_common(3)
        #print "Top 3 are =",max
        #max=list
        max1.append(word_counts.most_common(3))
    #print "LIST OF MAX 3 from each file"
    #print max1

    #----------------------- To find top 3 out of all top 3 words of the web pages ------------------------------#
    
    t=[]
    for items in max1:
        for j in items:
            for i in j:
                t.append(i)
    print t
    i = iter(t)
    b = dict(izip(i, i))
    #print b
    #I have to delete searched word from b
    Capital_word=searched_word.upper()
    del b[Capital_word]
   

    word_counts = Counter(b) #counts the number each time a word appears
     
    max_final=word_counts.most_common(3)
    print max_final
    #[(u'BAKING', 51), (u'SODA', 50), (u'CHEMISTRY', 32)]
    words_to_find=[]
    for items in max_final:
        words_to_find.append(items[0])
    print "Words to find"
    print words_to_find

    #--------------------- To find the words from the list of urls -------------------------------------------#
   
    
    for i in words_to_find:
        print "The following word " , i , "is in URL's"
        for j in url_with_required_word:
            page = open(j,'r')
            soup = BeautifulSoup(page.read(),"html.parser")
            k=soup.get_text()
            words = re.findall(r'\w+', k)
            cap_words = [word.upper() for word in words]
            stop_words=[word.upper() for word in stop_words1]
            list3 = [item for item in cap_words if item not in stop_words]
            if i in list3:
                print j   
    return

    

root = Tk()

root.geometry('550x550+100+20')
#'wxh±x±y'
#A geometry string is a standard way of describing the size and location of a top-level window on a
#desktop.
#NMT page 36
entry1=StringVar()
entry2=StringVar()
entry3=StringVar()
entry4=StringVar()
helv36 = tkFont.Font(family='Helvetica',size=25, weight='bold')
font1 = tkFont.Font(family='Helvetica',size=12, weight='bold')
root.title("Done with you finally")
#mlabel=Label(text='URL',fg='red').place(x=10,y=10)
mlabel1=Label(text='Meta Search Engine',font=helv36).grid(row=0,column=20,sticky=W,rowspan=20)
mlabel2=Label(text='URL').grid(row=40,column=2,sticky=W,rowspan=20)
mEntry2=Entry(root,textvariable=entry1,width=40).grid(row=40,column=20,sticky=W,rowspan=20,columnspan=20)
#Sticky can be east west north and south
mlabel3=Label(text='Address').grid(row=80,column=2,sticky=W,rowspan=20)
mEntry3=Entry(root,textvariable=entry2,width=40).grid(row=80,column=20,sticky=W,rowspan=20,columnspan=20)
button1=Button(text='Download',command=mhello,fg='blue',bg='yellow').grid(row=120,column=20)

mlabel4=Label(text='Query String').grid(row=160,column=2,rowspan=20,sticky=W)
mEntry4=Entry(root,textvariable=entry3,width=40).grid(row=160,column=20,sticky=W,rowspan=20,columnspan=20)
mlabel5=Label(text='Location to find the query string').grid(row=200,column=2,rowspan=20,sticky=W)
mEntry5=Entry(root,textvariable=entry4,width=40).grid(row=200,column=20,sticky=W,rowspan=20,columnspan=20)

button2=Button(text='Search',command=sSearch,fg='blue',bg='yellow').grid(row=240,column=20)

mainloop()

