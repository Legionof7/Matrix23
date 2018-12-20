// Select a depth-capable capture device.
guard let videoDevice = AVCaptureDevice.default(.builtInTrueDepthCamera,
    for: .video, position: .unspecified)
    else { fatalError("No dual camera.") }
guard let videoDeviceInput = try? AVCaptureDeviceInput(device: videoDevice),
    self.captureSession.canAddInput(videoDeviceInput)
    else { fatalError("Can't add video input.") }
self.captureSession.beginConfiguration()
self.captureSession.addInput(videoDeviceInput)


// Set up photo output for depth data capture.
let photoOutput = AVCapturePhotoOutput()
photoOutput.isDepthDataDeliveryEnabled = photoOutput.isDepthDataDeliverySupported
guard self.captureSession.canAddOutput(photoOutput)
    else { fatalError("Can't add photo output.") }

// Select a depth (not disparity) format that works with the active color format.
let availableFormats = self.videoCaptureDevice.activeFormat.supportedDepthDataFormats
let depthFormat = availableFormats.first(where: { format in
    let pixelFormatType = CMFormatDescriptionGetMediaSubType(format.formatDescription)
    return (pixelFormatType == kCVPixelFormatType_DepthFloat16 ||
        pixelFormatType == kCVPixelFormatType_DepthFloat32)
})

// Set the capture device to use that depth format.
self.captureSession.beginConfiguration()
self.videoCaptureDevice.activeDepthDataFormat = depthFormat
self.captureSession.commitConfiguration()


let photoSettings = AVCapturePhotoSettings(format: [AVVideoCodecKey: AVVideoCodecType.hevc])
photoSettings.isDepthDataDeliveryEnabled = 
    self.photoOutput.isDepthDataDeliverySupported

// Shoot the photo, using a custom class to handle capture delegate callbacks.
let captureProcessor = PhotoCaptureProcessor()
self.photoOutput.capturePhoto(with: photoSettings, delegate: captureProcessor)

