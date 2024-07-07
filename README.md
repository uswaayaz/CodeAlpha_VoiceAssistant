This is the simple Voice assitant program that acts like a translator. It listens for your voice, converts it to text, and figures out what you want. Then, it uses different tools depending on your request, like searching the web, playing music, or tell the current time.  
 
Technologies Used
This code utilizes several Python libraries to create a basic virtual assistant:

Speech Recognition (speech_recognition): This library converts spoken audio captured by your microphone into text. It allows the program to understand your voice commands.
Text-to-Speech (pyttsx3): This library does the opposite of speech recognition. It turns text into spoken audio, enabling the program to respond to you with a synthesized voice.
Date and Time (datetime): This library is used to access the current date and time. It allows the program to tell you the time when you ask for it.
Subprocess: This library allows the program to execute other programs on your computer. Here, it's used to launch your web browser (Chrome) when you say "chrome."
pywhatkit (unofficial): This library is used to interact with YouTube. In this case, it attempts to play videos based on your request. However, it's important to note that pywhatkit is an unofficial library and its functionality might be limited or unreliable.

Key Features
This code demonstrates a few key features of a virtual assistant:

Voice Recognition: It listens to your voice commands and converts them to text for processing.
Speech Synthesis: It responds to your commands using a synthesized voice, providing audible feedback.
Basic Command Understanding: It can understand and respond to a limited set of commands, including opening Chrome, telling the time, and attempting to play videos on YouTube.
User Interaction Loop: It continuously listens for your commands, creating an interactive experience.
