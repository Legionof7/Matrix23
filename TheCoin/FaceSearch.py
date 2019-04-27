    #needs Dlib

    import face_recognition
    import os
    import sys
    path = r'/home/justin_zheng/worldfaceimages' #Put face images here
    Matches = 0 #Number of pictures that unknown face matches with.
    load_unknown = face_recognition.load_image_file("unknown.jpg")
    unknown_image_encoding = face_recognition.face_encodings(load_unknown)[0]

    for filename in os.listdir(path):
        with open(os.path.join(path, filename)) as f:
            if filename.endswith(".jpg"):
                load_image = face_recognition.load_image_file(filename)
                try: 
                    image_encoding = face_recognition.face_encodings(load_image)[0]
                    face_distance = face_recognition.face_distance([unknown_image_encoding], image_encoding)
                    if face_distance < 0.5:
                        print("Go scrap yourself bot")
                        Matches += 1
                    else: 
                        print("woohoo")
                        
                except:
                    continue
            
            else:
                continue
    if Matches > 1:
        print("Bot detected. Initiate termination.")
    else:
        print("Here's your Worldcoin fellow Human.")
        #Call Ethereum contract

