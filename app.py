import requests
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("GitHub Profile Analyzer (Free API)")

username = st.text_input("Enter GitHub Username:", "")

if username:
    user_url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos"

    user_data = requests.get(user_url).json()
    repos_data = requests.get(repos_url).json()

    if "message" in user_data:
        st.error("❌ User not found. Try another username.")
    else:
        st.subheader("👤 Profile Information")
        st.write(f"**Name:** {user_data.get('name')}")
        st.write(f"**Bio:** {user_data.get('bio')}")
        st.write(f"**Followers:** {user_data.get('followers')}")
        st.write(f"**Public Repos:** {user_data.get('public_repos')}")

        repo_list = []
        for repo in repos_data:
            repo_list.append([repo["name"], repo["stargazers_count"], repo["language"]])

        df = pd.DataFrame(repo_list, columns=["Repository", "Stars", "Language"])

        st.subheader("📦 Repository Overview")
        st.dataframe(df)

        st.subheader("⭐ Top Starred Repositories")
        top_repos = df.sort_values(by="Stars", ascending=False).head(5)
        st.table(top_repos)

        st.subheader("🎨 Language Usage Distribution")
        lang_summary = df["Language"].value_counts()

        fig, ax = plt.subplots()
        lang_summary.plot(kind="pie", autopct="%1.1f%%", ax=ax)
        ax.set_ylabel("")
        st.pyplot(fig)

        st.subheader("📝 Summary")
        st.write(f"{username} mainly works with: **{lang_summary.index[0]}**")
