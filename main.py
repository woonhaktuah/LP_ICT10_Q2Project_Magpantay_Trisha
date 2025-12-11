from pyscript import document

def compute_average(event):
    english = float(document.getElementById("english").value)
    math = float(document.getElementById("math").value)
    science = float(document.getElementById("science").value)
    social_studies = float(document.getElementById("socstudies").value)
    filipino = float(document.getElementById("filipino").value)
    ict = float(document.getElementById("ict").value)

    total = english + math + science + social_studies + filipino + ict
    average = total / 6

    first = document.getElementById("first").value
    last = document.getElementById("last").value

    document.getElementById("name").innerText = f"Name: {first} {last}"
    document.getElementById("output").innerText = f"Your Computed Average is {round(average, 2)}"