from flask import Flask, render_template, request,redirect,url_for
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))

    state = db.Column(db.String(50))
    city = db.Column(db.String(50))

    venue = db.Column(db.String(200))
    design = db.Column(db.String(100))

    guests = db.Column(db.String(20))
    date = db.Column(db.String(20))
    time = db.Column(db.String(20))

    message = db.Column(db.Text)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'jainabk595@gmail.com'
app.config['MAIL_PASSWORD'] = 'ylmxvxeofysexwqe'
app.config['MAIL_USE_TLS'] = True

mail = Mail(app)

# =========================
# HOME PAGE
# =========================
@app.route('/')
def home():
    return render_template('index.html')


# =========================
# CONTACT PAGE
# =========================
@app.route('/contact')
def contact():
    return render_template('contact.html')


# =========================
# VIEW DETAILS PAGE (from trending cards)
# =========================
@app.route('/bridal-full-hand')
def bridal_full_hand():
    return render_template('bridal_mehendi.html')


# =========================
# SERVICES PAGES (Dropdown Navigation)
# =========================

@app.route('/bridal_mehendi')
def bridal():
    return render_template('bridal_mehendi.html')


@app.route('/party_mehendi')
def party():
    return render_template('party_mehendi.html')


@app.route('/engagement_mehendi')
def engagement():
    return render_template('engagement_mehendi.html')


@app.route('/festival_mehendi')
def festival():
    return render_template('festival_mehendi.html')

# services
@app.route('/services')
def services():
    return render_template('services.html')

# designs
@app.route('/designs')
def designs():
    return render_template('designs.html')

# collections
@app.route("/collections")
def collections_page():

    collection_data = [
         {
            "id": "bridal",
            "title": "Bridal Mehendi",
            "designs": [
                {"img": "bridal1.jpg", "price": "₹249"},
                {"img": "bridal2.jpg", "price": "₹534"},
                {"img": "bridal3.jpg", "price": "₹298"},
                {"img": "bridal4.jpg", "price": "₹1465"},
                {"img": "bridal10.jpg", "price": "₹1643"},
                {"img": "bridal6.jpg", "price": "₹876"},
                {"img": "bridal7.jpg", "price": "₹897"},
                {"img": "bridal8.jpg", "price": "₹654"},
                {"img": "bridal9.jpg", "price": "₹324"},
                {"img": "bridal10.jpg", "price": "₹658"},
            ]
        },
        {
            "id": "party",
            "title": "Party Mehendi",
            "designs": [
                {"img": "party1.jpg", "price": "₹869"},
                {"img": "party2.jpg", "price": "₹899"},
                {"img": "e3.jpg", "price": "₹1099"},
                {"img": "party4.jpg", "price": "₹799"},
                {"img": "party5.jpg", "price": "₹899"},
                {"img": "party6.jpg", "price": "₹436"},
                {"img": "party7.jpg", "price": "₹1099"},
                {"img": "party8.jpg", "price": "₹879"},
                {"img": "party9.jpg", "price": "₹899"},
                {"img": "party10.jpg", "price": "₹478"},
            ]
        },
        {
            "id": "ring",
            "title": "Engagement Mehendi",
            "designs": [
                {"img": "e1.jpg", "price": "₹1499"},
                {"img": "e2.jpg", "price": "₹1574"},
                {"img": "e3.jpg", "price": "₹1399"},
                {"img": "e4.jpg", "price": "₹1699"},
                {"img": "e5.jpg", "price": "₹1499"},
                {"img": "e6.jpg", "price": "₹1599"},
                {"img": "e7.jpg", "price": "₹1399"},
                {"img": "e8.jpg", "price": "₹1699"},
                {"img": "e9.jpg", "price": "₹1399"},
                {"img": "e10.jpg", "price": "₹1699"},
            ]
        },
        {
            "id": "arabic",
            "title": "Arabic Mehendi",
            "designs": [
                {"img": "a1.jpg", "price": "₹2499"},
                {"img": "a2.jpg", "price": "₹2699"},
                {"img": "a3.jpg", "price": "₹2386"},
                {"img": "a4.jpg", "price": "₹2599"},
                {"img": "a5.jpg", "price": "₹2034"},
                {"img": "a6.jpg", "price": "₹2499"},
                {"img": "a7.jpg", "price": "₹2699"},
                {"img": "a8.jpg", "price": "₹2685"},
                {"img": "a9.jpg", "price": "₹2599"},
                {"img": "a10.jpg", "price": "₹2086"},
            ]
        },
        {
            "id": "indo_arabic",
            "title": "Indo Arabic Mehendi",
            "designs": [
                {"img": "i1.jpg", "price": "₹346"},
                {"img": "i2.jpg", "price": "₹976"},
                {"img": "i3.jpg", "price": "₹789"},
                {"img": "i4.jpg", "price": "₹876"},
                {"img": "i5.jpg", "price": "₹269"},
                {"img": "i6.jpg", "price": "₹947"},
                {"img": "i7.jpg", "price": "₹939"},
                {"img": "i8.jpg", "price": "₹969"},
                {"img": "i9.jpg", "price": "₹757"},
                {"img": "e7.jpg", "price": "₹948"},
            ]
        },{
            "id": "indian",
            "title": "Indian Mehendi",
            "designs": [
                {"img": "y1.jpg", "price": "₹758"},
                {"img": "y2.jpg", "price": "₹973"},
                {"img": "y3.jpg", "price": "₹947"},
                {"img": "y4.jpg", "price": "₹654"},
                {"img": "y5.jpg", "price": "₹868"},
                {"img": "y6.jpg", "price": "₹853"},
                {"img": "y7.jpg", "price": "₹980"},
                {"img": "y8.jpg", "price": "₹479"},
                {"img": "y9.jpg", "price": "₹657"},
                {"img": "y10.jpg", "price": "₹689"},
            ]
        },{
            "id": "pakistani",
            "title": "Pakistani Mehendi",
            "designs": [
                {"img": "p1.jpg", "price": "₹2499"},
                {"img": "p2.jpg", "price": "₹2699"},
                {"img": "p3.jpg", "price": "₹2899"},
                {"img": "p4.jpg", "price": "₹2578"},
                {"img": "p5.jpg", "price": "₹2799"},
                {"img": "p6.jpg", "price": "₹2499"},
                {"img": "p7.jpg", "price": "₹2699"},
                {"img": "p8.jpg", "price": "₹27568"},
                {"img": "p9.jpg", "price": "₹2599"},
                {"img": "bridal2.jpg", "price": "₹2675"},
            ]
        },{
            "id": "festival",
            "title": "Festival Mehendi",
            "designs": [
                {"img": "f1.jpg", "price": "₹2499"},
                {"img": "f2.jpg", "price": "₹2699"},
                {"img": "f3.jpg", "price": "₹2457"},
                {"img": "f4.jpg", "price": "₹2089"},
                {"img": "f5.jpg", "price": "₹2799"},
                {"img": "f6.jpg", "price": "₹967"},
                {"img": "w3.jpg", "price": "₹2699"},
                {"img": "f8.jpg", "price": "₹1756"},
                {"img": "f9.jpg", "price": "₹2599"},
                {"img": "f10.jpg", "price": "₹1987"},
            ]
        },{
            "id": "moroccan",
            "title": "Moroccon Mehendi",
            "designs": [
                {"img": "m1.jpg", "price": "₹2499"},
                {"img": "m2.jpg", "price": "₹2079"},
                {"img": "m3.jpg", "price": "₹2899"},
                {"img": "m4.jpg", "price": "₹2599"},
                {"img": "m5.jpg", "price": "₹1978"},
                {"img": "m6.jpg", "price": "₹2499"},
                {"img": "m7.jpg", "price": "₹109"},
                {"img": "m8.jpg", "price": "₹2899"},
                {"img": "m9.jpg", "price": "₹568"},
                {"img": "m10.jpg", "price": "₹986"},
            ]
        },{
            "id": "portrait",
            "title": "Portrait Mehendi",
            "designs": [
                {"img": "z1.jpg", "price": "₹2499"},
                {"img": "z2.jpg", "price": "₹2699"},
                {"img": "z3.jpg", "price": "₹1867"},
                {"img": "z4.jpg", "price": "₹986"},
                {"img": "z5.jpg", "price": "₹2799"},
                {"img": "z6.jpg", "price": "₹2499"},
                {"img": "z7.jpg", "price": "₹753"},
                {"img": "z8.jpg", "price": "₹2899"},
                {"img": "z9.jpg", "price": "₹867"},
                {"img": "z10.jpg", "price": "₹2799"},
            ]
        },{
            "id": "african",
            "title": "African Mehendi",
            "designs": [
                {"img": "r1.jpg", "price": "₹2499"},
                {"img": "r2.jpg", "price": "₹2699"},
                {"img": "r3.jpg", "price": "₹2899"},
                {"img": "r4.jpg", "price": "₹2599"},
                {"img": "r5.jpg", "price": "₹2799"},
                {"img": "r6.jpg", "price": "₹2499"},
                {"img": "r7.jpg", "price": "₹2699"},
                {"img": "r8.jpg", "price": "₹2899"},
                {"img": "r9.jpg", "price": "₹2599"},
                {"img": "r10.jpg", "price": "₹2799"},
            ]
        },{
            "id": "western",
            "title": "Western Mehendi",
            "designs": [
                {"img": "w1.jpg", "price": "₹2499"},
                {"img": "w2.jpg", "price": "₹8578"},
                {"img": "w3.jpg", "price": "₹986"},
                {"img": "w4.jpg", "price": "₹2599"},
                {"img": "w5.jpg", "price": "₹2799"},
                {"img": "w6.jpg", "price": "₹467"},
                {"img": "w7.jpg", "price": "₹2699"},
                {"img": "w8.jpg", "price": "₹9875"},
                {"img": "e8.jpg", "price": "₹2599"},
                {"img": "w10.jpg", "price": "₹789"},
            ]
        } 
    ]
    return render_template("collections.html", collections=collection_data)



# ✅ PASTE HERE 👇


    


@app.route('/about')
def about():
    return render_template('about.html')
    # =========================
    # 1. EMAIL TO USER
    # =========================
    
   
@app.route('/book', methods=['POST'])
def book_form():
    data = Booking(
        name=request.form['name'],
        phone=request.form['phone'],
        email=request.form['email'],
        state=request.form['state'],
        venue=request.form['venue'],
        design=request.form['design'],
        guests=request.form['guests'],
        date=request.form['date'],
        time=request.form['time'],
    )

    db.session.add(data)
    db.session.commit()

    # ✅ EMAIL CODE (your existing)
    user_msg = Message(
        subject="Booking Confirmed",
        sender=app.config['MAIL_USERNAME'],
        recipients=[request.form['email']]
    )

    user_msg.body = f"""
Hi {request.form['name']},

Your Mehendi booking is confirmed!
"""

    mail.send(user_msg)

    return redirect('/?success=true')

# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=True)