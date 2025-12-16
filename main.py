from pyscript import document

# --- GWA Calculator ---
def calculate_gwa(event):
    try:
        first_name = document.getElementById("firstName").value
        last_name = document.getElementById("lastName").value

        science = float(document.getElementById("science").value)
        math = float(document.getElementById("math").value)
        english = float(document.getElementById("english").value)
        filipino = float(document.getElementById("filipino").value)
        ict = float(document.getElementById("ict").value)
        pe = float(document.getElementById("pe").value)

        subjects = {
            "Science": science,
            "Math": math,
            "English": english,
            "Filipino": filipino,
            "ICT": ict,
            "PE": pe
        }

        weighted_sum = (science*5 + math*5 + english*5 + filipino*3 + ict*2 + pe*1)
        total_units = 21
        gwa = weighted_sum / total_units

        summary = f"Name: {first_name} {last_name}\n\nSubject Grades:\n"
        for subj, grade in subjects.items():
            summary += f"{subj}: {grade:.0f}\n"

        document.getElementById("result").innerHTML = summary.replace("\n", "<br>")
        document.getElementById("gwa").innerHTML = f"Your General Weighted Average: {gwa:.2f}"
    except:
        document.getElementById("gwa").innerHTML = "Please fill in all fields with valid numbers."

# --- Club Information ---
club_data = {
    "student_nurses": {
        "name": "Student Nurses Association",
        "description": "Develops nursing skills and leadership.",
        "meeting_time": "Monday 3-4 PM",
        "location": "Nursing Lab",
        "moderator": "Ms. Cruz",
        "members": 40,
        "category": "Medical"
    },
    "medical_technologists": {
        "name": "Medical Technology Society",
        "description": "Focuses on lab science and diagnostics.",
        "meeting_time": "Tuesday 3-4 PM",
        "location": "Medical Lab",
        "moderator": "Mr. Lim",
        "members": 32,
        "category": "Medical"
    },
    "red_cross_youth": {
        "name": "Red Cross Youth Council",
        "description": "Promotes first aid and community service.",
        "meeting_time": "Wednesday 3-4 PM",
        "location": "Room 402",
        "moderator": "Ms. Medina",
        "members": 50,
        "category": "Service"
    },
    "public_health": {
        "name": "Public Health Advocates",
        "description": "Health education and community programs.",
        "meeting_time": "Friday 3-4 PM",
        "location": "Room 405",
        "moderator": "Dr. Velasco",
        "members": 27,
        "category": "Medical"
    },
    "mental_health": {
        "name": "Mental Health Awareness Club",
        "description": "Promotes mental wellness and peer support.",
        "meeting_time": "Thursday 3-4 PM",
        "location": "Wellness Center",
        "moderator": "Ms. Fernandez",
        "members": 35,
        "category": "Wellness"
    },
    "medical_research": {
        "name": "Medical Research Society",
        "description": "Trains students in research and data analysis.",
        "meeting_time": "Saturday 9-11 AM",
        "location": "Research Room",
        "moderator": "Dr. Santos",
        "members": 20,
        "category": "Academic"
    }
}

def get_selected_club():
    return document.querySelector("#clubSelect").value

def display_club_information(event):
    selected = get_selected_club()
    display_box = document.querySelector("#clubDisplay")
    if selected == "":
        display_box.style.display = "none"
        return
    info = club_data.get(selected)
    if info:
        text = f"{info['name']}\n\nDescription: {info['description']}\nMeeting Time: {info['meeting_time']}\nLocation: {info['location']}\nAdvisor: {info['moderator']}\nMembers: {info['members']}\nCategory: {info['category']}"
        display_box.textContent = text
        display_box.style.display = "block"
    else:
        display_box.textContent = "Club information not found."
        display_box.style.display = "block"
