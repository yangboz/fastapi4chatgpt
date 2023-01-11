from fastapi import FastAPI
import openai
app = FastAPI()
@app.get("/")
async def root():
	return {"message": "Hello Chatgpt"}

@app.get("/chatgpt")
def chatgpt(api_key:str,model_engines: List[str] = Query(None, description="List of names to chatgpt model engines"),_prompt:str,_max_tokens:int=128):
	openai.api_key  = api_key
	# Set the maximum number of tokens to generate in the response
	max_tokens = 128

	# Generate a response
	completion = openai.Completion.create(
	    engine=model_engine,
	    prompt=_prompt,
	    max_tokens=_max_tokens,
	    temperature=0.5,
	    top_p=1,
	    frequency_penalty=0,
	    presence_penalty=0
	)
	res=completion.choices[0].text 
	# Print the response
	print(res)
	return res

