from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from ecommbot.ingest import ingestdata

# Here we implemenetd retriver data from vstore then passing to llm with prompt
def generation(vstore):
    retriever = vstore.as_retriever(search_kwargs={"k":3})

    PRODUCT_TEMPLATE = '''
    Your ecommercebot bot is an expert in product recommendations and customer queries.
    It analyzes product titles and reviews to provide accurate and helpful responses.
    Ensure your answers are relevant to the product context and refrain from straying off-topic.
    Your responses should be concise and informative.

    CONTEXT:
    {context}

    QUESTION: {question}

    YOUR ANSWER:
    '''
  
    # Initializing prompt
    prompt = ChatPromptTemplate.from_template(PRODUCT_TEMPLATE)

    # Initializing LLM
    llm = ChatOpenAI()

    # Created chain
    chain = (
        {"context": retriever, "question":RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return chain

if __name__ =='__main__':
    vstore = ingestdata("done")
    chain = generation(vstore)
    print(chain.invoke("can you tell me th best bluetooth headset?"))
 
