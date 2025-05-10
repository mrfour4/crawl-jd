# insert_jobs.py
import random
from datetime import datetime, timedelta
from mongo_config import collection  # Đảm bảo bạn có file mongo_config.py chứa cấu hình MongoDB

job_data = {
    "Software Engineer": {
        "tech": ["Python", "Java", "C#", "Git", "Docker", "Microservices", "REST APIs", "Unit Testing", "SQL", "OOP"],
        "soft": ["Problem-solving", "Teamwork", "Communication skills", "Adaptability", "Critical thinking"],
        "level": ["Intern", "Junior", "Mid-level", "Senior", "Lead", "Principal", "Manager", "Director", "VP", "CTO"]
    },
    "Backend Developer": {
        "tech": ["Node.js", "Express.js", "Java", "Python", "MySQL", "PostgreSQL", "REST API", "MongoDB", "Docker", "Redis"],
        "soft": ["Problem-solving", "Communication skills", "Analytical thinking", "Attention to detail"],
        "level": ["Intern", "Junior", "Mid-level", "Senior", "Lead", "Principal", "Manager", "Director"]
    },
    "Frontend Developer": {
        "tech": ["React.js", "JavaScript", "HTML5", "CSS3", "Vue.js", "TypeScript", "Redux", "Responsive Design", "Webpack"],
        "soft": ["Creativity", "Teamwork", "Communication skills", "Attention to detail"],
        "level": ["Intern", "Junior", "Mid-level", "Senior", "Lead", "Principal", "Manager", "Director"]
    },
    "Fullstack Developer": {
        "tech": ["Node.js", "React.js", "MongoDB", "Express.js", "HTML5", "CSS3", "Git", "Docker", "TypeScript", "GraphQL"],
        "soft": ["Versatility", "Team collaboration", "Problem-solving", "Time management"],
        "level": ["Junior", "Mid-level", "Senior", "Lead", "Principal", "Manager", "Director"]
    },
    "DevOps Engineer": {
        "tech": ["Docker", "Kubernetes", "AWS", "CI/CD", "Linux", "Terraform", "Jenkins", "Monitoring tools", "Python"],
        "soft": ["Adaptability", "Automation mindset", "Attention to detail", "Collaboration"],
        "level": ["Junior", "Mid-level", "Senior", "Lead", "Principal", "Manager", "Director"]
    },
    "Mobile Developer (Android/iOS/Flutter)": {
        "tech": ["Flutter", "React Native", "Swift", "Kotlin", "Android SDK", "iOS SDK", "Dart", "Xcode", "Firebase"],
        "soft": ["Creativity", "User-centric thinking", "Teamwork", "Debugging skills"],
        "level": ["Intern", "Junior", "Mid-level", "Senior", "Lead", "Principal"]
    },
    "QA/QC Engineer": {
        "tech": ["Selenium", "JMeter", "TestNG", "Postman", "Manual Testing", "Bug Tracking", "SQL", "API Testing"],
        "soft": ["Attention to detail", "Analytical skills", "Communication skills", "Problem-solving"],
        "level": ["Intern", "Junior", "Mid-level", "Senior", "Lead"]
    },
    "Automation Tester": {
        "tech": ["Selenium", "TestNG", "Java", "Python", "CI/CD", "API Testing", "Postman", "Jenkins", "JUnit"],
        "soft": ["Logical thinking", "Precision", "Team collaboration", "Adaptability"],
        "level": ["Junior", "Mid-level", "Senior", "Lead"]
    },
    "Manual Tester": {
        "tech": ["Test Case Design", "Bug Reporting", "Blackbox Testing", "SQL", "TestRail", "JIRA", "Excel"],
        "soft": ["Thoroughness", "Communication skills", "Critical thinking", "Problem-solving"],
        "level": ["Intern", "Junior", "Mid-level", "Senior"]
    },
    "Performance QA Engineer": {
        "tech": ["JMeter", "LoadRunner", "Gatling", "Monitoring Tools", "Java", "Python", "AWS", "Grafana", "Prometheus"],
        "soft": ["Analytical thinking", "Precision", "Communication skills", "Problem-solving"],
        "level": ["Junior", "Mid-level", "Senior", "Lead"]
    },
    "System Administrator": {
        "tech": ["Linux", "Windows Server", "Networking", "Shell Scripting", "Backup Tools", "Monitoring", "Security", "VMware"],
        "soft": ["Responsibility", "Discipline", "Problem-solving", "Documentation"],
        "level": ["Junior", "Mid-level", "Senior", "Lead", "Manager"]
    },
    "Network Engineer": {
        "tech": ["Cisco", "Switching", "Routing", "Firewall", "LAN/WAN", "Network Monitoring", "VPN", "Load Balancer"],
        "soft": ["Analytical skills", "Documentation", "Teamwork", "Communication skills"],
        "level": ["Junior", "Mid-level", "Senior", "Lead"]
    },
    "Cloud Engineer (AWS/Azure/GCP)": {
        "tech": ["AWS", "Azure", "GCP", "Terraform", "CloudFormation", "Kubernetes", "Docker", "CI/CD", "Monitoring"],
        "soft": ["Scalability mindset", "Responsibility", "Problem-solving", "Adaptability"],
        "level": ["Junior", "Mid-level", "Senior", "Lead", "Principal", "Manager", "Director"]
    },
    "Data Engineer": {
        "tech": ["Python", "ETL", "SQL", "Spark", "Kafka", "Hadoop", "Airflow", "AWS", "BigQuery"],
        "soft": ["Analytical skills", "Detail-oriented", "Communication", "Teamwork"],
        "level": ["Junior", "Mid-level", "Senior", "Lead", "Principal", "Manager"]
    },
    "Data Scientist": {
        "tech": ["Python", "Pandas", "Scikit-learn", "TensorFlow", "SQL", "Jupyter", "Data Visualization", "ML Models"],
        "soft": ["Analytical skills", "Problem-solving", "Curiosity", "Presentation skills"],
        "level": ["Junior", "Mid-level", "Senior", "Lead", "Principal", "Manager", "Director"]
    },
    "Business Analyst (BA)": {
        "tech": ["Excel", "SQL", "BI Tools", "Data Visualization", "UML", "JIRA", "Confluence", "Wireframing Tools"],
        "soft": ["Communication", "Critical thinking", "Documentation", "Presentation"],
        "level": ["Junior", "Mid-level", "Senior", "Lead", "Manager"]
    },
    "Project Manager (IT PM)": {
        "tech": ["JIRA", "Confluence", "MS Project", "Agile", "Scrum", "Gantt Charts", "Risk Management"],
        "soft": ["Leadership", "Time management", "Conflict resolution", "Planning"],
        "level": ["Mid-level", "Senior", "Lead", "Manager", "Director", "VP"]
    },
    "UI/UX Designer": {
        "tech": ["Figma", "Sketch", "Adobe XD", "Photoshop", "Prototyping Tools", "HTML/CSS", "User Research", "Design Systems"],
        "soft": ["Creativity", "Empathy", "Attention to detail", "Communication"],
        "level": ["Intern", "Junior", "Mid-level", "Senior", "Lead", "Manager", "Director"]
    },
    "IT Support / Helpdesk": {
        "tech": ["Windows", "MacOS", "Office 365", "Ticketing System", "Networking Basics", "Remote Desktop", "Active Directory"],
        "soft": ["Patience", "Customer service", "Problem-solving", "Communication"],
        "level": ["Intern", "Junior", "Mid-level", "Senior"]
    },
    "Cybersecurity Engineer": {
        "tech": ["Network Security", "Firewalls", "IDS/IPS", "SIEM", "Penetration Testing", "Encryption", "Python", "Linux"],
        "soft": ["Ethical mindset", "Analytical thinking", "Attention to detail", "Responsibility"],
        "level": ["Junior", "Mid-level", "Senior", "Lead", "Principal", "Manager", "Director"]
    }
}

# Thành phố và tỉnh
major_cities = ["Hà Nội", "Thành phố Hồ Chí Minh", "Đà Nẵng", "Hải Phòng", "Cần Thơ", "Huế"]
other_provinces = [
    "An Giang", "Bà Rịa – Vũng Tàu", "Bạc Liêu", "Bắc Giang", "Bắc Kạn", "Bắc Ninh", "Bến Tre", "Bình Dương", 
    "Bình Định", "Bình Phước", "Bình Thuận", "Cà Mau", "Cao Bằng", "Đắk Lắk", "Đắk Nông", "Điện Biên", "Đồng Nai", 
    "Đồng Tháp", "Gia Lai", "Hà Giang", "Hà Nam", "Hà Tĩnh", "Hải Dương", "Hậu Giang", "Hòa Bình", "Hưng Yên", 
    "Khánh Hòa", "Kiên Giang", "Kon Tum", "Lai Châu", "Lâm Đồng", "Lạng Sơn", "Lào Cai", "Long An", "Nam Định", 
    "Nghệ An", "Ninh Bình", "Ninh Thuận", "Phú Thọ", "Phú Yên", "Quảng Bình", "Quảng Nam", "Quảng Ngãi", 
    "Quảng Ninh", "Quảng Trị", "Sóc Trăng", "Sơn La", "Tây Ninh", "Thái Bình", "Thái Nguyên", "Thanh Hóa", 
    "Tiền Giang", "Trà Vinh", "Tuyên Quang", "Vĩnh Long", "Vĩnh Phúc", "Yên Bái"
]
provinces = major_cities * 3 + other_provinces

def random_date_last_two_years():
    start_date = datetime.now() - timedelta(days=730)
    random_days = random.randint(0, 729)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

def generate_job_doc():
    job_title_base = random.choice(list(job_data.keys()))
    job_info = job_data[job_title_base]
    tech_list = job_info["tech"]
    soft_list = job_info["soft"]
    level = random.choice(job_info["level"])
    location = random.choice(provinces)
    update_date = random_date_last_two_years()

    formatted_title = f"[{location}] {level} {job_title_base} ({update_date})"
    
    return {
        "update_date": update_date,
        "job_title": formatted_title,
        "location": location,
        "seniority_level": level,
        "soft_skills": random.sample(soft_list, min(random.randint(3, 5), len(soft_list))),
        "techn_stack": random.sample(tech_list, min(random.randint(5, 10), len(tech_list)))
    }

# Cấu hình số lượng
BATCH_SIZE = 10000
TOTAL_DOCUMENTS = 1_000_000

# Thêm dữ liệu theo lô
for batch_start in range(0, TOTAL_DOCUMENTS, BATCH_SIZE):
    batch = [generate_job_doc() for _ in range(BATCH_SIZE)]
    collection.insert_many(batch)
    print(f"✅ Inserted batch {batch_start // BATCH_SIZE + 1} ({batch_start + BATCH_SIZE} docs)")
