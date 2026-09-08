import pandas as pd
import streamlit as st
from database import *


st.set_page_config(
    page_title="Psychology Research Portal",
    page_icon="🧠",
    layout="wide"
)

initialize_database()





with st.form("participant_form"):
    st.subheader("Participant Information")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name")
    with col2:
        age = st.number_input("Age", min_value = 1, max_value = 120, step = 1)
    gender = st.radio(
        "Gender",
        ["Male", "Female", "Other"],
        horizontal=True 
    )
    education = st.selectbox(
        "Education Level",
        ["High School", "Bachelor's Degree", "Master's Degree", "PhD", "Other"]
    )
    submitted = st.form_submit_button("➕ Add Participant", type="primary")
    if submitted:
        if name and age and gender and education:
            add_participant(name, age, gender, education)
            st.success(f"Participant {name} added successfully!")
        else:
            st.error("Please fill in all fields before adding a participant.")
    st.divider()






    # st.subheader("📋 Registered Participants")

    # search = st.text_input( "🔎 Search participants", placeholder = "Search by name...")
    # rows = get_participants(search)

    # df = pd.DataFrame(rows, columns=["ID", "Name", "Age", "Gender", "Education"])
    # st.dataframe(df, width = "stretch", hide_index = True)

    # #   Delete
    # st.divider()
    # st.subheader("🗑️ Delete Participant")

    # participant_id = st.number_input("Enter Participant ID to delete", min_value=1, step=1)
    # if st.button("Delete Participant", type = "secondary"):
    #     delete_participant(participant_id)
    #     st.success(f"Participant with ID {participant_id} deleted successfully!")
    #     st.rerun()

    # #   update
    # st.divider()
    # st.subheader("✏️ Update Participant Information")
    # update_id = st.number_input("Enter Participant ID to update", min_value=1, step=1, key = "update_id")

    # new_name = st.text_input("New Name",key = "new_name")
    # new_age = st.number_input("New Age", min_value=0, max_value=120, step=1, key = "new_age")

    # if st.button("Update Participant", type = "secondary"):
    #     if new_name and new_age:
    #         conn.execute(
    #             """
    #             UPDATE participants
    #             SET name = ?, age = ?
    #             WHERE id = ?
    #             """,
    #             (new_name, new_age, update_id)
    #         )
    #         conn.commit()
    #         st.success(f"Participant with ID {update_id} updated successfully!")
    #         st.rerun()
    #     else:
    #         st.warning("Please provide both a new name and a new age to update the participant.")

