from flask import Flask, render_template, redirect, url_for, request
app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template(home.html)

#From importing data from HTML Amount

@app.route("paymentGateway",method=["POST","GET"])
def paymentGateway():
    if request.method=="POST":
    	Amount=request.form("Amt")
		#return redirect(url_for("Amount",Amo=Amount))
	else:
		return render_template("home.html")

#funcation Definding Amount based

@app.route("/<Amo>")
def Amount(Amo):
	if Amount <= 20:
        return f"Paid: {Amount} though Gateway: CheapPaymentGateway"
    elif 21 <= Amount <= 500:
        return f"Paid: {Amount} though Gateway: ExpensivePaymentGateway"
   	 else:
        return f"Paid: {Amount} though Gateway: PremiumPaymentGateway"

#Auto Debug mode
if __name__ == '__main__':
	app.run(debug=True)