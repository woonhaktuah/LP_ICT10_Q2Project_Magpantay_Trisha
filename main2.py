from pyscript import document

clubs = {
    "Robotics Club": {
        "Description": "Design, build, and program robots for competitions.",
        "Meeting Time": "Every Monday 2:30–4:30 PM",
        "Location": "Computer Lab",
        "Advisor": "Mr. Kim",
        "Number of Members": 16,
        "Category": "Academic"
    },
    "Communication Arts Club": {
        "Description": "Express creativity through writing, acting, and public speaking.",
        "Meeting Time": "Every Thursday 2:00-4:00 PM",
        "Location": "Room 204",
        "Advisor": "Mr. Myung",
        "Number of Members": 19,
        "Category": "Academic"
    },
    "MathSci Guild": {
        "Description": "Develop mathematical and scientific skills through competitions and projects.",
        "Meeting Time": "Every Tuesday 2:00–4:00 PM",
        "Location": "Room 103 or Science Lab",
        "Advisor": "Mr. Kim",
        "Number of Members": 18,
        "Category": "Academic"
    },
    "Dance Club": {
        "Description": "Engage in creating choreography and performing in dance competitions.",
        "Meeting Time": "Every Wednesday 2:30–4:30 PM",
        "Location": "Dance Studio",
        "Advisor": "Mr. Lee",
        "Number of Members": 15,
        "Category": "Extracurricular"
    },
    "Music Ensemble": {
        "Description": "Perform musical pieces during events using vocal and instrumental arrangements.",
        "Meeting Time": "Every Monday 2:30–4:30 PM",
        "Location": "Music Room",
        "Advisor": "Mr. Han",
        "Number of Members": 20,
        "Category": "Extracurricular"
    },
    "Culinary Arts Club": {
        "Description": "Explore culinary techniques and cater events.",
        "Meeting Time": "Every Wednesday 2:30–4:30 PM",
        "Location": "TLE Lab",
        "Advisor": "Mr. Park",
        "Number of Members": 17,
        "Category": "Extracurricular"
    }
}

def show_info(event):
    select = document.getElementById("club-select")
    chosen = select.value
    
    info = clubs[chosen]
    
    output = f"""{chosen}
Description: {info['Description']}
Meeting Time: {info['Meeting Time']}
Location: {info['Location']}
Advisor: {info['Advisor']}
Number of Members: {info['Number of Members']}
Category: {info['Category']}"""
    
    document.getElementById("output-box").innerText = output