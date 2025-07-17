from flask import Flask, render_template, jsonify, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, db
import time

app = Flask(__name__)

# 🔹 Firebase Configuration
cred = credentials.Certificate("fir-192da-firebase-adminsdk-fbsvc-1763627e0f.json")  
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fir-192da-default-rtdb.firebaseio.com/'
})

# 🔹 Home Route → Landing Page
@app.route('/')
def landing_page():
    return render_template('landing.html')

# 🔹 Doctor Login Route
@app.route('/doctor-login', methods=["GET", "POST"])
def doctor_login():
    if request.method == "POST":
        doctor_name = request.json.get("doctorName")
        password = request.json.get("password")

        if doctor_name and password:  
            return jsonify({"success": True, "redirect": "/dashboard"})  
        return jsonify({"error": "Invalid credentials"}), 401

    return render_template('doctor_login.html')

# 🔹 Patient Login Route
@app.route('/patient-login', methods=["GET", "POST"])
def patient_login():
    if request.method == "POST":
        patient_name = request.json.get("patientName")
        patient_tag = request.json.get("patientTag")

        if patient_name and patient_tag:
            return jsonify({"success": True, "redirect": f"/user-profile?patient={patient_tag}"})
        return jsonify({"error": "Invalid credentials"}), 401

    return render_template('patient_login.html')

# 🔹 Fetch Users for Dashboard
@app.route('/api/user-dashboard')
def get_users():
    ref_users = db.reference("users")
    users_data = ref_users.get() or {}

    users_list = []
    for user_id, user_info in users_data.items():
        users_list.append({
            "name": user_info.get("name", "Unknown"),
            "patient": user_info.get("patient", "N/A"),
            "activity": user_info.get("Activity", "No activity recorded"),
            "latest_score": list(user_info.get("Score", {}).values())[-1] if user_info.get("Score") else "N/A"
        })
    
    return jsonify(users_list)

# 🔹 Fetch User Profile Data
@app.route('/api/user-info')
def get_user_info():
    patient = request.args.get("patient")
    if not patient:
        return jsonify({"error": "Patient ID is required"}), 400

    ref_users = db.reference("users")
    users_data = ref_users.get() or {}

    found_user = next((user for user in users_data.values() if user.get("patient") == patient), None)

    if found_user:
        return jsonify({
            "name": found_user.get("name", "N/A"),
            "patient": found_user.get("patient", "N/A"),
            "dob": found_user.get("dob", "N/A"),
            "admission_date": found_user.get("admission_date", "N/A"),
            "activity": found_user.get("Activity", "N/A"),
            "score": list(found_user.get("Score", {}).values())[-1] if found_user.get("Score") else "N/A",
            "timestamp": found_user.get("timestamp", int(time.time()))
        })

    return jsonify({"error": "User not found"}), 404

# 🔹 Route for User Profiles
@app.route('/user-profile')
def user_profile():
    patient = request.args.get("patient", "P01")  # Default to P01 if no patient is specified
    return render_template('user_profile.html', patient=patient)

@app.route('/user-profile1')
def user_profile1():
    # Always redirect P02 to P01's profile
    return redirect(url_for('user_profile', patient="P01"))
# 🔹 Dashboard Route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# 🔹 Fetch Scores for User
@app.route('/api/user-scores')
def get_user_scores():
    patient = request.args.get("patient")

    if not patient:
        return jsonify({"error": "Patient ID is required"}), 400

    ref_users = db.reference("users")
    ref_new_users = db.reference("new_users")  # New User Table

    users_data = ref_users.get() or {}
    new_users_data = ref_new_users.get() or {}

    # Fetch user info from "users"
    user_info = next((user for user in users_data.values() if user.get("patient") == patient), None)

    # Fetch new user scores (if patient exists in "new_users")
    new_user_info = next((user for user in new_users_data.values() if user.get("patient") == patient), None)

    all_scores = []

    if user_info:
        user_scores = user_info.get("Score", {})
        all_scores.extend([{"timestamp": int(time.time()), "score": score} for score in user_scores.values()])

    if new_user_info:
        new_user_scores = new_user_info.get("Score", {})
        all_scores.extend([{"timestamp": int(time.time()), "score": score} for score in new_user_scores.values()])

    if not all_scores:
        return jsonify({"error": "No score data found"}), 404

    return jsonify(all_scores)


if __name__ == '__main__':
    app.run(debug=True)
