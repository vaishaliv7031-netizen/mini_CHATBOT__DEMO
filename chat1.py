from flask import Flask, render_template, request
#rendor _template method is act like brigde b/w frontend and backed coding 
#render_template is used to genrate dynamic HTML webpages by rendering HTML templates with data from the backend. It allows you to create HTML files with placeholders for dynamic content, which can be filled in with data when the template is rendered. This is commonly used in web applications to create dynamic and interactive web pages.


chatbot1=Flask(__name__)  # Tells Flask where is chatbot1 located

@chatbot1.route('/',methods=['GET','POST'])# route means the URL  and '/ means homepage

#GET means get data from the server  and POSt mean send  data to the server 


def home():
    ''''now for getting the data from user and sending response  we create response variable 
    under this we create types of responces that when user ask something there is easy 
    to predic what user want to know and what response is best for that question and then we return the response to user'''
    

     # now why we create empty variable ? ..because user may have  different queries?
    # now we create some if else statement for different queries
    # this is for getting the data from user and store in user variable
    response= "" 
    if request.method=="POST":
        user=request.form['message'] # this is for checking if the method is post or not
        # basic chatbot logic
        if 'hello' in user.lower():            
         response = 'Hello! How can I assist you today?'
        elif 'how are you' in user.lower():
         response = 'I am a chatbot, so I do not have feelings, but I am here to help you!'
        elif 'what is your name' in user.lower():
         response = 'I am Chatbot1, your virtual assistant.'     
        else:
         response="i am still learning mean my responses are under development process "

    return render_template("index.html", response=response)
    ''' this is for sending response to user 
    and render_template is for rendering the html file and response=response is for sending the response variable to html file'''
      
chatbot1.run(debug=True) # this is for running the chatbot and debug=True is for showing error if there is any error in code


      
