from langchain_google_genai import ChatGoogleGenerativeAI

llm=ChatGoogleGenerativeAI(model="gemini-pro",google_api_key="",)
# response=llm.invoke("write a 5 lin poem on Ai")

# print(response.content)

batch_repsponse=llm.batch(
    [
         "Who is the President of USA?",
        "What are the three capitals of South Africa?",
    ]
)
for response in batch_repsponse:
    print(response.content)