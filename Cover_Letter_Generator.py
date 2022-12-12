import PySimpleGUI as sg
import sys
import os
from os import path
#Default settings of interfaces
text_size = (20,1)
input_size = (40,1)
button_size = (20,1)
sg.theme('Kayak')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
#All the related paths are listed here:
path_source = "./lookUpSource"
path_body = path_source + "/body.txt"
path_word_pool = path_source + "/wordPool.txt"
path_company_doc = path_source + "/company"
path_company_des = path_company_doc + "/companyDescription.txt"
path_dictionary = path_source + "/keywordsDict.txt"
path_skill_des = path_source + "/skillDescription"
path_field_des = path_source + "/fieldDescription"
path_result = path_source + "/result"
#All the marks are initialized here:
content_marks = []
content_mark_start = "<-- From here your cover letter start -->"
content_marks.append(content_mark_start)
content_mark_role = "<-- Here fills a copy of the role you are applying for -->"
content_marks.append(content_mark_role)
content_mark_source = "<-- Here fills the social media name you know this job -->"
content_marks.append(content_mark_source)
content_mark_company_name = "<-- Here fills a copy of company name -->"
content_marks.append(content_mark_company_name)
content_mark_company_nickname = "<-- Here fills what the company is usually known as -->"
content_marks.append(content_mark_company_nickname)
content_mark_company_product = "<-- Here fills what the star product the company owns -->"
content_marks.append(content_mark_company_product)
content_mark_field = "<-- Here fills the description of your field -->"
content_marks.append(content_mark_field)
content_mark_skill = "<-- This is a paragraph descriping your technical stack, you can add many skills in it -->"
content_mark_skill_addition_01 = "<-- This is another paragraph descriping your technical stack, leave it blank if no need -->"
content_mark_skill_addition_02 = "<-- This is another paragraph descriping your technical stack, leave it blank if no need -->"
content_marks.append(content_mark_skill)
content_marks.append(content_mark_skill_addition_01)
content_marks.append(content_mark_skill_addition_02)
content_mark_company_description = "<-- This is a paragraph descriping the company you are applying to, it will be generated refering to company/companyDescription.txt you can modify it as you wish -->"
content_marks.append(content_mark_company_description)
content_mark_end = "<-- Your cover letter ends here -->"
content_marks.append(content_mark_end)

#First time refresh
if not path.exists(path_source):
    os.mkdir(path_source)

if not path.exists(path_dictionary):
    f_dict = open(path_dictionary,'w',encoding='utf-8')
    f_dict.writelines(["[Keyword Dictionary] You can find the keywords you need if you delete them by mistake\n","\n"])
    for i in range(len(content_marks)):
            f_dict.writelines(["\n",content_marks[i]])
    f_dict.close()


if not path.exists(path_body):
    f = open(path_body,'w',encoding='utf-8')
    f.writelines(["Thanks for using cover letter generator! You should finish your body of your cover letter once first, here is an example bolow, do not change any contents contains \"<--  -->\", they are essential marks.\n\n", 
                    content_mark_start,"\n","Dear "+content_mark_company_name+" hiring team:","\n","I am Ben. I graduated from University of Vitoria Royal Guards. I am now applying for the role "+content_mark_role+" you posted in " +content_mark_source+".","\n",
                    content_mark_field,"\n",content_mark_skill,"\n",content_mark_skill_addition_01,"\n",content_mark_skill_addition_02,"\n",
                    content_mark_company_name+" is known as "+content_mark_company_nickname+" for its product " + content_mark_company_product +", which make me interested in this field. It would be good if I can join such a team.","\n",content_mark_end,"\n[Caution] Examples teaching only, the author never guarantee anything, honest first. In other word, do not come to me for dealing with any possible failure to job searching. Good luck!"])
    f.close()

with open(path_body,'r',encoding='utf-8') as f:
    generate_body = f.readlines(encoding='utf-8').split(content_mark_start)[1].split(content_mark_end)[0]
    f.close()

if not path.exists(path_word_pool):
    f = open(path_word_pool,'w',encoding='utf-8')
    f.writelines(["Add some random adjs to descripe your company, one line for one word:","\n","Good"])
    f.close()
    
if not path.exists(path_skill_des):
    os.mkdir(path_skill_des)

    

if not path.exists(path_field_des):
    os.mkdir(path_field_des)
    
skill_description_list = os.listdir(path_skill_des)
field_description_list = os.listdir(path_field_des)

random_words = []
with open(path_word_pool,'r',encoding='utf-8') as f:
    random_words = f.readlines(encoding='utf-8').split("\n")
    f.close()
if len(field_description_list) == 0:
    f = open(path_field_des + "/eg.Internet.txt",'w',encoding='utf-8')
    f.writelines(["Internet is very good"])
    f.close()
    field_description_list = os.listdir(path_field_des)
if len(skill_description_list) == 0:
    f = open(path_skill_des + "/eg.python.txt",'w',encoding='utf-8')
    f.writelines(["My python is very good"])
    f.close()
    skill_description_list = os.listdir(path_skill_des)

if not path.exists(path_company_doc):
    os.mkdir(path_company_doc)
    
if not path.exists(path_company_des):
    f = open(path_company_des,'w',encoding='utf-8')
    f.writelines([content_mark_company_name + " is known as " + content_mark_company_nickname + " for its product "+content_mark_company_product,"\n","This is a simple example for company description."])
    f.close()
#Refresh the current document status and contents
def Refresh():
    if not path.exists(path_source):
        os.mkdir(path_source)

    if not path.exists(path_dictionary):
        f_dict = open(path_dictionary,'w',encoding='utf-8')
        f_dict.writelines(["[Keyword Dictionary] You can find the keywords you need if you delete them by mistake\n","\n"])
        for i in range(len(content_marks)):
             f_dict.writelines(["\n",content_marks[i]])
        f_dict.close()

    if not path.exists(path_body):
        f = open(path_body,'w',encoding='utf-8')
        f.writelines(["Thanks for using cover letter generator! You should finish your body of your cover letter once first, here is an example bolow, do not change any contents contains \"<--  -->\", they are essential marks.\n\n", 
                      content_mark_start,"\n","Dear "+content_mark_company_name+" hiring team:","\n","I am Ben. I graduated from University of Vitoria Royal Guards. I am now applying for the role "+content_mark_role+" you posted in " +content_mark_source+".","\n",
                      content_mark_skill,"\n",content_mark_skill_addition_01,"\n",content_mark_skill_addition_02,"\n",
                      content_mark_company_name+" is known as "+content_mark_company_nickname+" for its product " + content_mark_company_product +", which make me interested in this field. It would be good if I can join such a team.","\n",content_mark_end,"\n[Caution] Examples teaching only, the author never guarantee anything, honest first. In other word, do not come to me for dealing with any possible failure to job searching. Good luck!"])
        f.close()

    with open(path_body,'r',encoding='utf-8') as f:
        generate_body = f.readlines(encoding='utf-8').split(content_mark_start)[1].split(content_mark_end)[0]
        f.close()

    if not path.exists(path_word_pool):
        f = open(path_word_pool,'w',encoding='utf-8')
        f.writelines(["Add some random adjs to descripe your company, one line for one word:","\n","Good"])
        f.close()
    
    if not path.exists(path_skill_des):
        os.mkdir(path_skill_des)

    

    if not path.exists(path_field_des):
        os.mkdir(path_field_des)
    
    skill_description_list = os.listdir(path_skill_des)
    field_description_list = os.listdir(path_field_des)

    random_words = []
    with open(path_word_pool,'r',encoding='utf-8') as f:
        random_words = f.readlines(encoding='utf-8').split("\n")
    f.close()
    if len(field_description_list) == 0:
        f = open(path_field_des + "/eg.Internet.txt",'w',encoding='utf-8')
        f.writelines(["Internet is very good"])
        f.close()
        field_description_list = os.listdir(path_field_des)
    if len(skill_description_list) == 0:
        f = open(path_skill_des + "/eg.python.txt",'w',encoding='utf-8')
        f.writelines(["My python is very good"])
        f.close()
        skill_description_list = os.listdir(path_skill_des)

    if not path.exists(path_company_doc):
        os.mkdir(path_company_doc)
    
    if not path.exists(path_company_des):
        f = open(path_company_des,'w',encoding='utf-8')
        f.writelines([content_mark_company_name + " is known as " + content_mark_company_nickname + " for its product "+content_mark_company_product,"\n","This is a simple example for company description."])
        f.close()


#Build the user interface:
def Showup(screen_message = "",filename =""):
    global UI_keys_field_description_list
    UI_keys_field_description_list = []
    global UI_keys_skill_description_list
    UI_keys_skill_description_list = []
    global UI_keys_skill_description_addtion_01_list
    UI_keys_skill_description_addtion_01_list = []
    global UI_keys_skill_description_addtion_02_list
    UI_keys_skill_description_addtion_02_list = []
    welcome_info = "**Welcome to cover letter generator!**\nBy filling the blanks and preparing your files,\nThen create cover letter for different companies in 1 sec!" 
    done_info = "Done!\nYour cover letter has been saved in \"result\" folder as:"
    if screen_message == "":
        screen_message = welcome_info
    if screen_message == "done":
        screen_message = done_info + filename
    UI_field_description_list = [sg.Text('Field description: ',size = text_size)]
    for i in range(len(field_description_list)):
        tmp_des = field_description_list[i]
        UI_field_description_list.append(sg.Radio(tmp_des,"field_des",key=tmp_des,default = False))
        UI_keys_field_description_list.append(tmp_des)
    UI_skill_description_list = [sg.Text('Skill description(1): ',size = text_size)]
    UI_skill_description_list_addtion_01 = [sg.Text('Skill description(2): ',size = text_size)]
    UI_skill_description_list_addtion_02 = [sg.Text('Skill description(3): ',size = text_size)]
    for i in range(len(skill_description_list)):
        tmp_des = skill_description_list[i]
        UI_skill_description_list.append(sg.CBox(tmp_des,key=tmp_des+"01"))
        UI_keys_skill_description_list.append(tmp_des+"01")
        UI_skill_description_list_addtion_01.append(sg.CBox(tmp_des,key=tmp_des+"02"))
        UI_keys_skill_description_addtion_01_list.append(tmp_des+"02")
        UI_skill_description_list_addtion_02.append(sg.CBox(tmp_des,key=tmp_des+"03"))
        UI_keys_skill_description_addtion_02_list.append(tmp_des+"03")
    # All the stuff inside your window.
    layout = [  [sg.Text('You must fill all the (*) blanks')],
                [sg.Text('Company name*: ',size = text_size), sg.Input(size = input_size,key='company_name')],
                [sg.Text('Company nickname: ',size = text_size), sg.Input(size = input_size,key='company_nickname')],
                [sg.Text('Position name(role,job title)*: ',size = text_size), sg.Input(size = input_size,key='position_name')],
                [sg.Text('Where you know this job: ',size = text_size), sg.Input(size = input_size,key='social_name')],
                [sg.Text('Name of star product: ',size = text_size), sg.Input(size = input_size,key='product_name')],
                
                UI_field_description_list,
                UI_skill_description_list,
                UI_skill_description_list_addtion_01,
                UI_skill_description_list_addtion_02,

                [sg.Button('Give me cover letter!',size = button_size), sg.Button('Refresh',size = button_size), sg.Button('Quit',size = button_size)],
                [sg.Text(screen_message,size=(80,5), key='output')]
                ]

    # Create the Window
    window = sg.Window('Cover Letter Generator', layout,enable_close_attempted_event=True)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.readlines()
        if (event == sg.WIN_CLOSED or event == 'Quit') and sg.popup_yes_no('Do you really want to exit?\nThanks for using, I hope you good luck in job searching!') == 'Yes': # if user closes window or clicks cancel
            break
        if (event == 'Give me cover letter!'):
            window.close()
            InputCheck(values)
            
        if (event == 'Refresh'):
            Refresh()
            window.close()
            Showup("Document status updated!")
            

        window['output'].update(screen_message)
    window.close()     


def InputCheck(values):
    msg = "done"
    done = True
    res = generate_body
    filename = ""
    if values['company_name'] == "":
        msg = "company name can not be empty!"
        done = False
    else:
        res = InsertContents(res,content_mark_company_name,values['company_name'])
    if values['position_name'] == "":
        msg = "position name can not be empty!"
        done = False
    else:
        res = InsertContents(res,content_mark_role,values['position_name'])
    res = InsertContents(res,content_mark_company_nickname,values['company_nickname'])
    res = InsertContents(res,content_mark_source,values['social_name'])
    res = InsertContents(res,content_mark_company_product,values['product_name'])
    for i in range(len(UI_keys_field_description_list)):
        if values[UI_keys_field_description_list[i]] == True:
            res = InsertContents(res,content_mark_field, ReadSpecificSentence(path_field_des+"/"+field_description_list[i]))
    for i in range(len(UI_keys_skill_description_list)):
        if values[UI_keys_skill_description_list[i]] == True:
            res = InsertContents(res,content_mark_skill,ReadSpecificSentence(path_skill_des+"/"+skill_description_list[i]))
    for i in range(len(UI_keys_skill_description_addtion_01_list)):
        if values[UI_keys_skill_description_addtion_01_list[i]] == True:
            res = InsertContents(res,content_mark_skill_addition_01,ReadSpecificSentence(path_skill_des+"/"+skill_description_list[i]))
    for i in range(len(UI_keys_skill_description_addtion_02_list)):
        if values[UI_keys_skill_description_addtion_02_list[i]] == True:
            res = InsertContents(res,content_mark_skill_addition_02,ReadSpecificSentence(path_skill_des+"/"+skill_description_list[i]))
    if done:
        if not path.exists(path_result):
            os.mkdir(path_result)
        filename = values['position_name']+"-"+values['company_name']+".txt"
        with open(path_result+"/"+filename,'w',encoding='utf-8') as f:
            f.writelines(res)
            f.close()
    Showup(msg,filename)
    pass



#Read contents from files:


def ReadSpecificSentence(path):
    with open(path,'r',encoding='utf-8') as f:
        res = f.readlines(encoding='utf-8')
        f.close()
        return res
def ReadRandomSection(path):
    with open(path,'r',encoding='utf-8') as f:
        res = f.readlines(encoding='utf-8')
        f.close()
        return res

#Combine the inputs and preset contents, userinput should be a dictionary



def InsertContents(origin_body,content_mark,content):
    origin_body_list = origin_body.split(content_mark)
    n = len(origin_body_list)
    if n <= 1:
        return origin_body
    else:
        res = ""
        i = 0
        while i < n-1:
            res += origin_body_list[i]
            res += content
            i+=1
        res += origin_body_list[n-1]
        return res





Refresh()

Showup()
