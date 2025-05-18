# Study Buddy: AI Assistant

[*Link to App*](https://student-study-buddy.streamlit.app/)

[*Demo Video*](www.youtube.com)

**Study smarter, not harder.** Study Buddy is your personal AI assistant designed to help you ace your studies by making your learning materials interactive and accessible. Simply upload your PDF documents, and let Study Buddy help you understand concepts faster, generate practice questions, and get instant answers to your queries based directly on your study materials. Leveraging the power of Google's Gemini models and intelligent tools, Study Buddy transforms your static documents into a dynamic learning experience.

## How Study Buddy Helps You Study Better and Faster

Traditional studying can be time-consuming. Study Buddy cuts through the inefficiency by:

* **Instant Answers from Your Materials:** No more sifting through pages! Upload your PDFs and ask Study Buddy questions directly about the content. Get precise answers derived straight from your documents in seconds.
* **Automated Q&A Generation:** Understand key concepts by having Study Buddy automatically generate question-and-answer pairs from your uploaded study materials. Test your knowledge and reinforce learning effortlessly.
* **Intelligent Contextual Chat:** Discuss your study topics with an AI that understands the context of your uploaded documents and your previous questions, providing a personalized learning conversation.
* **Quick Knowledge Lookups:** Need to clarify a concept not in your document? Study Buddy can use web search to provide additional context and information.
* **Organized Learning:** Keep track of your study sessions with chat history, allowing you to revisit explanations and questions.

## Features

* **Document-Based Q&A:** Get answers and generate questions directly from your uploaded PDF and DOCX study materials.
* **Intelligent Chat:** Engage in contextual conversations related to your studies and uploaded documents.
* **Web Search Integration:** Access external information to supplement your learning.
* **Chat History:** Review past study sessions and conversations.
* **Google Authentication:** Secure and easy login using your Google account.
* **Feedback Mechanism:** Help us improve Study Buddy by providing feedback.

## Code Structure

* `app.py`: The heart of the application, managing the user interface, authentication flow, and the core chat logic.
* `agent.py`: Configures the AI agent, defines prompt templates, and sets up the tools Study Buddy uses.
* `ext_tools/`: Contains specialized tools like `qa_tool.py` for generating Q&A from documents and `instant_rag.py` for document retrieval.
* `utils/`: Houses utility functions for database interactions (`database.py`), user account handling (`account.py`), and feedback processing (`feedback.py`).

## Dependencies

* `langchain`: The framework powering the AI agent's logic.
* `langchain_google_genai`: Connects Study Buddy to Google's powerful Gemini models.
* `pymongo`: Used for storing chat history and feedback data in MongoDB.
* `streamlit`: Provides the interactive web interface.
* `tavily-python`: Enables web search capabilities for broader knowledge.
* `PyPDF2`, `python-docx`: Libraries for processing your PDF and DOCX study materials.
* `Authlib`: Handles the Google OAuth authentication flow.

## Setup

To get Study Buddy up and running, you will need accounts and credentials from a few external services:

1.  **MongoDB Account:** You'll need a MongoDB database to store chat history and feedback. Obtain your connection string.
2.  **Tavily Account:** Get an API key from Tavily Search for web search functionality.
3.  **Google Cloud Account:** You'll need this to obtain OAuth 2.0 User Credentials for Google Authentication. Follow the Google Cloud documentation to create an OAuth 2.0 Client ID and Client Secret for a Web Application. Configure the authorized redirect URI as `http://localhost:8501/oauth2callback`.

Once you have your accounts and credentials:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/GeamXD/Study-Agent
    cd Study-Agent
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Secrets:**
    Study Buddy uses two files for managing secrets: `.env` for general environment variables and `.streamlit/secrets.toml` for Streamlit-specific secrets, including authentication details.

    * Create a `.env` file in the root directory of the project and add:

        ```env
        DATABASE_URL="YOUR_MONGODB_CONNECTION_STRING"
        TAVILY_API_KEY="YOUR_TAVILY_API_KEY"
        GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
        ADMIN_EMAIL="YOUR_ADMIN_EMAIL" # Email of the admin user for potential future features
        ```
        Replace the placeholder values with your actual credentials.

    * Create a `.streamlit/secrets.toml` file in the `.streamlit` directory (create it if it doesn't exist) and add:

        ```toml
        [auth]
        redirect_uri = "http://localhost:8501/oauth2callback"
        cookie_secret = "A_RANDOM_LONG_STRING_FOR_COOKIE_SECURITY" # Generate a strong, random string
        client_id = "YOUR_GOOGLE_CLIENT_ID"
        client_secret = "YOUR_GOOGLE_CLIENT_SECRET"
        server_metadata_url = "[https://accounts.google.com/.well-known/openid-configuration](https://accounts.google.com/.well-known/openid-configuration)"
        ```
        Replace the placeholder values with your actual Google OAuth credentials and a strong random string for `cookie_secret`.

4.  **Run the Application:**
    ```bash
    streamlit run pages.py --server.enableCORS false --server.enableXsrfProtection false
    ```

5.  **Access Study Buddy:**
    Open your web browser and go to `http://localhost:8501`.

6.  **Authenticate:**
    Click on the "Login with Google" button to sign in using the Google account you configured as the admin email (or any allowed user if you modify the authentication logic).

7.  **Start Studying:**
    * Use the document upload feature to add your PDF or DOCX study materials.
    * Type your questions in the chat interface to get answers based on your documents or general knowledge.
    * Explore the Q&A generation feature to create practice questions.

8.  **Provide Feedback:**
    Help improve Study Buddy by using the feedback option.

9.  **Review History:**
    Check the chat history to see your previous interactions.

10. **Logout:**
    Click "Logout" when you're done with your study session.

## Contributing

We welcome contributions to make Study Buddy even better! If you have ideas for new features, improvements, or find bugs, please open an issue or submit a pull request.