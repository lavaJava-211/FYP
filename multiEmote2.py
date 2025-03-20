# Use a pipeline as a high-level helper
from transformers import pipeline

def classify_emotion(text):
    pipe = pipeline("text-classification", model="Sungjin228/roberta-finetuned-sem_eval-english", top_k=3)
    results = pipe(text)

    emotion1 = results[0][0]
    emo1_name = emotion1['label']
    emo1_score = emotion1['score']
    emotion2 = results[0][1]
    emo2_name = emotion2['label']
    emo2_score = emotion2['score']
    emotion3 = results[0][2]
    emo3_name = emotion3['label']
    emo3_score = emotion3['score']

    return (emo1_name, emo1_score), (emo2_name, emo2_score), (emo3_name, emo3_score)

