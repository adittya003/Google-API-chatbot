import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred=credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

# new_question = {
#     "Question": "your_new_question_here",
#     "Answer": "your_new_answer_here"
# }

# Update the document in Firestore

def question_number(usr):
    doc_ref = db.collection(u'ChatBot').document(usr)

    if not doc_ref.get().exists:
        doc_ref.set({})
        print(0)
        return str(0)
    else:
        # Retrieve the user's document data
        user_data = doc_ref.get().to_dict()
        print(user_data)
        # Calculate the length of the dictionary
        x = len(user_data) if user_data else 0
        print(x)
        return str(x)

# Example usage
question_number("User2")

def firestore_user_inputting(usr,question_no,new_question):

    doc_ref = db.collection(u'ChatBot').document(usr)
    
    if not doc_ref.get().exists:
        doc_ref.set({})

    doc_ref.update({
        question_no: new_question
    })

def firestore_clear_questions(usr):
    # Specify the document reference for the user
    doc_ref = db.collection('ChatBot').document(usr)

    # Delete the document to clear all questions
    doc_ref.delete()