import librosa
import numpy as np
import os
import argparse
from pathlib import Path

def detect_silence(audio_path, min_silence_duration=5.0, threshold_db=-60):
    # Load audio file
    y, sr = librosa.load(audio_path)
    
    # Convert to dB scale
    S = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    
    # Get mean amplitude for each time frame
    mean_amplitude = np.mean(S, axis=0)
    
    # Find silent regions
    silent_frames = mean_amplitude < threshold_db
    
    # Convert frames to time
    hop_length = 512  # Default hop length in librosa.stft
    frame_duration = hop_length / sr
    
    # Find continuous silent regions
    silence_starts = []
    silence_durations = []
    current_start = None
    
    for i, is_silent in enumerate(silent_frames):
        if is_silent and current_start is None:
            current_start = i
        elif not is_silent and current_start is not None:
            duration = (i - current_start) * frame_duration
            if duration >= min_silence_duration:
                silence_starts.append(current_start * frame_duration)
                silence_durations.append(duration)
            current_start = None
    
    # Check if file ends with silence
    if current_start is not None:
        duration = (len(silent_frames) - current_start) * frame_duration
        if duration >= min_silence_duration:
            silence_starts.append(current_start * frame_duration)
            silence_durations.append(duration)
    
    return silence_starts, silence_durations

def main():
    parser = argparse.ArgumentParser(description='Detect long silences in audio files')
    parser.add_argument('path', help='Path to audio file or directory')
    parser.add_argument('--min-duration', type=float, default=5.0,
                       help='Minimum silence duration in seconds (default: 5.0)')
    parser.add_argument('--threshold', type=float, default=-60,
                       help='Silence threshold in dB (default: -60)')
    args = parser.parse_args()

    path = Path(args.path)
    if path.is_file():
        files = [path]
    else:
        files = list(path.glob('**/*.wav'))

    for file in files:
        try:
            silence_starts, silence_durations = detect_silence(
                str(file),
                min_silence_duration=args.min_duration,
                threshold_db=args.threshold
            )
            
            if silence_starts:
                print(f"\n{file}:")
                for start, duration in zip(silence_starts, silence_durations):
                    print(f"  Silence at {start:.2f}s for {duration:.2f}s")
        except Exception as e:
            print(f"Error processing {file}: {e}")

if __name__ == '__main__':
    main()