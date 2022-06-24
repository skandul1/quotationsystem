from flask import Flask, redirect, url_for, request
app = Flask(__name__)
temp=[]
@app.route('/success/<name>')
def success(name):
    a=name
    return 'quote data is  %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    # print(temp)
    if request.method == 'POST':
        # user=request.form['nm']
        # user1 = request.form['nm1']
        Quote_no = request.form['Quote_no']
        Part_Number=request.form['Part_Number']
        Part_Name = request.form['Part_Name']
        Alloy = request.form['Alloy']
        Temper=request.form['Temper']
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
        temp.append(Part_Number)
        temp.append(Part_Name)
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
        # temp.append()
        # temp.append()
        print(temp)
        # user1=request.form['nm1']
        return redirect(url_for('success',name = Quote_no + " " + Part_Number + " " + Part_Name + " " + Alloy + " "+ Temper + " "+ Profile + " " + Part_Size_Thickness + " " + Part_Size_Width + " " + Part_Size_Length +
         " " + Part_Size_Weight + " " + Raw_Material_Thickness + " " + Raw_Material_Width + " "
          + Raw_Material_Length + " " + Raw_Material_Weight + " " + Metal_removal + " " + Removal_rate + " " + 
          Machine_Hours + " " + Machine_rate + " " + Machining_price + " " + Material_dollar + " " + Material_price + " " + Treatment_Price))
    else:
        # user = request.args.get('nm')
        # user1 = request.args.get('nm1')
        # user1 = request.args.get('Quote_no')
        return redirect(url_for('success',name = Quote_no + " "+ Part_Number + " " + Part_Name + " " + Alloy + " "+ Temper + " "+Profile + " "+ Part_Size_Thickness + " " + Part_Size_Width + " " + Part_Size_Length + 
            " " + Part_Size_Weight + " " + Raw_Material_Thickness + " " + Raw_Material_Width + " " 
            + Raw_Material_Length + " " + Raw_Material_Weight + " " + Metal_removal + " " + Removal_rate + " " 
            + Machine_Hours + " " + Machine_rate + " " + Machining_price + " " + Material_dollar + " " + Material_price + " " + Treatment_Price))
    

if __name__ == '__main__':
    app.run(debug = True)