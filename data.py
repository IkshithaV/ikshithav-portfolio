"""
============================================================
 PORTFOLIO DATA FILE
============================================================
This is the ONLY file you should normally need to edit.
Update your info here, then re-run `python generate.py`
to rebuild index.html.
============================================================
"""

PROFILE = {
    "name": "Vuppala Ikshitha",
    "role": "AI & Data Science Undergraduate",
    "tagline": "Building machine learning systems with an eye on security.",
    "location": "Hyderabad, India",
    "email": "ikshithavuppala@gmail.com",
    "phone": "+91 9959552012",
    "linkedin": "https://linkedin.com/in/vuppala-ikshitha",  # update with your real LinkedIn URL
    "github": "https://github.com/IkshithaV",
    "summary": (
        "AI & Data Science undergraduate with hands-on experience in machine "
        "learning projects including fake account detection and recommendation "
        "systems. Proficient in Python, data analysis, and model building using "
        "Logistic Regression and Random Forest. Experienced in deploying ML "
        "applications using Streamlit with a strong interest in AI and cybersecurity."
    ),
}

# Terminal-style typing lines shown in the hero section
TERMINAL_LINES = [
    "whoami",
    "> vuppala_ikshitha — AI/ML Engineer in training",
    "cat interests.txt",
    "> machine learning, cybersecurity, recommendation systems",
    "status --check",
    "> [ READY TO BUILD ]",
]

EDUCATION = [
    {
        "degree": "B.Tech in Artificial Intelligence & Data Science",
        "school": "Koneru Lakshmaiah Education Foundation, Vijayawada, India",
        "period": "May 2022 – May 2026",
        "score": "GPA: 8.8 / 10",
    },
    {
        "degree": "Intermediate (MPC)",
        "school": "Sri Chaitanya Junior College, Hyderabad, India",
        "period": "May 2020 – May 2022",
        "score": "GPA: 7.0 / 10",
    },
]

EXPERIENCE = [
    {
        "title": "Palo Alto Cybersecurity Virtual Internship",
        "org": "AICTE",
        "period": "Oct 2024 – Dec 2024",
        "points": [
            "Completed AICTE-certified virtual internship in cybersecurity in collaboration with Palo Alto Networks, gaining foundational knowledge in network security, firewalls, and threat prevention.",
            "Acquired hands-on experience with cybersecurity concepts such as malware analysis, phishing detection, and endpoint protection using industry-relevant tools and simulations.",
            "Learned the fundamentals of next-generation firewall (NGFW) operations, including policy configuration and traffic monitoring.",
        ],
    },
]

PROJECTS = [
    {
        "name": "Fake Account Detection on Instagram",
        "tech": ["Python", "Machine Learning", "Pandas", "NumPy", "Scikit-learn", "Streamlit"],
        "points": [
            "Developed a machine learning-based system to detect fake Instagram accounts using profile and activity-based features.",
            "Performed data preprocessing, feature engineering, and exploratory data analysis (EDA) to improve model reliability.",
            "Implemented and compared Logistic Regression and Random Forest classifiers to analyze performance and improve prediction accuracy.",
            "Built an interactive Streamlit web application that allows users to input profile details and view real-time predictions of whether an account is fake or genuine.",
        ],
        "link": "",  # add a live demo or GitHub link if you have one
    },
    {
        "name": "Amazon End-to-End Recommendation System",
        "tech": ["Python", "Pandas", "NumPy", "Streamlit"],
        "points": [
            "Developed an end-to-end product recommendation system using Amazon product and user review data.",
            "Implemented content-based filtering and collaborative filtering techniques to generate personalized recommendations.",
            "Evaluated recommendation quality using similarity scores and user relevance metrics.",
            "Deployed the application with an interactive UI to recommend products based on user input.",
        ],
        "link": "",
    },
]

CERTIFICATIONS = [
    "Certified Cloud Practitioner – AWS",
    "Certified AI Associate – Salesforce",
    "Certified Essentials RPA Professional – Automation Anywhere",
]

SKILLS = {
    "Programming Languages": ["C", "Python", "SQL"],
    "Tools": ["GitHub", "VS Code", "PyCharm", "MySQL", "Excel", "Power BI"],
    "Machine Learning": ["Classification", "Recommendation Systems", "Feature Engineering", "Model Evaluation"],
    "Soft Skills": ["Teamwork", "Adaptability", "Time Management"],
}
