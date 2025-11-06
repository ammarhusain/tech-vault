import SwiftUI

struct ContentView: View {
    @StateObject private var ocrViewModel = OCRViewModel()
    @State private var selectedImage: UIImage?
    @State private var showImagePicker = false
    @State private var showActionSheet = false
    @State private var imageSourceType: UIImagePickerController.SourceType = .photoLibrary
    
    var body: some View {
        NavigationView {
            VStack(spacing: 20) {
                if let image = selectedImage {
                    Image(uiImage: image)
                        .resizable()
                        .aspectRatio(contentMode: .fit)
                        .frame(maxHeight: 300)
                        .cornerRadius(10)
                        .shadow(radius: 5)
                } else {
                    RoundedRectangle(cornerRadius: 10)
                        .fill(Color.gray.opacity(0.3))
                        .frame(height: 200)
                        .overlay(
                            VStack {
                                Image(systemName: "photo")
                                    .font(.system(size: 50))
                                    .foregroundColor(.gray)
                                Text("No image selected")
                                    .foregroundColor(.gray)
                            }
                        )
                }
                
                Button(action: {
                    showActionSheet = true
                }) {
                    HStack {
                        Image(systemName: "camera.fill")
                        Text("Select Image")
                    }
                    .frame(maxWidth: .infinity)
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(10)
                }
                
                if ocrViewModel.isProcessing {
                    ProgressView("Processing...")
                        .padding()
                } else if !ocrViewModel.recognizedText.isEmpty {
                    ScrollView {
                        Text(ocrViewModel.recognizedText)
                            .padding()
                            .frame(maxWidth: .infinity, alignment: .leading)
                            .background(Color.gray.opacity(0.1))
                            .cornerRadius(10)
                    }
                    .frame(maxHeight: 300)
                    
                    Button(action: {
                        UIPasteboard.general.string = ocrViewModel.recognizedText
                    }) {
                        HStack {
                            Image(systemName: "doc.on.clipboard")
                            Text("Copy Text")
                        }
                        .frame(maxWidth: .infinity)
                        .padding()
                        .background(Color.green)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                    }
                }
                
                Spacer()
            }
            .padding()
            .navigationTitle("Lens Text Snap")
            .actionSheet(isPresented: $showActionSheet) {
                ActionSheet(
                    title: Text("Select Image"),
                    buttons: [
                        .default(Text("Camera")) {
                            imageSourceType = .camera
                            showImagePicker = true
                        },
                        .default(Text("Photo Library")) {
                            imageSourceType = .photoLibrary
                            showImagePicker = true
                        },
                        .cancel()
                    ]
                )
            }
            .sheet(isPresented: $showImagePicker) {
                ImagePicker(selectedImage: $selectedImage, isPresented: $showImagePicker, sourceType: imageSourceType)
            }
            .onChange(of: selectedImage) { image in
                if let image = image {
                    ocrViewModel.recognizeText(from: image)
                }
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}