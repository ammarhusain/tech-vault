import SwiftUI
import Vision
import UIKit

class OCRViewModel: ObservableObject {
    @Published var recognizedText: String = ""
    @Published var isProcessing: Bool = false
    
    func recognizeText(from image: UIImage) {
        guard let cgImage = image.cgImage else { return }
        
        isProcessing = true
        recognizedText = ""
        
        let request = VNRecognizeTextRequest { [weak self] request, error in
            DispatchQueue.main.async {
                self?.isProcessing = false
                
                if let error = error {
                    self?.recognizedText = "Error: \(error.localizedDescription)"
                    return
                }
                
                guard let observations = request.results as? [VNRecognizedTextObservation] else {
                    self?.recognizedText = "No text found"
                    return
                }
                
                var detectedText = ""
                for observation in observations {
                    guard let topCandidate = observation.topCandidates(1).first else { continue }
                    detectedText += topCandidate.string + "\n"
                }
                
                self?.recognizedText = detectedText.isEmpty ? "No text found" : detectedText
            }
        }
        
        request.recognitionLevel = .accurate
        request.usesLanguageCorrection = true
        
        let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
        
        DispatchQueue.global(qos: .userInitiated).async {
            do {
                try handler.perform([request])
            } catch {
                DispatchQueue.main.async {
                    self.isProcessing = false
                    self.recognizedText = "Error processing image: \(error.localizedDescription)"
                }
            }
        }
    }
}