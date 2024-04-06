# main.py
from openai import OpenAI
from pydantic import BaseModel, Field, validator
from typing import Optional, Dict
import instructor

class Character(BaseModel):
    Intent: str = Field(..., description="classify the intent as one of these 3 values: Greetings, Check balance or transfer money")
    Creds: Optional[Dict[str, str]] = Field(None, description="Determine if there's the Username of the user in the query")

    @validator('Creds', always=True)
    def set_creds(cls, v, values):
        if v is not None and 'username' in v:
            values['Creds'] = v['username']
        return v

def get_response(usernames, user_message):
    client = instructor.patch(
        OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="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",
        ),
        mode=instructor.Mode.JSON,
    )

    resp = client.chat.completions.create(
            model="llama2:7b-chat",
        messages=[{
                    "role": "system",
                    "content": "You are a banking assistant determining what is the intent of the user. Also, if there's username present in the user query, you'll find that out and fill it in the creds."
                },
            {
                "role": "user",
                "content": user_message,
            }
        ],
        response_model=Character,
    )
    return resp.model_dump_json(indent=2)
