from openai import OpenAI
import anthropic
import os
from transformers import pipeline
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from dotenv import load_dotenv

load_dotenv()

###Score format
###reiterate why ai can be used as judges just like an expert
###explain why switching to ai as judges of the evaluation
###reshape so it encompases a wide range of evaluation
###ai studio & record results into excel


APImessage = """Prompt -You must use the following persona to judge whether
the analysis and classification of student
feedback using a new solution was useful. You must remain objective and bias 
during this process. The evaluation must factor in helpfulness, relevance,
accuracy, depth, creativity, and level of detail within the results. Your 
evaluation must
start with a short overall explanation and then followed by a rating from
 1 to 10 in this format only "Factor: [10]". Explain the reasoning behind 
 the scores in a separate 
paragraph after 
the ratings.
<\Prompt>

<persona>You are a faculty member of the computer science department at a 
university.
Your day consists of giving computer science lectures, doing research and 
being a supervisor
for undergraduate team projects. You have been tasked to carry out surveys 
to understand
how students feel about their course and modules they take, however you do
 not have enough
time to collect and analyse the feedback given from the surveys. Therefore, 
you must 
rely on tools to help with this task to ensure the task is done correctly 
and the 
results can be used. <\persona>

<Feedback> I really enjoyed this module, I enjoyed working with others 
and creating our own project. Some people didnt help but the team endured 
and were happy with the result 
<\Feedback>

<Emotion Detected>approval, confusion, caring<\Emotion Detected>

<Results> 
• Positive language: "enjoyed," "happy with the result"
• Emphasis on teamwork: "working with others," "team endured"
• Successful outcome: "creating our own project," "happy with the result"
<\Results>
"""

def judge1():
  key=os.getenv("fyp_api_key_judge")
  
  client = OpenAI(
    api_key=key
  )

  completion = client.chat.completions.create(
      model="gpt-4o",
      store=True,
      messages=[
          {"role": "user", "content": APImessage}
      ]
  )

  return(completion.choices[0].message)

def judge2():
  key=os.getenv("fyp_api_key_judge2")
  client = anthropic.Anthropic(api_key=key)
  message = """who are you?"""

  message = client.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=1000,
        temperature=0.1,
        messages = [
            {
                "role" : "user",
                "content" : [
                    {
                        "type" : "text",
                        "text": APImessage
                    }
                ]
            }
        ]
    )
  return message.content[0].text

message = judge1()
print(message)
