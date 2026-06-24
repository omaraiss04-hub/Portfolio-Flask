import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 1. المسار الرئيسي (الصفحة الرئيسية)
@app.route('/')
def home():
    return render_template('index.html')

# 2. مسار صفحة تفاصيل مشروع الفلاسک (يجب أن يكون هنا قبل سطر التشغيل!)
@app.route('/project/flask-backend')
def flask_project_detail():
    return render_template('project_flask.html')

# 3. مسار استقبال وإرسال الرسائل
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    
    # التحقق من أن جميع الحقول ليست فارغة (Validation)
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    message = data.get('message', '').strip()

    if not name or not email or not message:
        return jsonify({"status": "error", "message": "Alle Felder sind erforderlich!"}), 400
    
    # طباعة الرسالة المستلمة داخل الـ Terminal الخاص بـ VS Code
    print("\n   --- Neue Nachricht erhalten ---")
    print(f"   Name:      {name}")
    print(f"   E-Mail:    {email}")
    print(f"   Nachricht: {message}")
    print(f"   ---------------------------------\n")
    
    return jsonify({"status": "success", "message": "Nachricht erfolgreich empfangen!"})

# مسار صفحة تفاصيل مشروع الأردوينو والـ RFID
@app.route('/project/rfid-door-lock')
def rfid_project_detail():
    return render_template('project_rfid.html')
# 4. سطر تشغيل السيرفر (يجب أن يكون دائماً هو آآآخر سطر في الملف)
if __name__ == '__main__':
    app.run(debug=True)