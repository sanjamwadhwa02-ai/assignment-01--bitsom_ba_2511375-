essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

clean_essay = essay.strip()
print("1. Clean Essay:")
print(clean_essay)

print("\n2. Title Case:")
print(clean_essay.title())

count = clean_essay.count("python")
print("\n3. Count of 'python':", count)

replaced = clean_essay.replace("python", "Python 🐍")
print("\n4. After Replacement:")
print(replaced)

sentences = clean_essay.split(". ")
print("\n5. Sentence List:")
print(sentences)

print("\n6. Numbered Sentences:")
for i in range(len(sentences)):
    sentence = sentences[i]
    
    if not sentence.endswith("."):
        sentence = sentence + "."
    
    print(f"{i+1}. {sentence}")