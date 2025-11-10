# GitHub Profile Analyzer (API + Python + Data Visualization)

This project analyzes any GitHub user's public profile using the **free GitHub REST API**.  
It compares developer activity, repository stats, and programming language usage.  
No authentication, no paid API keys required.

---

## 🔥 Objective
To understand developer skill patterns from their GitHub activity and present insights through:
- Repository stats
- Programming language trends
- Stars & popularity metrics
- Profile comparison reports

---

## 🧠 Tech Used
| Component | Tech |
|----------|------|
| Data Source | GitHub REST API (Free) |
| Language | Python |
| Libraries | requests, pandas, matplotlib |
| Output | Text Reports + Visualizations |

---

## 📌 How It Works
1. Input a GitHub username
2. Fetch public profile + repo list from API
3. Analyze:
   - Languages used
   - Stars & repository popularity
   - Follower/Following ratio
4. Generate:
   - Profile Summary
   - Top Repositories Table
   - Language Pie Chart

---

## 🔍 Example Users Analyzed
We compared **Linus Torvalds** (creator of Linux) with **dynamic010**.

| Metric | torvalds | dynamic010 |
|--------|---------|------------|
| Public Repos | Many (Linux contributions) | Growing portfolio |
| Followers | Extremely high (global legend) | Growing developer community |
| Primary Languages | C, C++ | Python, AI/ML Projects |
| Repo Focus | OS kernel, low-level systems | Data Analytics, Machine Learning, AI Apps |

---

## 🎨 Language Usage Visualization
The project generates a **pie chart** showing which languages the user works in most.

---

## 🔥 Top Starred Repositories Report
The project also ranks repositories by stars to identify:
- Best work
- Most popular contributions
- Community impact indicators

---

## 📦 Files in This Repository
| File | Description |
|------|-------------|
| `GitHub_Profile_Analyzer.ipynb` | Main notebook |
| `github_profile_report.txt` | Summary report output |
| `profile_language_pie.png` (optional) | Language usage chart |

---

## 📝 Resume Bullet Points
