from face_app.face_app import FaceApp

instance = FaceApp("notebooks\SourceImage.jpg", "notebooks\DestinationImage.jpg", 'static/modefied.jpg')

instance.run()