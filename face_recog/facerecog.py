import os
import face_recognition



with open('database.db') as f:
    data = f.read()


x = data.split("$");

y = data.split("%");

#print(y[len(y)-2])
#print(x[len(x)-2])

latestimage = "tobeverified/" + x[len(x)-2]
image = face_recognition.load_image_file(latestimage)
encoding1 = face_recognition.face_encodings(image)[0]


dir_path = 'static/images'

count = 0
const2 = -3;

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        print(path)
        image2 = face_recognition.load_image_file(f"static/images/{path}")
        
        if len(face_recognition.face_encodings(image2)) != 0:
            encoding2 = face_recognition.face_encodings(image2)[0]

            if (face_recognition.compare_faces([encoding1], encoding2) == [True]):
                print("welcome", y[len(y)-2])
                const2 = 0;
            

                break

        
        


        #print(type(face_recognition.compare_faces([encoding1], encoding2)))
        
        else:
            continue


        

if(const2 != 0):
    print("Not Verified!")


#print(count);





