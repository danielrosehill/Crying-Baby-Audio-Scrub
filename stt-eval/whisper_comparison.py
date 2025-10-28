#!/usr/bin/env python3
"""
STT Evaluation: Compare original vs DeepNet-processed audio using Whisper API
"""

import os
from openai import OpenAI
from pathlib import Path
import json
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key from environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment. Please set it in .env file.")
client = OpenAI(api_key=api_key)

def transcribe_audio(audio_path, label):
    """Transcribe audio file using Whisper API"""
    print(f"\n{'='*60}")
    print(f"Transcribing: {label}")
    print(f"File: {audio_path}")
    print(f"{'='*60}\n")

    try:
        with open(audio_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="verbose_json"
            )

        return {
            "label": label,
            "file": str(audio_path),
            "text": transcript.text,
            "language": transcript.language,
            "duration": transcript.duration,
            "success": True,
            "error": None
        }

    except Exception as e:
        return {
            "label": label,
            "file": str(audio_path),
            "text": None,
            "language": None,
            "duration": None,
            "success": False,
            "error": str(e)
        }

def main():
    # Define paths
    original = Path("/home/daniel/repos/github/Crying-Baby-Audio-Scrub/stt-eval/source/original.mp3")
    enhanced = Path("/home/daniel/repos/github/Crying-Baby-Audio-Scrub/stt-eval/source/enhanced_output.mp3")

    # Verify files exist
    if not original.exists():
        print(f"ERROR: Original file not found: {original}")
        return
    if not enhanced.exists():
        print(f"ERROR: Enhanced file not found: {enhanced}")
        return

    print("\n🎤 STT EVALUATION: Whisper API Comparison")
    print(f"Timestamp: {datetime.now().isoformat()}")

    # Transcribe both files
    results = {
        "timestamp": datetime.now().isoformat(),
        "model": "whisper-1",
        "original": transcribe_audio(original, "Original (with baby crying)"),
        "enhanced": transcribe_audio(enhanced, "DeepNet Processed")
    }

    # Save results to JSON
    output_file = Path("stt_comparison_results.json")
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'='*60}")
    print("RESULTS SUMMARY")
    print(f"{'='*60}\n")

    # Display results
    for key in ["original", "enhanced"]:
        result = results[key]
        print(f"\n📝 {result['label']}")
        print(f"   Success: {result['success']}")
        if result['success']:
            print(f"   Language: {result['language']}")
            print(f"   Duration: {result['duration']:.2f}s")
            print(f"   Transcript:\n   \"{result['text']}\"")
        else:
            print(f"   Error: {result['error']}")

    print(f"\n{'='*60}")
    print(f"Results saved to: {output_file.absolute()}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
