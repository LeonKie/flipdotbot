import os
import openai
import ast
import re


openai.api_key = os.getenv("OPENAI_API_KEY")
restart_sequence = "\n"


def main(input: str):
    
    prompt= "Extract the coordinate from the following text:\n\nText: Flip 2,2 and 5,7\nCoordinates: [[2,2],[5,7]]\n\nText: [10,4]\nCoordinates: [10,4]\n\nText: Row 4 Column 5\nCoordinates: [5,4]\n\nText:"

    number_occ = len(re.findall('\d+', input))
    
    if number_occ >= 2:
    
        prompt+= input+ "\nCordinates: " 

        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=40,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        
        print("Respons: ", response.choices[0].text)
        output_string=re.sub(' ', '', response.choices[0].text)
        
        try:
            coordinates =ast.literal_eval(output_string)
            
            if all(isinstance(x, int) for x in coordinates) and len(coordinates) == 2:
                return coordinates
            elif all(isinstance(x, list) and len(x)==2 for x in coordinates):
                return coordinates
            else:
                print("Error: Invalid Format")
                return []
        except:
            print("Error: Invalid input")
            return []
    
    else:
        print("No Coordinates Found")
        return []
    
    
if __name__ == "__main__":
    inp=input()
    print(main(inp))  


