from flask import Flask,render_template,request,make_response,session
from DB import DB
app = Flask(__name__)
# app.secret_key="bsjvhusdhg5565645"

@app.route('/')
def homePage():
    return  render_template("Home.html")


@app.route('/vCust')
def VCustomer():
    return  render_template("ViewCustomerForm.html")


@app.route("/viewCustomer", methods=["POST"])
def viewCustomerFormHandler():
    try:
        email=request.form["email"]
        name=request.form["name"]
        cust=[email,name]
        db=DB("localhost","root","jamshaid1818@18","bankdatabase")
        found,data=db.searchCustomer(cust)
        print(data)
        if found:
            return  render_template("ShowCustomer.html",dataFound=data)
        else:
            message="No such record Exsist !!"
            return render_template("ViewCustomerForm.html" ,message=message)
            
    except Exception as e:
        message=str(e)
        return render_template("ViewCustomerForm.html" ,message=message)
    

@app.route('/transMoney')
def showForm():
    return  render_template("TransferMoneyForm.html")

@app.route('/transferMoney', methods=["POST"])
def transferMoney():
    try:
        email=request.form["email"]
        name=request.form["name"]
        payment=request.form["amount"]
        cont=[email,name,payment]

        db=DB("localhost","root","jamshaid1818@18","bankdatabase")
        trans=db.transferMoney(cont)
        if trans:
            message="Amount transferred successfully!!!!"
            return  render_template("Dashboard.html", message=message)
        else:
            message="Invalid name or email "
            return render_template("TransferMoneyForm.html" ,message=message)
            
    except Exception as e:
        message="Registation failed "+str(e)
        return render_template("TransferMoneyForm.html" ,message=message)


# main function
if __name__ == '__main__':
    app.run()


