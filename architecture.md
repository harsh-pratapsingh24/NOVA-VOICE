# Architecture Diagram: Voice Assistant

```mermaid
graph TD
    A[User Voice] -->|Audio Input| B[Microphone]
    B -->|Audio Chunk| C{Wake Word Detection}
    C -->|Detected| D[STT: Google Speech Recognition]
    C -->|Wait| B
    D -->|Text Query| E[LLM: Groq Llama-3]
    E -->|Text Response| F[TTS: Edge-TTS]
    F -->|Audio File| G[Audio Playback: Pygame]
    G -->|Voice Output| H[User]
    
    subgraph Latency Tracking
        D -.-> |Timing| I[Latency Benchmarking]
        E -.-> |Timing| I
        F -.-> |Timing| I
    end
```

## System Flow
1. **Wake Word Detection**: The system continuously listens for the word "assistant".
2. **STT (Speech to Text)**: Once the wake word is detected, the next segment of audio is captured and transcribed using the Google Speech Recognition API.
3. **LLM Interaction**: The transcribed text is sent to the Groq API (Llama-3 model) for a concise response.
4. **TTS (Text to Speech)**: The LLM's response is converted to audio using Microsoft Edge's Neural TTS.
5. **Playback**: The audio is played back to the user via Pygame.
6. **Latency Measurement**: Each stage (STT, LLM, TTS) is timed to provide a detailed performance report.
