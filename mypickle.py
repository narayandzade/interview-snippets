
import pickle


data = {
    "name": "Narayan",
    "age": 34,
    "localtion": "Pune"
    
}

with open("file.txt", "wb") as file:
    pickle.dump(data, file)

with open("file.txt", "rb") as file:
        newdata = pickle.load(file)

print(newdata)