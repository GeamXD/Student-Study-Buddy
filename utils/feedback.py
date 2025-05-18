import streamlit as st
import pandas as pd
from utils.database import feedback_collection
from dotenv import load_dotenv; load_dotenv()

st.subheader("Provide feedback to app developer")

def handle_feedback(rating: int, feed_back: str, user:str):
    feedback_collection.insert_one({
        "user_id": user,
        "rating" : rating,
        "feedback": feed_back
    })
    

if not st.experimental_user.is_logged_in:
    st.info("Kindly note that you are giving feedback as an anonymous user, you can also login (Go back to Home page) to do that so that we can proper keep track of things")
    with st.form("feebback_offline"):
        user = st.text_input("Please supply a name/nickname (optional)")
        rating = st.feedback(options="stars")
        feedback = st.text_input("Provide detailed feedback (optional)")
        
        btn_offline = st.form_submit_button("Submit Feedback")
        with st.spinner("Submitting feedback ..."):
            if btn_offline:
                if not user:
                    user = "Anonymous"
                if not feedback:
                    feedback = "No detailed feedback supplied"
                try:
                    if rating:
                        handle_feedback(rating=rating+1, feed_back=feedback, user=user)
                        st.success("Feedback submitted successfully. Thank you.")
                    else:
                        st.error("Supplying the star rating is compulsory")
                except:
                    st.error("Error encountered while trying to submit feedback, try again")
            
else:
    if not st.experimental_user.email == st.secrets.get("ADMIN_EMAIL").strip():
        with st.form("feebback_online"):
            user = st.session_state.email
            rating = st.feedback(options="stars")
            feedback = st.text_input("Provide detailed feedback")
            
            with st.spinner("Submitting feedback ..."):
                btn_online = st.form_submit_button("Submit Feedback")
                if btn_online:
                    if not feedback:
                        feedback = "No detailed feedback supplied"
                    
                    try:
                        if rating:
                            handle_feedback(rating=rating+1, feed_back=feedback, user=user)
                            st.success("Feedback submitted successfully. Thank you.")
                        else:
                            st.error("Supplying the star rating is compulsory")
                    except:
                        st.error("Error encountered while trying to submit feedback, try again")
    else:
        st.divider()
        st.write("Admin section for all feedbacks")
        
        with st.spinner("Loading feedbacks"):
            all_feedbacks = feedback_collection.find()
            df = pd.DataFrame(list(all_feedbacks))
            if not df.empty:
                df = df.drop(columns=["_id"])
            
                st.dataframe(df, use_container_width=True)
            else:
                st.warning("Nothing to see here, yet")