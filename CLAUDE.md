# CLAUDE.md - Crying Baby Audio Scrub Project

## Project Purpose

This repository is for testing audio noise removal and inpainting utilities to determine if they can effectively remove baby crying/fussing from voice recordings to enable successful speech-to-text (STT) transcription.

## User Intent and Vision

Daniel is exploring whether AI-powered audio scrubbing can solve a practical problem for parents using voice technology: children often start fussing during dictation, making STT transcription fail. This is a **one-time experiment** to assess feasibility and quality.

### Target Pipeline

```
Noisy audio (with baby crying) → AI-cleaned audio → Successful STT transcript
```

The goal is NOT to produce completely silent/kid-free audio, but to clean it enough for STT systems to work properly.

## Audio Files

- **`original-note.mp3`**: Recording of a shopping list with baby crying in background (unedited, real-world test case)
- **`cancel.mp3`**: Isolated segment of baby crying/fussing (may be useful for identifying target frequencies/patterns to remove)

## Technical Approach

### Two Testing Tracks

1. **Cloud/GUI-based tools** ("press a button" AI audio scrubbing) - tested outside this repo
2. **Local deep learning models** - tested within this repo

### Environment Setup

- **Conda environment required**: Check for existing suitable conda environment before creating new one
- **GPU acceleration preferred**: Daniel has AMD RX 7700 XT with ROCm configured
- Previous attempts with deep learning tools locally have failed, but try once more before falling back to CPU-only processing
- This is a useful capability with applications beyond this specific project

## Implementation Guidelines

When working on this project:

1. **Check for existing conda environments** that might suit audio processing/deep learning before creating new ones
2. **Prioritize ROCm/GPU-accelerated solutions** when possible given the hardware
3. **Test the full pipeline**: audio cleaning → STT transcription to validate success
4. **Evaluate quality**: The litmus test is whether STT can successfully transcribe the cleaned audio
5. Focus on **practical experimentation** rather than production-ready code

## Success Criteria

- Clean audio well enough that STT can produce an accurate transcript
- Compare quality of different audio scrubbing approaches
- Document what works and what doesn't for future reference

## Additional Context

For more detailed background, motivation, and the user's thought process, refer to **`context.md`**. That file serves as Daniel's scratchpad and contains the fuller narrative behind this project, including personal anecdotes and use case details. Use `context.md` when you need deeper understanding of the "why" behind the technical requirements.
