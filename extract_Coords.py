import os
import openai
import ast
import re


openai.api_key = os.getenv("OPENAI_API_KEY")
restart_sequence = "\n"


def main(input: str):
    prompt= "Extract the coordinate from the following text:\n\nText: Flip 2,2 and 5,7\nCoordinates: [[2,2],[5,7]]\n\nText: [10,4]\nCoordinates: [10,4]\n\nText: Row 4 Column 5\nCoordinates: [5,4]\n\nText:"

    prompt+= input+ "\nCordinates: " 

    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    temperature=0,
    max_tokens=20,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    
    output_string=re.sub(' ', '', response.choices[0].text)
    return ast.literal_eval(output_string)
    
    
if __name__ == "__main__":
    main()    


