import streamlit as st
import time

st.title("✨ Your Season ✨")
tab1, tab2 = st.tabs(["Quiz", "More about your result"])
with tab1:
    st.text("Have you ever wondered which season best represents you? \nAnswer 5 fun questions to find out!")
    st.image("https://media.tenor.com/Obm7FIMrbVcAAAAi/tonton-chick.gif",
             use_container_width=True) #NEW
    st.write("---")
    st.text("\n\n\n")

    #Set up point=0
    pts = 0

    #Q1
    question1 = "What is your fav drink?"
    options1 = ["🥤Milkshake", "🍵 Matcha", "🫖 Tea", "☕️ Coffee"]

    st.subheader(question1)
    radio1 = st.radio('Choose one:', options1) #NEW
    st.write("---")
    pts += options1.index(radio1)

    #Q2
    question2 = "Choose your room temperature:"

    st.subheader(question2)
    num_input2 = st.number_input('*in degree Fahrenheit (°F)', min_value=59, max_value=77, value=67) #NEW
    st.write("---")
    if num_input2 <= 63:
        pts += 3
    elif num_input2 > 63 and num_input2 <= 68:
        pts += 2
    elif num_input2 > 68 and num_input2 <= 72:
        pts += 0
    else:
        pts += 1


    #Q3
    question3 = "Which is your fav clothing item?"
    options3 = [("Coat", "images/coat.jpg", "Luca Nardone on Pexels"),
                ("T-shirt", "images/tshirt.jpg", "Dmitriy Ganin on Pexels"),
                ("Hoodie", "images/hoodie.jpg", "Cottonbro Studio on Pexels"),
                ("Cardigan", "images/cardigan.png", "Tima Miroshnichenko on Pexels")]

    st.subheader(question3)
    col1, col2 = st.columns(2) #NEW

    if "answer3" not in st.session_state:
        st.session_state["answer3"] = None

    with col1:
        for i1 in range(0, len(options3), 2):
            op3 = options3[i1][0]
            img3 = options3[i1][1]
            cap3 = options3[i1][2]
            st.image(img3, width=200, caption=cap3)

            if st.button(op3): #NEW
                st.session_state["answer3"] = op3

    with col2:
        for i2 in range(1, len(options3), 2):
            op3 = options3[i2][0]
            img3 = options3[i2][1]
            cap3 = options3[i2][2]
            st.image(img3, width=200, caption=cap3)

            if st.button(op3):
                st.session_state["answer3"] = op3
                
    if st.session_state["answer3"] == "Coat":
        st.write(f"You picked: {options3[0][0]}")
        pts += 2
    elif st.session_state["answer3"] == "T-shirt":
        st.write(f"You picked: {options3[1][0]}")
        pts += 1
    elif st.session_state["answer3"] == "Hoodie":
        st.write(f"You picked: {options3[2][0]}")
        pts += 3
    elif st.session_state["answer3"] == "Cardigan":
        st.write(f"You picked: {options3[3][0]}")
        pts += 0
    st.write("---")

    #Q4
    question4 = "When are you at your best?"

    st.subheader(question4)
    slider4 = st.slider('Choose an hour in military time:', max_value=23, min_value=0, value=12) #NEW
    st.write("---")
    if slider4 <= 6 or slider4 > 21:
        pts += 3
    elif slider4 > 6 and slider4 <= 11:
        pts += 0
    elif slider4 > 11 and slider4 <= 16:
        pts += 1
    else:
        pts += 2

    #Q5
    question5 = "What are your hobbies?"
    options5 = ["Art", "Cooking","Hiking", "Planting", "Reading", "Swimming"]

    st.subheader(question5)
    order5 = st.multiselect("Starting from most loved:", options5) #NEW
    st.write("---")

    if order5 == []:
        pass
    elif order5[0] == "Cooking":
        pts += 0
    elif order5[0] == "Swimming" or order5[0] == "Planting":
        pts += 1
    elif order5[0] == "Hiking" or order5[0] == "Art":
        pts += 2
    elif order5[0] == "Reading":
        pts += 3



    #waiting:
    def waiting():
        #Placeholder
        placeholder = st.empty()
        with placeholder:
            st.image("https://media1.tenor.com/m/LMz_TrIOxV8AAAAd/mr-bean-mrbean.gif",
                     use_container_width=True)

        progress_text = "Thinking in progress. Please wait."
        bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.02)
            bar.progress(percent_complete + 1, text=progress_text) #NEW

        time.sleep(1)

        #Remove image + progress bar
        placeholder.empty()
        bar.empty()
        st.success("Here's your result...") #NEW
        st.balloons() #NEW
        
        #Calculate and return result:
        avg = pts / 5
        if avg <= 0.5:
            st.markdown(
                """
                <div style="padding: 10px; border-radius: 5px; background-color: #fff3cd; border: 1px solid #ffeeba;">
                    <p style="color=black;"><strong>🌸 Spring!</strong></p><br>
                    <img src="https://media.tenor.com/4ZVSxNBJoF8AAAAm/peach-goma-flowers.webp" alt="spring-flower-gif" width="150">
                </div>
                """,
                unsafe_allow_html=True
            )
        elif avg > 0.5 and avg <= 1.5:
            st.markdown(
                """
                <div style="padding: 10px; border-radius: 5px; background-color: #fff3cd; border: 1px solid #ffeeba;">
                    <p style="color=black;"><strong>💐 Summer!</strong></p><br>
                    <img src="https://media.tenor.com/kZzow5agOnkAAAAi/flowers.gif" alt="giving-you-flowers" width="150">
                </div>
                """,
                unsafe_allow_html=True
            )
        elif avg > 1.5 and avg <= 2.5:
            st.markdown(
                """
                <div style="padding: 10px; border-radius: 5px; background-color: #fff3cd; border: 1px solid #ffeeba;">
                    <p style="color=black;"><strong>🍁 Fall!</strong></p><br>
                    <img src="https://media.tenor.com/cfTFUax4X5kAAAAi/malloon-cute.gif" alt="cat-on-a-pumpkin" width="150">
                </div>
                """,
                unsafe_allow_html=True
            )
        elif avg > 2.5:
            st.markdown(
                """
                <div style="padding: 10px; border-radius: 5px; background-color: #fff3cd; border: 1px solid #ffeeba;">
                    <p style="color=black;"><strong>❄️ Winter!</strong></p><br>
                    <img src="https://media.tenor.com/Du9VVJYDPDkAAAAi/tkthao219-bubududu.gif" alt="cold-in-winter" width="150">
                </div>
                """,
                unsafe_allow_html=True
            )

    #Submit button
    submit = st.button("Submit", width="stretch", type="primary")
    if submit:
        waiting()

with tab2:
    st.text("Now you have got your result. Let's figure out what it means for you! \nRemember that this quiz is for fun ^-^")

    #Spring
    st.subheader("Is Spring Your Season?")
    spring = st.expander("Yes")
    spring.image("https://media1.tenor.com/m/jA5XOxnT5HgAAAAC/spring-is-here.gif")
    spring.write("Spring represents warmth, care, and kindness.")
    
    #Summer
    st.subheader("Is Summer Your Season?")
    summer = st.expander("Yeahh")
    summer.image("https://media1.tenor.com/m/gWKIuZk3x-gAAAAC/adventure-run.gif")
    summer.write("Summer represents liveliness, passion, and exploration.")
    
    #Fall
    st.subheader("Is Fall Your Season?")
    fall = st.expander("Yep")
    fall.image("https://media1.tenor.com/m/vHdocgXXpEQAAAAC/falling-leaves-changing-leaves.gif")
    fall.write("Fall represents elegance, calmness, and rest.")
    
    #Winter
    st.subheader("Is Winter Your Season?")
    winter = st.expander("Yea")
    winter.image("https://media1.tenor.com/m/GtlGPpATOZkAAAAC/cold-good-morning-winter.gif")
    winter.write("Winter represents solitude, wisdom, and resilience.")

