import google.generativeai as genai

class GENAIException(Exception):
    "exception"

class ChatBot:

    CHATBOT_NAME='My Generative AI'

    def __init__(self,api_key):
        self.genai=genai
        self.genai.configure(api_key=api_key)
        self.model=self.genai.GenerativeModel('gemini-pro')
        self.conversation=None
        self._conversation_history=[]
        self.preload_conversation() 
    
    
    def send_prompt(self,prompt,temperature=0.3):
        if temperature<0 or temperature>1:
            raise GENAIException("temperature must be between 0 and 1")
        if not prompt:
            raise GENAIException("prompt cannot be empty")
        
        try:
            response=self.conversation.send_message(
                content=prompt,
                generation_config=self._generation_config(temperature)
                
                )
            
            response.resolve 
            return f'{response.text}\n' + '---'*20
        except Exception as e:
            raise GENAIException(e.args[0])

    @property
    def history(self):
        conversation_history=[{'role':message.role,'text':message.parts[0].text} for message in self.conversation.history]
        return conversation_history

    def clear_conversation(self):
        self.conversation=self.model.start_chat(history=[])

    def start_conversation(self):
        self.conversation=self.model.start_chat(history=self._conversation_history)

    def _generation_config(self,temperature):
        return genai.types.GenerationConfig(temperature=temperature)
    
    def _construct_message(self,text,role='user'):
        return { 
            'role': role,
            'parts': [text]
            }


    def preload_conversation(self,conversation_history=None):
        if isinstance(conversation_history,list):
            self._conversation_history=conversation_history
        else:
            self._conversation_history=[
                self._construct_message('from now on return the output as a JASON object that can be loaded in python with the key as \'text\'. For example, {"text":"<output goes here">}'),
                self._construct_message('{"text":"Sure , I can return thr output as a regular JSON object with the key as "text".Here is an example:{"text":"your output"}.','model')
            ]