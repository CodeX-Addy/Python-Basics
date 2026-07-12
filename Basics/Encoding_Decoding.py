label_text = "This © is a test string with special characters: ©, ®, ™, and emojis 😊🚀"
encoded_text = label_text.encode("utf-8")

print(f"Label text: {label_text}")
print(f"Encoded text: {encoded_text}")

decode_text = encoded_text.decode("utf-8")
print(f"Decoded text: {decode_text}")
