import random
import pyttsx3
import pymysql

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[0].id)
Assistant.setProperty('rate', 170)

def generate_patient_id():
    return random.randint(100, 999)

def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f"==> MWISE :{audio}")
    print("   ")
    Assistant.runAndWait()


responses = {
    "greeting": ["Hello! How are you feeling today?", "Hi there! What's on your mind?",
                 "Hey! How can I support you today?", "Greetings! How can I assist you?"],
    "goodbye": ["Goodbye! Remember, I'm here whenever you need me.", "See you later! Take care of yourself.",
                "Bye! Take some time for self-care.", "Take care! Remember, you're not alone."],
    "thanks": ["You're welcome! Remember, reaching out is a sign of strength.", "No problem! I'm here to support you.",
               "Anytime! Don't hesitate to reach out whenever you need to."],
    "name": ["My name is MWISE , Mental Wellness Interactive Support Engine"],
    "feeling": ["It's okay to feel the way you do. Can you tell me more about what's been going on?",
                "Your feelings are valid. Would you like to talk more about them?",
                "Acknowledging your feelings is an important step. What's been on your mind?"],
    "selfcare": ["Self-care is crucial for your well-being. What are some activities that help you relax?",
                 "Taking care of yourself is important. What self-care practices do you enjoy?",
                 "Self-care looks different for everyone. How do you like to take care of yourself?"],
    "positive affirmation": ["You're doing great! Keep going, one step at a time.",
                             "Remember, you are worthy of love and respect.",
                             "You're stronger than you think. Keep pushing forward."],
    "loneliness": [
        "Feeling lonely can be really tough, but you're not alone in experiencing it. It's important to reach out to others and take care of yourself. Would you like to talk more about what's been making you feel this way?",
        "Loneliness can be overwhelming, but there are ways to connect with others and feel supported. Have you tried reaching out to friends or joining a community? I'm here to listen if you'd like to share more.",
        "It's okay to feel lonely sometimes, and it's important to acknowledge those feelings. Let's explore some ways to cope with loneliness together. How can I support you right now?"],
    "deep breathing": [
        "Let's take a moment to breathe deeply. Inhale for 4 counts, hold for 4 counts, and exhale for 4 counts.",
        "Deep breathing can help calm your mind. Let's try it together. Inhale deeply through your nose, hold, and exhale slowly."],
    "mindfulness": [
        "Mindfulness can help bring you back to the present moment. Let's take a moment to notice our surroundings and how we feel.",
        "Being mindful can help reduce stress and anxiety. Take a moment to focus on your breath and the sensations in your body."],
    "gratitude": ["Practicing gratitude can improve your mood. What's something you're grateful for today?",
                  "Even in difficult times, there's always something to be grateful for. What's brought you joy recently?"],
    "grounding techniques": [
        "Grounding techniques can help when you're feeling overwhelmed. Let's try focusing on your senses. What can you see, hear, smell, taste, and touch right now?",
        "When you feel anxious, grounding techniques can help bring you back to the present moment. Let's try counting objects in the room or naming things you can see."],
    "sad": ["I'm sorry to hear that you're feeling sad. Let's work through it together.",
            "It's okay to feel sad sometimes. I'm here to support you.",
            "I understand. It's important to acknowledge your emotions. What's been bothering you?"],
    "setting boundaries": [
        "Setting boundaries is important for your mental health. Have you thought about what boundaries you need to set?",
        "It's okay to say no and set boundaries that protect your well-being. What boundaries do you need to establish in your life?"],
    "coping strategies": [
        "Coping strategies can help you manage difficult emotions. What are some healthy ways you cope with stress?",
        "Having coping strategies in place can make challenging situations more manageable. What techniques have worked for you in the past?"],
    "goal setting": [
        "Setting small, achievable goals can help improve your mood and motivation. What's one thing you'd like to accomplish today?",
        "Setting goals gives you something to strive for. What's a goal you'd like to work towards?"],
    "support system": [
        "Having a support system is crucial for your mental health. Who can you reach out to for support when you're feeling down?",
        "It's important to have people you can lean on during tough times. Who can you turn to for support?"],
    "positive activity": ["Engaging in positive activities can improve your mood. What's something you enjoy doing?",
                          "Doing things you love can boost your mood. What positive activity can you engage in today?"],
    "sleep hygiene": [
        "Good sleep hygiene is important for your mental health. Have you tried establishing a bedtime routine?",
        "Getting enough sleep is essential for your well-being. What steps can you take to improve your sleep hygiene?"],
    "stress management": [
        "Managing stress is key to maintaining good mental health. What are some techniques you've used to cope with stress in the past?",
        "Stress is a normal part of life, but it's important to find healthy ways to manage it. What helps you relax when you're feeling stressed?"],
    "mindful eating": [
        "Mindful eating can help you develop a healthier relationship with food. Have you tried paying attention to the taste, texture, and smell of your food?",
        "Eating mindfully can help you enjoy your meals more and make healthier choices. How can you incorporate mindful eating into your routine?"],
    "validation": ["Your feelings are valid, and it's okay to express them. I'm here to listen without judgment.",
                   "Feeling understood is important. I hear you, and I'm here to support you."],
    "relaxation_techniques": [
        "Relaxation techniques can help reduce stress and anxiety. Let's try a progressive muscle relaxation exercise. Start by tensing and then relaxing each muscle group in your body, one by one.",
        "Finding ways to relax is important for your well-being. What relaxation techniques do you find helpful?"],
    "emotional_support": [
        "Emotional support is crucial during difficult times. How can I support you emotionally right now?",
        "You're not alone. I'm here to offer emotional support whenever you need it."],
    "meditation": ["Meditation can help calm your mind and reduce stress. Let's try a guided meditation together.",
                   "Practicing meditation regularly can have numerous benefits for your mental health. Would you like to try a meditation exercise?"],
    "journaling": ["Journaling can help you process your thoughts and emotions. Have you tried keeping a journal?",
                   "Writing down your thoughts and feelings can be therapeutic. How do you feel about starting a journaling practice?"],
    "therapy": [
        "Therapy can provide you with the support and tools you need to cope with life's challenges. Have you considered reaching out to a therapist?",
        "Speaking to a therapist can help you gain insight into your thoughts and behaviors. Would you like assistance finding a therapist?"],
    "medication": [
        "Medication can be helpful for managing certain mental health conditions. Have you discussed medication options with a healthcare professional?",
        "If you're struggling with your mental health, medication may be part of your treatment plan. Have you considered speaking to a doctor about your options?"],
    "joke": ["Why did the scarecrow win an award? Because he was outstanding in his field!",
             "How does a penguin build its house? Igloos it together!",
             "Why don't skeletons fight each other? They don't have the guts!",
             "Why did the tomato turn red? Because it saw the salad dressing!",
             "Why don't scientists trust atoms? Because they make up everything!",
             "What do you call fake spaghetti? An impasta!",
             "Why did the bicycle fall over? Because it was two-tired!"],
    "guilt": [
        "Guilt can be a heavy emotion to carry. It's important to understand that we all make mistakes, but it's how we learn and grow from them that matters. Would you like to talk more about what's making you feel guilty?",
        "Feeling guilty is a natural emotion, but it's also essential to practice self-compassion. What do you think you could do to make things right, or how can I help you work through these feelings?",
        "Guilt can weigh on us, but it's also a chance to reflect and take responsibility. It's okay to acknowledge your feelings, but remember, you deserve forgiveness too. How can I support you in moving forward?"],
    "stress reduction": [
        "Reducing stress is important for your overall well-being. What steps can you take to decrease your stress levels?",
        "Stress can take a toll on your mental"],
    "anger management": [
        "Feeling angry is normal, but it's important to express it in healthy ways. How do you usually cope with anger?",
        "Anger is a powerful emotion. Let's explore some strategies to help you manage it more effectively.",
        "When you're feeling angry, taking a step back and counting to ten can help you cool down. Have you tried this technique before?"],
    "addiction support": [
        "Struggling with addiction can be tough, but you're not alone. Have you considered reaching out for support?",
        "Taking the first step towards recovery can be daunting, but it's worth it. How can I support you on your journey?",
        "Recovery is possible, and there are many resources available to help you overcome addiction. Would you like assistance finding support groups or treatment programs?"],
    "addiction recovery": [
        "Recovery is a journey, and it's okay to take it one day at a time. How are you feeling about your progress?",
        "Every small step you take towards recovery is a victory. What's one positive change you've noticed since starting your journey?",
        "Remember, relapse is a part of recovery, not a failure. What strategies can you implement to prevent relapse in the future?"],
    "anger coping strategies": [
        "Finding healthy ways to cope with anger is crucial for your well-being. What activities help you feel calmer?",
        "Anger can be overwhelming, but there are techniques you can use to manage it. Have you tried deep breathing or visualization exercises?",
        "Identifying the triggers that make you angry can help you develop coping strategies. What situations tend to provoke your anger?"],
    "addiction triggers": [
        "Understanding your addiction triggers is an important part of recovery. What situations or emotions make you more likely to use?",
        "Identifying your triggers can help you develop strategies to avoid them or cope with them more effectively. What are some triggers you've noticed in the past?",
        "Certain people, places, or activities can trigger cravings. How can you minimize your exposure to these triggers?"],
    "anger expression": [
        "Expressing your anger in a healthy way can help prevent it from building up. Have you tried journaling or talking to a trusted friend about what's bothering you?",
        "Suppressing your anger can lead to negative consequences. How can you express your feelings in a constructive manner?",
        "Finding healthy outlets for your anger, such as exercise or creative activities, can help you release tension. What activities do you enjoy that help you feel more relaxed?"],
    "addiction recovery resources": [
        "There are many resources available to support you on your journey to recovery, including support groups, therapy, and rehabilitation programs. Have you explored any of these options?",
        "Recovery is a personal journey, but you don't have to go through it alone. Would you like help finding addiction recovery resources in your area?",
        "Taking the first step towards recovery can be intimidating, but there are people who want to help you succeed. How can I assist you in finding the support you need?"],
    "anger communication": [
        "Communicating assertively can help you express your feelings without resorting to anger. Have you tried using 'I' statements to express how you feel?",
        "Effective communication can help resolve conflicts and reduce anger. How can you improve your communication skills in challenging situations?",
        "When discussing difficult topics, it's important to listen actively and validate the other person's feelings. How can you practice active listening in your interactions?"],
    "addiction support_network": [
        "Building a strong support network is crucial for maintaining sobriety. Who can you turn to for support when you're struggling?",
        "Having friends and family who understand what you're going through can make a big difference in your recovery. How can you strengthen your support network?",
        "Support groups provide a sense of community and understanding. Have you considered joining a support group for people in recovery?"],
    "anger relaxation": [
        "Finding relaxation techniques that work for you can help you manage your anger more effectively. Have you tried deep breathing, progressive muscle relaxation, or mindfulness exercises?",
        "When you're feeling angry, taking a break and engaging in a calming activity can help you regain control. What activities help you relax?",
        "Practicing relaxation techniques regularly can help reduce your overall stress levels and prevent anger from building up. How can you incorporate relaxation into your daily routine?"],
    "addiction triggers_management": [
        "Identifying your triggers is the first step towards managing them effectively. What strategies can you use to avoid or cope with your triggers?",
        "Developing a plan for how to handle your triggers can help you stay on track with your recovery. How can you prepare yourself for situations that might trigger cravings?",
        "When you encounter a trigger, it's important to have healthy coping mechanisms in place. What coping strategies do you find helpful in challenging situations?"],
    "anger journaling": [
        "Keeping a journal can help you gain insight into your anger triggers and patterns. Have you tried journaling about your feelings when you're angry?",
        "Writing down your thoughts and feelings can be a cathartic way to process your emotions. "],
    "anger issues": [
        "It's okay to feel angry, but it's important to manage it in healthy ways. How do you typically cope with your anger?",
        "Anger can be overwhelming, but learning to manage it can greatly improve your quality of life. How can I support you in dealing with your anger?",
        "Recognizing and addressing your anger issues is a positive step towards emotional well-being. What are some triggers that make you feel angry?"],
    "social media": [
        "Social media can sometimes make us feel pressured or inadequate. Remember to take breaks and prioritize your mental health. It's okay to log off and take time for yourself.",
        "Social media can have both positive and negative effects on our mental health. It's important to be mindful of how much time you spend online and how it makes you feel.",
        "It's common to feel overwhelmed by social media. Remember, you are more than your online presence. Take time to connect with yourself and those around you offline."],
    "mental health": [
        "Your mental health is important. It's okay to ask for help when you need it. You're not alone in your struggles.",
        "Taking care of your mental health is just as important as your physical health. Remember to prioritize self-care and seek support when you need it.",
        "It's okay to not be okay. Your feelings are valid, and it's important to talk about them. You deserve support and understanding."],
    "bullying": [
        "I'm really sorry to hear that you're experiencing bullying. Remember, it's not your fault. You deserve to feel safe and respected. Is there anything specific you'd like to talk about or any support you need?"],
    "depression": [
        "Dealing with depression can be incredibly tough, but you're not alone. It's important to reach out for support. Would you like to discuss your feelings further or explore coping strategies together?"],
    "anxiety": [
        "Anxiety can be overwhelming, but there are ways to manage it. Would you like to talk about what's been causing your anxiety or explore relaxation techniques that might help?"],
    "exam_pressure": [
        "Feeling stressed about exams is completely normal, but it's important to take care of yourself too. Let's discuss some strategies for managing exam pressure and stress. Remember, your well-being is just as important as your grades."],
    "children_mental_health": [
        "Children's mental health is incredibly important. If you're concerned about a child's well-being, it's essential to provide support and understanding. How can I assist you in supporting a child's mental health?"],
    "coping_strategies_bullying": [
        "When facing bullying, it's crucial to prioritize your well-being. Consider talking to a trusted adult, practicing assertiveness, and focusing on activities that bring you joy and confidence. You deserve to feel safe and supported."],
    "coping_strategies_depression": [
        "Managing depression can involve various strategies such as reaching out to supportive friends or family, engaging in regular physical activity, practicing mindfulness or meditation, and seeking professional help if needed. Remember, it's okay to ask for support."],
    "coping_strategies_anxiety": [
        "To cope with anxiety, it can be helpful to practice deep breathing exercises, progressive muscle relaxation, journaling your thoughts and feelings, challenging negative thoughts, and gradually facing fears through exposure therapy. Don't hesitate to reach out for support."],
    "cyberbullying": [
        "I'm sorry to hear that you're experiencing cyberbullying. It's important to take steps to protect yourself and seek support. Remember, you're not alone in this. "],
    "ptsd": [
        "Post-traumatic stress disorder (PTSD) can deeply affect your mental well-being. It's important to talk to someone you trust or seek professional help. Would you like to explore coping strategies or discuss your feelings?",
        "If you're struggling with PTSD, you're not alone. It's okay to seek support from a therapist or counselor. Would you like information on resources or techniques to manage symptoms?",
        "Living with PTSD can be challenging, but there are ways to heal. Taking small steps, reaching out for support, and practicing grounding techniques can help. How can I assist you today?"
    ],
    "default": ["Hmm, looks like you caught me off guard with that one!",
                "I'm sorry, I'm not sure how to respond to that. Could you rephrase your question or try asking something else?",
                "It seems like I don't have the information you're looking for at the moment. Is there anything else I can help you with?",
                "I'm still learning, and it appears I don't have an answer for that right now. Is there another topic you'd like to discuss?",
                "I'm sorry, I don't have the knowledge to address that question. Would you like assistance with a different topic?",
                "Hmm, it seems I'm not familiar with that. Let's try talking about something else. What's on your mind?",
                "I'm sorry, I didn't understand that.", "Could you please rephrase that?", "I'm not sure I follow."]
}
problems = []
def generate_response(question):
    question = question.lower()

    if "hello" in question or "hi" in question or "how's going" in question or "how r u" in question or "how are you" in question:
        Speak(random.choice(responses["greeting"]))
    elif "thank" in question:
        Speak(random.choice(responses["thanks"]))
    elif "feeling" in question:
        Speak(random.choice(responses["feeling"]))
    elif "selfcare" in question:
        Speak(random.choice(responses["selfcare"]))
    elif "positive affirmation" in question:
        Speak(random.choice(responses["positive affirmation"]))
    elif "deep breathing" in question:
        Speak(random.choice(responses["deep breathing"]))
    elif "mindfulness" in question:
        Speak(random.choice(responses["mindfulness"]))
    elif "gratitude" in question:
        Speak(random.choice(responses["gratitude"]))
    elif "grounding techniques" in question:
        Speak(random.choice(responses["grounding techniques"]))
    elif "setting boundaries" in question:
        Speak(random.choice(responses["setting boundaries"]))
    elif "coping strategies" in question:
        Speak(random.choice(responses["coping strategies"]))
    elif "goal setting" in question:
        Speak(random.choice(responses["goal setting"]))
    elif "support system" in question:
        Speak(random.choice(responses["support system"]))
    elif "positive activity" in question:
        Speak(random.choice(responses["positive activity"]))
    elif "sleep hygiene" in question:
        Speak(random.choice(responses["sleep hygiene"]))
    elif "stress management" in question:
        Speak(random.choice(responses["stress management"]))
    elif "relaxation techniques" in question:
        Speak(random.choice(responses["relaxation techniques"]))
    elif "emotional support" in question:
        Speak(random.choice(responses["emotional support"]))
    elif "meditation" in question:
        Speak(random.choice(responses["meditation"]))
    elif "therapy" in question:
        Speak(random.choice(responses["therapy"]))
    elif "medication" in question:
        Speak(random.choice(responses["medication"]))
    elif "stress reduction" in question:
        Speak(random.choice(responses["stress reduction"]))
    elif "anger management" in question:
        Speak(random.choice(responses["anger management"]))
        problems.append("anger management")
    elif "anger issues" in question:
        Speak(random.choice(responses["anger issues"]))
        problems.append("anger issues")
    elif "addiction support" in question or "addiction" in question or "addicted" in question:
        Speak(random.choice(responses["addiction support"]))
        problems.append("addiction")
    elif "addiction recovery" in question:
        Speak(random.choice(responses["addiction recovery"]))
        problems.append("addiction recovery")
    elif "addiction triggers" in question:
        Speak(random.choice(responses["addiction triggers"]))
        problems.append("addiction triggers")
    elif "anger expression" in question:
        Speak(random.choice(responses["anger expression"]))
        problems.append("anger expression")
    elif "cyberbullying" in question or "cyberbullied" in question:
        Speak(random.choice(responses["cyberbullying"]))
        problems.append("cyberbullying")
    elif "social media" in question:
        Speak(random.choice(responses["social media"]))
        problems.append("social media")
    elif "mental health" in question:
        Speak(random.choice(responses["mental health"]))
        problems.append("mental health")
    elif "depressed" in question:
        Speak(random.choice(responses["depression"]))
        problems.append("depression")
    elif "anxious" in question:
        Speak(random.choice(responses["anxiety"]))
        problems.append("anxiety")
    elif "exam" in question:
        Speak(random.choice(responses["exam_pressure"]))
        problems.append("exam pressure")
    elif "children" in question:
        Speak(random.choice(responses["children_mental_health"]))
        problems.append("children mental health")
    elif "bullying" in question:
        Speak(random.choice(responses["bullying"]))
        problems.append("bullying")
    elif "sad" in question:
        Speak(random.choice(responses["sad"]))
        problems.append("sadness")
    elif "stress" in question:
        Speak(random.choice(responses["stress management"]))
        problems.append("stress")
    elif "ptsd" in question:
        Speak(random.choice(responses["ptsd"]))
        problems.append("ptsd")
    elif "loneliness" in question:
        Speak(random.choice(responses["loneliness"]))
        problems.append("loneliness")
    elif "guilt" in question:
        Speak(random.choice(responses["guilt"]))
        problems.append("guilt")

    elif "motivation" in question:
        Speak(
            "Motivation is crucial for achieving your goals and overcoming challenges. Remember, you have the strength and resilience to face whatever comes your way. Take one step at a time, celebrate your progress, and keep moving forward. Believe in yourself and your abilities, and never underestimate the power of perseverance. You've got this!")
    elif "joke" in question or "make me laugh" in question:
        Speak("Sure")
        Speak(random.choice(responses["joke"]))
    elif "how can you help me" in question:
        Speak(
            "I'm here to provide support and guidance on various aspects of mental health and well-being. Feel free to ask me anything, and I'll do my best to assist you.")
    elif "not yet" in question:
        Speak("Do you need more help??")
    else:
        Speak(random.choice(responses["default"]))



def main():

    Speak("Initialising MWISE...")
    Speak("Enter Your Details Before Starting the Session")
    name = input("ENTER YOUR NAME=>")
    age = input("ENTER YOUR AGE=>")
    phone_no = input("ENTER YOUR PHONE NO.=>")
    email = input("ENTER YOUR EMAIL ID=>")
    Speak(F"Hello {name}, I am MWISE, How can I help you Today")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print(random.choice(responses["goodbye"]))
            Speak("Inserting your Details in my Database")
            try:
                connection = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='TonyMk50',
                    database='mwise'
                )
                print("Connection to the database established successfully!")

                cursor = connection.cursor()

                insert_query = """
                INSERT INTO REPORT (PATIENT_ID, NAME, AGE, PHONE_NO, EMAIL, PROBLEM)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                patient_id = generate_patient_id()
                problem = ", ".join(problems)
                cursor.execute(insert_query, (patient_id, name, age, phone_no, email, problem))
                connection.commit()
                print(f"Record inserted successfully with Patient ID: {patient_id}")
            except pymysql.MySQLError as e:
                print(f"Error while connecting to the database: {e}")
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    print("Database connection closed.")
            break

        elif user_input.lower() == "show":
            try:
                # Step 1: Establish a connection to the database
                connection = pymysql.connect(
                    host='localhost',  # Database host
                    user='root',  # Database username
                    password='TonyMk50',  # Database password
                    database='test'  # Database name
                )
                print("Connection to the database established successfully!")

                # Step 2: Create a cursor object
                cursor = connection.cursor()

                # Step 3: Execute the query to fetch all records from the REPORT table
                cursor.execute("SELECT * FROM REPORT")

                # Step 4: Fetch all rows from the result
                records = cursor.fetchall()

                # Step 5: Display the records
                print("\nCurrent records in the REPORT table:")
                for row in records:
                    print(row)

            except pymysql.MySQLError as e:
                print(f"Error while connecting to the database: {e}")

            finally:
                # Step 6: Close the cursor and connection
                if connection:
                    cursor.close()
                    connection.close()
                    print("Database connection closed.")
            break

        response = generate_response(user_input)

main()
