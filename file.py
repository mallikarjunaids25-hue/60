with open("input.txt", "r") as file:
    text = file.read()

bad_words = ["spam", "forbidden", "badword"]
cleaned_words = [word for word in text.split() if word.lower() not in bad_words]
cleaned_text = " ".join(cleaned_words)

with open("output.txt", "w") as file:
    file.write(cleaned_text)

print("File successfully filtered and saved!")
