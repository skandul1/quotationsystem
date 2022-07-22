# from flask import Flask, redirect, url_for, request
#
# app = Flask(__name__)
# temp = []
#
#
# @app.route('/success/<name>')
# def success(name):
#     a = name
#     return 'quote data is  %s' % name
#
#
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     # print(temp)
#     if request.method == 'POST':
#         # user=request.form['nm']
#         # user1 = request.form['nm1']
#         Quote_no = request.form['Quote_no']
#         Part_Number = request.form['Part_Number']
#         Part_Name = request.form['Part_Name']
#         Alloy = request.form['Alloy']
#         Temper = request.form['Temper']
#         Profile = request.form['Profile']
#         Part_Size_Thickness = request.form['Part_Size_Thickness']
#         Part_Size_Width = request.form['Part_Size_Width']
#         Part_Size_Length = request.form['Part_Size_Length']
#         Part_Size_Weight = request.form['Part_Size_Weight']
#         Raw_Material_Thickness = request.form['Raw_Material_Thickness']
#         Raw_Material_Width = request.form['Raw_Material_Width']
#         Raw_Material_Length = request.form['Raw_Material_Length']
#         Raw_Material_Weight = request.form['Raw_Material_Weight']
#         Metal_removal = request.form['Metal_removal']
#         Removal_rate = request.form['Removal_rate']
#         Machine_Hours = request.form['Machine_Hours']
#         Machine_rate = request.form['Machine_rate']
#         Machining_price = request.form['Machining_price']
#         Material_dollar = request.form['Material_dollar']
#         Material_price = request.form['Material_price']
#         Treatment_Price = request.form['Treatment_Price']
#         temp.append(Quote_no)
#         temp.append(Part_Number)
#         temp.append(Part_Name)
#         temp.append(Alloy)
#         temp.append(Temper)
#         temp.append(Profile)
#         temp.append(Part_Size_Thickness)
#         temp.append(Part_Size_Width)
#         temp.append(Part_Size_Length)
#         temp.append(Part_Size_Weight)
#         temp.append(Raw_Material_Thickness)
#         temp.append(Raw_Material_Width)
#         temp.append(Raw_Material_Length)
#         temp.append(Raw_Material_Weight)
#         temp.append(Metal_removal)
#         temp.append(Removal_rate)
#         temp.append(Machine_Hours)
#         temp.append(Machine_rate)
#         temp.append(Machining_price)
#         temp.append(Material_dollar)
#         temp.append(Material_price)
#         temp.append(Treatment_Price)
#         # temp.append()
#         # temp.append()
#         print(temp)
#         # user1=request.form['nm1']
#         return redirect(url_for('success',
#                                 name=Quote_no + " " + Part_Number + " " + Part_Name + " " + Alloy + " " + Temper + " " + Profile + " " + Part_Size_Thickness + " " + Part_Size_Width + " " + Part_Size_Length +
#                                      " " + Part_Size_Weight + " " + Raw_Material_Thickness + " " + Raw_Material_Width + " "
#                                      + Raw_Material_Length + " " + Raw_Material_Weight + " " + Metal_removal + " " + Removal_rate + " " +
#                                      Machine_Hours + " " + Machine_rate + " " + Machining_price + " " + Material_dollar + " " + Material_price + " " + Treatment_Price))
#     else:
#         # user = request.args.get('nm')
#         # user1 = request.args.get('nm1')
#         # user1 = request.args.get('Quote_no')
#         return redirect(url_for('success',
#                                 name=Quote_no + " " + Part_Number + " " + Part_Name + " " + Alloy + " " + Temper + " " + Profile + " " + Part_Size_Thickness + " " + Part_Size_Width + " " + Part_Size_Length +
#                                      " " + Part_Size_Weight + " " + Raw_Material_Thickness + " " + Raw_Material_Width + " "
#                                      + Raw_Material_Length + " " + Raw_Material_Weight + " " + Metal_removal + " " + Removal_rate + " "
#                                      + Machine_Hours + " " + Machine_rate + " " + Machining_price + " " + Material_dollar + " " + Material_price + " " + Treatment_Price))
#
#
# if __name__ == '__main__':
#     app.run(debug=True ,port=5000,use_reloader=False)

import time
from flask import Flask, redirect, url_for, request
from flask import Flask, render_template, request, make_response
from openpyxl import load_workbook
from flask_cors import CORS
from flask import Flask;
import pandas as pd;
from pandas import DataFrame, read_csv;
import matplotlib.pyplot as plot
import os
from PIL import Image
import base64
import io
from matplotlib.ticker import MaxNLocator
import math

HOST_NAME = "localhost"
HOST_PORT = 5000
app = Flask(__name__)
CORS(app)

# app = Flask(__name__)
temp = []

# def temp():
#
# @app.route("/",methods=["POST","GET"])

@app.route("/",methods=['POST','GET'])
def index():
    # if request.form["btn"] == "home":
    # print("entering")
    if request.method == 'POST':
        # print("entering inside post")
        Manufacturer2 = request.form['Manufacturer2']
        Model2 = request.form['Model2']
        Machine_name2=request.form['Machine_name2']
        Category2 = request.form['Category2']
        Form2 = request.form['Form2']
        # print(Form2)
        Alloy2=request.form['Alloy2']
        text_file1 = open(r"C:\Users\saich\Desktop\quotation system\venv\templates\templates\index.html", "w")
        text_file1.write("")
        text_file1.close()
        # print(Manufacturer2)
        # print("exiting")
  # (B1) OPEN EXCEL FILE + WORKSHEET
  # book = load_workbook("s1_dummy.xlsx")
  # sheet = book.active
  # # first_column = sheet[0]
  # # (B2) PASS INTO HTML TEMPLATE
  # return render_template("s3_excel_table.html", sheet=sheet)
  # import pandas as pd
  # create dataframe
  #       print("hello there")
        data = pd.read_excel(r'C:\Users\saich\Desktop\quotation system\venv\templates\Quotationsystem_20220207.xlsx','Machining part',skiprows=2)
        data2 = pd.read_excel(r'C:\Users\saich\Desktop\quotation system\venv\templates\Quotationsystem_20220207.xlsx',
                             'Calculation_formula#1', skiprows=4)
  # xls = pd.ExcelFile('path_to_file.xls')
  # df1 = pd.read_excel(xls, 'Sheet1')
  # df = pd.DataFrame(data)
  # & (df_marks['Machining Name_1'] == "VC630")
        df_marks = pd.DataFrame(data,columns= ['Manufacturer','Model','Part Number','Part Name_01','Material_Elements',
                                         'Material_Form','Material_Alloy','Metal Removal (kg)','Metal Removal Rate (kg/hr)',
                                         'Machining Name_1','Machining Hours_1','Machining Cost_1'])
        df_marks2 = pd.DataFrame(data2)
        mytem1 = df_marks2.iloc[:, 9].values.tolist()
        mytem2 = df_marks2.iloc[:, 10].values.tolist()
        mytem3 = df_marks2.iloc[:, 8].values.tolist()
        mytem4 = df_marks2.iloc[:, 11].values.tolist()
        pet=[]
        for ter in mytem2:
            pet.append("{:.2f}".format(ter))
        mytem2 = pet
        # print(list(set(mytem3)))
        # print(mytem2)
        dict1={}
        # print(Category2 + Form2)
        for x in range(0,len(mytem1)):
            if mytem1[x]+mytem3[x] in dict1:
                dict1[mytem1[x]+mytem3[x]].append(str(mytem2[x])+'@'+str(mytem4[x]))
            else:
                dict1[mytem1[x]+mytem3[x]]= [str(mytem2[x])+'@'+str(mytem4[x])]
        # print(dict1[Category2+Form2])
        # print(dict1)
        # print("average rate= " + str(
        # sum(dict1[Category2]) / len(dict1[Category2])))
        # plot.hist(weightList, density=1, bins=20)
        # plot.plot(dict1[Category2+Form2],'o')
        # plot.axis(Category2)
        # axis([xmin,xmax,ymin,ymax])
        xlist=[]
        ylist=[]
        for x in dict1[Category2+Form2]:
            p=x.split('@')
            # print(p)
            xlist.append(int(float(p[1])))
            ylist.append(float(p[0]))
        # xi = list(range(len(x)))
        te=sum(ylist)/len(ylist)
        # fig, ax = plot.subplots()
        # str(te)
        # plot.text(1, 1, 'Hello World !')

        # plot.xticks(xi, xlist)
        # , marker = 'o', linestyle = '--', color = 'r'

        fig, ax = plot.subplots()
        ax.scatter(xlist, ylist)

        for i, txt in enumerate(ylist):
            ax.annotate(txt, (xlist[i], ylist[i]))
        xint = range(math.floor(min(mytem4)), math.ceil(max(mytem4))+1)
        plot.xticks(xint)
        plot.bar(xlist, ylist)
        plot.xlabel('year')
        plot.ylabel('Metal Removal Rate')
        plot.title('average' + '=' + str(te))
        # plot.xticks(range(min(xlist), max(ylist) + 1))
        # for i, v in enumerate(ylist):
        #     ax.text(v + 3, i + .25, str(v), color='blue', fontweight='bold')
        # plot.text(-5, 60, 'Graph1', fontsize=22)
        strFile = "temp.jpg"
        if os.path.isfile(strFile):
            print("yes")
            os.remove(strFile)  # Opt.: os.system("rm "+strFile)
            print("removed")
        # plot.savefig(strFile)

        plot.savefig('temp.jpg')
        # plot.savefig('temp.jpg',bbox_inches="tight",dpi=50)
        # plot.show()
        plot.close()
        # plot.show()
        # print(required_column1)
        # print(Manufacturer2)
        # print(Model2)
        f=1
        try:
            string_int = int(Model2)
        except ValueError:
            f=0
            pass
        if f==1:
            Model2 = int(Model2)
        f2 = 1
        try:
            string_int2 = int(Machine_name2)
        except ValueError:
            f2 = 0
            pass
        if f2 == 1:
            Machine_name2= int(Machine_name2)
        f3 = 1
        try:
            string_int3 = int(Alloy2)
        except ValueError:
            f3 = 0
            pass
        if f3 == 1:
            Alloy2 = int(Alloy2)
        # print(Machine_name2,type(Machine_name2))
        df_marks=df_marks.loc[(df_marks['Manufacturer'] == Manufacturer2) & (df_marks['Model'] == Model2) &
                              (df_marks['Machining Name_1'] == Machine_name2) &(df_marks['Material_Elements'] == Category2)
                              & (df_marks['Material_Form'] == Form2) & (df_marks['Material_Alloy'] == Alloy2)]
        #
        # df_marks=(df_marks.style.set_properties(**{'width': '2px','white-space': 'pre-wrap','text-align': 'left' , 'font-size': '7pt','border-color':'Black','border-width':'thin','border-style':'solid'}))
  # print(df_marks.columns)
  #       df_marks = df_marks.style.set_table_styles(
  #           [{"selector": "", "props": [("border", "1px solid grey")]},
  #            {"selector": "tbody td", "props": [("border", "1px solid grey")]},
  #            {"selector": "th", "props": [("border", "1px solid grey")]}
  #            ]
  #       )
  # df_marks = pd.DataFrame({'name': ['Somu', 'Kiku', 'Amol', 'Lini'],
  #                          'physics': [68, 74, 77, 78],
  #                          'chemistry': [84, 56, 73, 69],
  #                          'algebra': [78, 88, 82, 87]})

  # render dataframe as html
  #       im = Image.open("temp.jpg")
        # data = io.BytesIO()
        # im.save(data, "JPEG")
        # encoded_img_data = base64.b64encode(data.getvalue())
        # html = df_marks.to_html()
  # write html to file
  #       html = encoded_img_data.decode('utf-8')
        text_file = open(r"C:\Users\saich\Desktop\quotation system\venv\templates\templates\index.html", "w")
        html = """<html>
        <head></head>
        <body>
        <h1>Graph 1</h1>
        <img src="../temp.jpg" width="100%" height="500">
        <hr style="height:2px;border-width:0;color:gray;background-color:gray">
        <h1>Graph 2</h1>
        <img src="../temp.jpg" width="100%" height="500">
        <hr style="height:2px;border-width:0;color:gray;background-color:gray">
        <h1>Graph 3</h1>
        <img src="../temp.jpg" width="100%" height="500">
        </body>
        </html>"""
        text_file.write(html)
        # text_file.write(html)
        print("writing done")
        text_file.close()
    # return render_template("index.html")
    return ('', 204)
@app.route('/success/<name>')
def success(name):
    a = name
    return 'quote data is is  %s' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    # print(temp)
    if request.method == 'POST':
        # user=request.form['nm']
        # user1 = request.form['nm1']
        Quote_no = request.form['Quote_no']
        Manufacturer=request.form['Manufacturer']
        # Manufacturer2 = request.form['Manufacturer2']
        Model=request.form['Model']
        Part_Number = request.form['Part_Number']
        Part_Name = request.form['Part_Name']
        Material = request.form['Material']
        form = request.form['Form']
        Alloy = request.form['Alloy']
        Temper = request.form['Temper']
        Profile = request.form['Profile']
        Part_Size_Thickness = request.form['Part_Size_Thickness']
        Part_Size_Width = request.form['Part_Size_Width']
        Part_Size_Length = request.form['Part_Size_Length']
        Part_Size_Weight = request.form['Part_Size_Weight']
        Raw_Material_Thickness = request.form['Raw_Material_Thickness']
        Raw_Material_Width = request.form['Raw_Material_Width']
        Raw_Material_Length = request.form['Raw_Material_Length']
        Raw_Material_Weight = request.form['Raw_Material_Weight']
        Metal_removal = request.form['Metal_removal']
        Removal_rate = request.form['Removal_rate']
        Machine_Hours = request.form['Machine_Hours']
        Machine_rate = request.form['Machine_rate']
        Machining_price = request.form['Machining_price']
        Material_dollar = request.form['Material_dollar']
        Material_price = request.form['Material_price']
        Treatment_Price = request.form['Treatment_Price']
        temp.append(Quote_no)
        temp.append(Manufacturer)
        temp.append(Model)
        temp.append(Part_Number)
        temp.append(Part_Name)
        temp.append(Material)
        temp.append(Alloy)
        temp.append(Temper)
        temp.append(Profile)
        temp.append(Part_Size_Thickness)
        temp.append(Part_Size_Width)
        temp.append(Part_Size_Length)
        temp.append(Part_Size_Weight)
        temp.append(Raw_Material_Thickness)
        temp.append(Raw_Material_Width)
        temp.append(Raw_Material_Length)
        temp.append(Raw_Material_Weight)
        temp.append(Metal_removal)
        temp.append(Removal_rate)
        temp.append(Machine_Hours)
        temp.append(Machine_rate)
        temp.append(Machining_price)
        temp.append(Material_dollar)
        temp.append(Material_price)
        temp.append(Treatment_Price)
        # temp.append(Manufacturer2)
        # temp.append()
        # temp.append()
        # print(Manufacturer2)
        # user1=request.form['nm1']
        # + Machining_price + " "
        # + Machining_price + " "
        time.sleep(10)
        return redirect(url_for('success',
                                name=Quote_no + " " + Manufacturer+" " + Model + " " + Part_Number + " " +  Part_Name + " " + Material +
                                     " " + form + " " + Alloy + " " + Temper + " " +
                                     Profile + " " + Part_Size_Thickness + " " + Part_Size_Width + " " + Part_Size_Length +
                                     " " + Part_Size_Weight + " " + Raw_Material_Thickness + " " + Raw_Material_Width + " "
                                     + Raw_Material_Length + " " + Raw_Material_Weight + " " + Metal_removal + " " + Removal_rate + " " +
                                     Machine_Hours + " " + Machine_rate + " "+ Machining_price + " " + Material_dollar +" " + Material_price + " " +
                                     Treatment_Price))
        # return redirect(request.referrer)
    else:
        # user = request.args.get('nm')
        # user1 = request.args.get('nm1')
        # user1 = request.args.get('Quote_no')
        time.sleep(10)
        return redirect(url_for('success',
                                name=Quote_no + " " + Manufacturer+" " + Model + " " + Part_Number + " " + Part_Name + " " +  Material +
                                     " "  + form + " " + Alloy + " " + Temper + " " + Profile + " " + Part_Size_Thickness + " " + Part_Size_Width + " " + Part_Size_Length +
                                     " " + Part_Size_Weight + " " + Raw_Material_Thickness + " " + Raw_Material_Width + " "
                                     + Raw_Material_Length + " " + Raw_Material_Weight + " " + Metal_removal + " " + Removal_rate + " "
                                     + Machine_Hours + " " + Machine_rate + " " + Machining_price + " " + Material_dollar + " " + Material_price +
                                     " " + Treatment_Price))

        # return redirect(request.referrer)

if __name__ == '__main__':
    app.run(HOST_NAME, HOST_PORT,debug=True)