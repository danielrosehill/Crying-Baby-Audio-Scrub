The purpose of this repo is to test out various background noise removal and audio inpainting utilities to see whether any is capable of achieving a significant feat for parents: removing fussing babies from the soundtrack.

## Use Case

I'm working on an idea for a voice app that uses STT. One of the major benefits of voice tech in my opinion is for busy parents who may need to dictate emails rather than type them. Very frequently, kids begin fussing when you least expect it.

There are two things I want to try out:

- "Press a button" AI audio scrubbing: I'll try those outside of the repo
- Deep learning / local AI: I can run those tests here

This is a one-time experiment. I want to get a sense for whether this is at all possible and, if so, how good the scrubbing is.

The goal isn't really to produce "kid-free" audio either; it's to get clean enough audio so that the STT can work, as otherwise it's almost impossible to get a good transcript.

The pipeline I would like to attempt:

- Noisy audio with baby →
- Clean audio with AI →
- Successful transcript

## Files

The repo has `original-note.mp3`.

I was recording a shopping list when my son began crying and thought I would try to grab a minute of audio for this experiment. It's unedited.

I would like to see if this can be scrubbed, what the results are like, and then (the litmus test) can it be STT-ed successfully. I would probably need the cleaned audio just to be able to provide a good source of truth.

`cancel.mp3` is a segment of (mostly) crying/fussing. My thinking being that this might be useful to identify the frequencies and/or vocal patterns we're trying to cancel.

## Conda

I tried and failed to use a deep learning tool locally before, but let's make one more attempt before resorting to CPU-only processing. Either way, check if there's a conda environment and if not, create one as this is a useful task with many applications beyond this project.