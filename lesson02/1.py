import PyPDF2
# text to speech
import pyttsx3

# Open the PDF file (Enter Path To Your PDF)
file = open('chinese.pdf', 'rb')
# file = open('story.pdf', 'rb')
readpdf = PyPDF2.PdfReader(file)

# Initialize text-to-speech engine
speaker = pyttsx3.init()
rate = speaker.getProperty('rate')   # Get current speaking rate
speaker.setProperty('rate', 200)

volume = speaker.getProperty('volume')
speaker.setProperty('volume', 1)  # Set volume level (0.0 to 1.0)

# Get and set a different voice
voices = speaker.getProperty('voices')
for voice in voices: 
    print("Voice:") 
    print(" - ID: %s" % voice.id) 
    print(" - Name: %s" % voice.name) 
    print(" - Languages: %s" % voice.languages) 
    print(" - Gender: %s" % voice.gender) 
    print(" - Age: %s" % voice.age)

# import sys
# sys.exit()

# voices = speaker.getProperty('voices')
# for voice in voices:
    # if "english" in voice.name.lower() and "us" in voice.name.lower():
        # speaker.setProperty('voice', voice.id)
        # break

# Chinese
en_voice_id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-TW_HANHAN_11.0"
# english
# en_voice_id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
speaker.setProperty('voice', en_voice_id)
        
        
# Iterate over each page in the PDF
for pagenumber in range(len(readpdf.pages)):
    #if pagenumber < 5: continue
    # Extract text from the page
    page = readpdf.pages[pagenumber]
    text = page.extract_text()
    
    # Use the speaker to read the text
    speaker.say(text)
    speaker.runAndWait()

# Save the last extracted text to an audio file (if needed)
speaker.save_to_file(text, 'story.mp3')
speaker.runAndWait()

# Stop the speaker
speaker.stop()

# Close the PDF file
file.close()