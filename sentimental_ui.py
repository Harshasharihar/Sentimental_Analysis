import tkinter as tk

import requests

import json


def apiResponse():
    sent1 = fb1.get()
    sent2 = fb2.get()
    sent3 = fb3.get()
    senti = [sent1,sent2,sent3]
    def analyseResp(resp_recieved):
        dict1 = d[0]
        new_d = {}
        actual_response = ''
        for k,v in dict1.items():
            if k == 'classifications':
                new_d = v[0]
                for k1,v1 in new_d.items():
                    if k1 == 'tag_name':
                        actual_response = v1
                        return actual_response



    api_key = '88a20b724080776b540ae80fc5a5ff6a7e9fadef'
    url = 'https://api.monkeylearn.com/v3/classifiers/cl_pi3C7JiL/classify/'
    header = {"Authorization":f"Token {api_key}"}
    new_sent=[]
    for i in range(0,3):
        data = {'data':[senti[i]]}
        response = requests.post(url,headers=header,json=data)
        d=response.json()
        sentiment = analyseResp(d)
        new_sent.append(sentiment)
    lbl2.config(text=new_sent[0])
    lbl3.config(text=new_sent[1])
    lbl4.config(text=new_sent[2])



root = tk.Tk()
root.title("Sentimental Analysis")
lbl1 = tk.Label(root,text='Welcome to Sentimental Analysis')
fb1 = tk.Entry(root)
fb2 = tk.Entry(root)
fb3 = tk.Entry(root)
btn  = tk.Button(root,text='Send',fg ='lightblue',bg='Blue',command=apiResponse)
fb1.grid(row=1,column=0)
fb2.grid(row=3,column=0)
fb3.grid(row=5,column=0)
btn.grid(row=7,column=0)
lbl2 = tk.Label(root,text="")
lbl3 = tk.Label(root,text="")
lbl4 = tk.Label(root,text="")
lbl1.grid(row=0,column=0)
lbl2.grid(row=2,column=0)
lbl3.grid(row=4,column=0)
lbl4.grid(row=6,column=0)
root.mainloop()