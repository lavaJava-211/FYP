import os 
import sys
import time

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add current directory to path
import database, multiEmoteFt, reasoning, stats

def d_m1():
    start = time.time()
    feedback = "I really enjoyed this module, I enjoyed working with others and creating our own project. Some people didnt help but the team endured and were happy with the result "
    module = "CS2002"
    emotion1 = "approval"
    emotion2 = "confusion"
    emotion3 = "caring"
    reasons = """• Positive language: "enjoyed," "happy with the result"• Emphasis on teamwork: "working with others," "team endured"• Successful outcome: "creating our own project," "happy with the result"""
    database.enter_data(feedback, module, emotion1, emotion2, emotion3, reasons)
    end = time.time()
    return (end-start)

def d_m2():
    start = time.time()
    prompt = "What module had the most responses?"
    response = "Based on the provided data, CS2002 and CS2001 both had 2 responses each, while CS2003 had 1 response. Therefore, CS2002 and CS2001 tied for the most responses."
    database.enter_query(prompt, response)
    end = time.time()
    return (end-start)

def d_g1():
    start = time.time()
    reasons = database.get_reasons()
    end = time.time()
    return (end-start)

def d_g2():
    start = time.time()
    reasons = database.get_queries()
    end = time.time()
    return (end-start)

def d_g3():
    start = time.time()
    reasons = database.get_count()
    end = time.time()
    return (end-start)

def d_g4():
    start = time.time()
    reasons = database.get_all()
    end = time.time()
    return (end-start)

def d_g5():
    start = time.time()
    reasons = database.get_dates()
    end = time.time()
    return (end-start)

def d_g6():
    start = time.time()
    reasons = database.get_modules()
    end = time.time()
    return (end-start)

def me_m1():
    start = time.time()
    reasoning = multiEmoteFt.EmotionDetector2()
    text = "The Networks and Operating Systems module was a valuable learning experience, equipping students with a solid foundation in key computing concepts. The combination of theoretical instruction and practical exercises ensured a well-rounded understanding, preparing students for further studies and professional applications in the field of computer science. With minor improvements, the module could be even more effective in aligning with industry trends and advancements."
    top_n =3 
    emotion1, emotion2, emotion3 = reasoning.detect_emotion(text, top_n)
    end = time.time()
    return(end-start)

def r1_m1():
    start = time.time()
    textType = "reason"
    emotion = "admiration"
    feedback = "The Networks and Operating Systems module was a valuable learning experience, equipping students with a solid foundation in key computing concepts. The combination of theoretical instruction and practical exercises ensured a well-rounded understanding, preparing students for further studies and professional applications in the field of computer science. With minor improvements, the module could be even more effective in aligning with industry trends and advancements."
    response = reasoning.claudeAPI(textType, emotion, feedback)
    end = time.time()
    return(end - start)

def r1_m2():
    start = time.time()
    textType = "summary"
    emotion = ""
    feedback = ""
    response = reasoning.claudeAPI(textType, emotion, feedback)
    end = time.time()
    return(end - start)

def r1_m3():
    start = time.time()
    textType = "query"
    emotion = ""
    feedback = "What are some long term and short term improvements that can be made to improve each module?"
    response = reasoning.claudeAPI(textType, emotion, feedback)
    end = time.time()
    return(end - start)

def s1_m1():
    start = time.time()
    list1, list2 = stats.graphPC()
    end = time.time()
    return(end - start)

def s1_m2():
    start = time.time()
    list1, list2 = stats.graphLine()
    end = time.time()
    return(end - start)

def s1_m3():
    start = time.time()
    list1, list2 = stats.emotionCount()
    end = time.time()
    return(end - start)

x =[]
for i in range(3):
    r1 = s1_m3()
    x.append(r1)

print(f"\n",x)